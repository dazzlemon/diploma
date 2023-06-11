"""
UdcPredictorModel and everything related to it
"""
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict
import toml
from functional import seq
from udc_code import UdcClass

@dataclass
class UdcPredictorModelRecord:
    """
    Internal representation for model record.
    """
    keyword: str
    udc_class: UdcClass
    weight: int


    @classmethod
    def from_dict(cls, the_dict: Dict[str, str]) -> 'UdcPredictorModelRecord':
        """
        Parse udc predictor model record from dict.
        """
        return cls(
            the_dict['keyword'],
            the_dict['udc_class'],
            the_dict['weight']
        )


@dataclass
class UdcPredictorModel:
    """
    Internal representation for the udc predictor model.
    """
    records: List[UdcPredictorModelRecord]


    @classmethod
    def from_dict(cls, records: List[Dict[str, str]]) -> 'UdcPredictorModel':
        """
        Parse udc predictor model from dict.
        """
        return cls(seq(records).map(UdcPredictorModelRecord.from_dict))


def read_model(filename: str) -> UdcPredictorModel:
    """
    Given filename read that file
    and return its contents parsed as UdcPredictorModel.
    """
    return UdcPredictorModel.from_dict(
        # I don't know the encoding beforehand, and it should be ok anyways
        # pylint: disable-next=unspecified-encoding
        toml.loads(Path(filename).read_text())['record']
    )
