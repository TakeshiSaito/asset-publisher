from dataclasses import dataclass
from typing import Any


@dataclass
class OptionValue:
    name: str
    value: Any
    required: bool

    def __post_init__(self):
        if self.required and not self.value:
            raise ValueError(f'{self.name} is required.')
