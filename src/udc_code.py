"""UDC code representation"""
from dataclasses import dataclass
from typing import List

UdcClass = str

@dataclass
class UdcCode:
    """UDC code representation"""
    classes: List[UdcClass]


    @classmethod
    def from_string(cls, string: str) -> 'UdcCode':
        """
        Parses a string and returns an object of this class.
        
        :param string: Is expected to be the input of `__str__`
        """
        return cls(string.split(','))


    # TODO:
		# override is supported in python 3.12
    # @override
    def __str__(self) -> str:
        return ','.join(self.classes)
