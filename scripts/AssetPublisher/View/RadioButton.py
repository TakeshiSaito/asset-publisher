from PySide2.QtWidgets import QHBoxLayout, QLabel, QRadioButton, QButtonGroup

from AssetPublisher.Model import OptionValue
from AssetPublisher.View.IOptionView import IOptionView, OptionNameMissing


class NeedOptionsError(Exception):
    pass


class RadioButtons(QHBoxLayout, IOptionView):

    def __init__(self, **kwargs):
        super(RadioButtons, self).__init__()

        try:
            self.__option_name = kwargs["option_name"]
        except KeyError:
            raise OptionNameMissing("option_name is required.")

        self.__required = kwargs.get("required", False)

        label = QLabel()
        label.setText(kwargs.get("label", ""))
        self.addWidget(label)

        try:
            options = kwargs["options"]
        except KeyError:
            raise NeedOptionsError("options are required.")

        self.__button_group = QButtonGroup()
        for option in options:
            radio_button = QRadioButton(option)
            self.addWidget(radio_button)
            self.__button_group.addButton(radio_button)

        self.__button_group.buttons()[0].setChecked(True)

    @property
    def option_name(self):
        return self.__option_name

    @property
    def value(self):
        selected_button = self.__button_group.checkedButton()
        if selected_button:
            return selected_button.text()

    @property
    def is_required(self) -> bool:
        return self.__required

    def get_option_value(self) -> OptionValue:
        return OptionValue(self.option_name, self.value, self.is_required)
