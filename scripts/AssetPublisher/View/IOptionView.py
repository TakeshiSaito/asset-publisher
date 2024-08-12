from abc import abstractmethod

from AssetPublisher.model import OptionValue


class OptionNameMissing(Exception):
    pass


class IOptionView:

    @abstractmethod
    def get_option_value(self) -> OptionValue:
        raise NotImplementedError()
