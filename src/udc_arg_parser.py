"""CLI tools for UDC predictor"""
import argparse
from typing import Optional
from mode import Mode, TrainingMode, PredictionMode, UDCComparisonMode

class UDCArgParser:
    """CLI args receiver for UDC predictor"""
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='UDC Classifier')
        self.parser.add_argument('model_filename',
                                 help='the name of the existing model file')
        self.parser.add_argument('text_filename',
                                 help='the name of the input text file')
        self.parser.add_argument('--training', dest='new_model_filename',
                                 help='the name of the output file for the updated model',
                                 required=False)
        self.parser.add_argument('--udc',
                                 help='the input UDC code to compare against the predicted classes',
                                 required=False)
        self.args = self.parser.parse_args()

        if self.args.new_model_filename and self.args.udc:
            raise ValueError("Cannot specify both --training and --udc options.")

    @property
    def model_filename(self) -> str:
        """The name of the existing model file."""
        return self.args.model_filename

    @property
    def text_filename(self) -> str:
        """The name of the input text file."""
        return self.args.text_filename

    @property
    def new_model_filename(self) -> Optional[str]:
        """The name of the output file for the updated model, if in training mode."""
        return self.args.new_model_filename

    @property
    def udc_code(self) -> Optional[str]:
        """
				The input UDC code to compare against the predicted classes, if in UDC comparison mode
				"""
        return self.args.udc

    @property
    def mode(self) -> Mode:
        """The current mode of the program."""
        if self.new_model_filename:
            return TrainingMode()
        if self.udc_code:
            return UDCComparisonMode()
        return PredictionMode()
