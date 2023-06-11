"""Internal representation for keywords"""
from dataclasses import dataclass
from typing import List

Keyword = str

@dataclass
class Keywords:
    """
		This class is responsible for parsing keywords from string.
		"""
    strings: List[str]

    @classmethod
    def from_string(cls, string: str) -> 'Keywords':
        """
        Parses an object of this class from string.
        """
        return cls(string.split(','))
