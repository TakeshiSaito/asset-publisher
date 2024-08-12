from PySide2.QtWidgets import QLineEdit, QHBoxLayout, QLabel

from AssetPublisher.Model import OptionValue
from AssetPublisher.View.IOptionView import IOptionView, OptionNameMissing


class LineEdit(QHBoxLayout, IOptionView):

    def __init__(self, **kwargs):
        super(LineEdit, self).__init__()

        try:
            self.__option_name = kwargs["option_name"]
        except KeyError:
            raise OptionNameMissing("option_name is required.")

        self.__required = kwargs.get("required", False)

        label = QLabel()
        self.line_edit = QLineEdit()

        self.addWidget(label)
        self.addWidget(self.line_edit)

        label.setText(kwargs.get("label", ""))
        self.line_edit.setText(kwargs.get("default_value", ""))
        self.line_edit.setPlaceholderText(kwargs.get("placeholder_text", ""))

    @property
    def option_name(self):
        return self.__option_name

    @property
    def value(self):
        return self.line_edit.text()

    @property
    def is_required(self) -> bool:
        return self.__required

    def get_option_value(self) -> OptionValue:
        return OptionValue(self.option_name, self.value, self.is_required)
