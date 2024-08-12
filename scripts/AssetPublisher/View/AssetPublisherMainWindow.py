from abc import abstractmethod
from pathlib import Path
from typing import List

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMainWindow, QMessageBox, QGroupBox, QVBoxLayout

from AssetPublisher.Model import OptionValue
from AssetPublisher.UseCase import PublishAssetUseCase
from AssetPublisher.View.FolderDialog import FolderDialog
from AssetPublisher.View.IOptionView import IOptionView
from AssetPublisher.View.LineEdit import LineEdit
from AssetPublisher.View.RadioButton import RadioButtons


class IMainWindow:

    @abstractmethod
    def update_progress_bar(self, value: int, status: str):
        raise NotImplementedError()

    @abstractmethod
    def show_confirm_dialog(self, title: str, message: str):
        raise NotImplementedError()

    @abstractmethod
    def on_click_publish(self):
        raise NotImplementedError()


class MainWindow(QMainWindow, IMainWindow):
    UI_FILE = Path(__file__).parent / 'resources' / 'AssetPublisherMainWindow.ui'

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.__widget = QUiLoader().load(self.UI_FILE.as_posix())
        self.setCentralWidget(self.__widget)
        self.resize(400, 313)

        self.__widget.setWindowTitle('Asset Publisher')

        self.__widget.btn_publish.clicked.connect(self.on_click_publish)

        self.__checkBox_bypass_validation = self.__widget.checkBox_bypass_validation
        self.__progress_bar = self.__widget.progressBar
        self.__groupBox_layout: QVBoxLayout = self.__widget.groupBox_options.layout()

        self.__option_uis: List[IOptionView] = []

    @property
    def bypass_validation(self):
        return self.__widget.checkBox_bypass_validation.isChecked()

    @property
    def option_values(self) -> List[OptionValue]:
        values = [ui.get_option_value() for ui in self.__option_uis]
        return values

    def show(self, **options):

        for option_name, value in options.items():
            option = value.copy()
            option['option_name'] = option_name

            if value['type'] == 'radio':
                option_ui = RadioButtons(**option)
            elif value['type'] == 'line_edit':
                option_ui = LineEdit(**option)
            elif value['type'] == 'folder_dialog':
                option_ui = FolderDialog(**option)
            else:
                raise ValueError(f'Invalid option type: {option[type]}')

            self.__groupBox_layout.addLayout(option_ui)
            self.__option_uis.append(option_ui)

        super(MainWindow, self).show()

    def update_progress_bar(self, value: int, status: str):
        self.__progress_bar.setValue(value)
        self.__progress_bar.setFormat(status)

    def show_confirm_dialog(self, title: str, message: str):
        QMessageBox.information(self, title, message, QMessageBox.Ok)

    def on_click_publish(self):
        try:
            options = self.option_values
        except ValueError as e:
            self.show_confirm_dialog('Error', str(e))
            return

        PublishAssetUseCase.execute(options=options,
                                    bypass_validation=self.bypass_validation,
                                    update_progress_bar=self.update_progress_bar,
                                    show_confirm_dialog=self.show_confirm_dialog)
