import argparse
from typing import Optional

class UDCArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='UDC Classifier')
        self.parser.add_argument('model_filename',
                                 help='the name of the existing model file')
        self.parser.add_argument('text_filename',
                                 help='the name of the input text file')
        self.parser.add_argument('--training', dest='new_model_filename',
                                 help='the name of the output file for the updated model')
        self.parser.add_argument('--udc',
                                 help='the input UDC code to compare against the predicted classes')
        self.args = self.parser.parse_args()

    def get_model_filename(self) -> str:
        return self.args.model_filename

    def get_text_filename(self) -> str:
        return self.args.text_filename

    def get_new_model_filename(self) -> Optional[str]:
        return self.args.new_model_filename

    def get_udc_code(self) -> Optional[str]:
        return self.args.udc

    def is_training_mode(self) -> bool:
        return self.args.new_model_filename is not None

    def is_udc_comparison_mode(self) -> bool:
        return self.args.udc is not None

    def is_prediction_mode(self) -> bool:
        return not self.is_training_mode() and not self.is_udc_comparison_mode()
