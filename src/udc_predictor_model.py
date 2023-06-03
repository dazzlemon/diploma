"""
UdcPredictorModel and everything related to it
"""
from pathlib import Path

UdcPredictorModel = str

def read_model(filename: str) -> UdcPredictorModel:
    """
    Given filename read that file
    and return its contents parsed as UdcPredictorModel.
    """
    # I don't know the encoding beforehand, and it should be ok anyways
    # pylint: disable-next=unspecified-encoding
    return Path(filename).read_text()
