from PySide2.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QLabel, QFileDialog

from AssetPublisher.Model import OptionValue
from AssetPublisher.View.IOptionView import IOptionView, OptionNameMissing


class FolderDialog(QHBoxLayout, IOptionView):

    def __init__(self, **kwargs):
        super(FolderDialog, self).__init__()

        try:
            self.__option_name = kwargs["option_name"]
        except KeyError:
            raise OptionNameMissing("option_name is required.")

        self.__required = kwargs.get("required", False)

        label = QLabel()
        self.line_edit_folder_path = QLineEdit()
        self.__dialog_btn = QPushButton('Select Folder')

        self.addWidget(label)
        self.addWidget(self.line_edit_folder_path)
        self.addWidget(self.__dialog_btn)

        label_value = kwargs.get("label", "")
        label.setText(label_value)

        placeholder_text = kwargs.get("placeholder_text", "")
        self.line_edit_folder_path.setPlaceholderText(placeholder_text)

        default_value = kwargs.get("default_value", "")
        self.line_edit_folder_path.setText(default_value)

        self.__dialog_btn.clicked.connect(self.open_folder_dialog)

    def open_folder_dialog(self):
        folder = QFileDialog.getExistingDirectory(None, 'Select Folder')
        if folder:
            self.line_edit_folder_path.setText(folder)

    @property
    def option_name(self):
        return self.__option_name

    @property
    def value(self):
        return self.line_edit_folder_path.text()

    @property
    def is_required(self) -> bool:
        return self.__required

    def get_option_value(self) -> OptionValue:
        return OptionValue(self.option_name, self.value, self.is_required)
