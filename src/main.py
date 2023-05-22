"""UDC classes predictor for scientific works in english"""
import pprint
from pathlib import Path
from parse_args import parse_args

UdcPredictorTextInput = str
UdcPredictorModel = str

def read_model(filename: str) -> UdcPredictorModel:
    """
    Given filename read that file
    and return its contents parsed as UdcPredictorModel.
    """
    # I don't know the encoding beforehand, and it should be ok anyways
    # pylint: disable-next=unspecified-encoding
    return Path(filename).read_text()


def read_text(filename: str) -> UdcPredictorTextInput:
    """
    Given filename read that file
    and return its contents parsed as UdcPredictorTextInput.
    """
    # I don't know the encoding beforehand, and it should be ok anyways
    # pylint: disable-next=unspecified-encoding
    return Path(filename).read_text()


if __name__ == '__main__':
    mode = parse_args()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(mode)

    model = read_model(mode.model_filename)
    text = read_text(mode.text_filename)

    print(f'{model=}')
    print(f'{text=}')
