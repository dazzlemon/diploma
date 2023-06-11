"""
UdcPredictorModel and everything related to it
"""
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict
import tomlkit
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


    def to_dict(self) -> Dict[str, str]:
        return {
            'keyword': self.keyword,
            'udc_class': self.udc_class,    
            'weight': self.weight,
        }


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


    def to_dict(self) -> List[Dict[str, str]]:
        return seq(self.records).map(lambda record: record.to_dict()).to_list()


def read_model(filename: str) -> UdcPredictorModel:
    """
    Given filename read that file
    and return its contents parsed as UdcPredictorModel.
    """
    return UdcPredictorModel.from_dict(
        # I don't know the encoding beforehand, and it should be ok anyways
        # pylint: disable-next=unspecified-encoding
        tomlkit.loads(Path(filename).read_text())['record']
    )


def write_model(filename: str, model: UdcPredictorModel):
    """
    Write `model` to `filename`
    """
    Path(filename).write_text(tomlkit.dumps({'record': model.to_dict()}))
