from abc import abstractmethod

from AssetPublisher.Model import OptionValue


class OptionNameMissing(Exception):
    pass


class IOptionView:

    @abstractmethod
    def get_option_value(self) -> OptionValue:
        raise NotImplementedError()
