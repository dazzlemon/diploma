"""
UdcPredictorTextInput and everything related to it
"""
from pathlib import Path

UdcPredictorTextInput = str

def read_text(filename: str) -> UdcPredictorTextInput:
    """
    Given filename read that file
    and return its contents parsed as UdcPredictorTextInput.
    """
    # I don't know the encoding beforehand, and it should be ok anyways
    # pylint: disable-next=unspecified-encoding
    return Path(filename).read_text()
