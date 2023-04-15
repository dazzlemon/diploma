"""CLI tools for UDC predictor"""
import argparse
from mode import Mode, TrainingMode, PredictionMode, UDCComparisonMode

def parse_args() -> Mode:
    """CLI args receiver for UDC predictor"""
    parser = argparse.ArgumentParser(description='UDC Classifier')
    parser.add_argument(
        'model_filename',
        help='the name of the existing model file'
    )
    parser.add_argument('text_filename', help='the name of the input text file')
    parser.add_argument(
        '--training',
        dest='new_model_filename',
        help='the name of the output file for the updated model',
        required=False
    )
    parser.add_argument(
        '--udc',
        help='the input UDC code to compare against the predicted classes',
        required=False
    )
    args = parser.parse_args()

    if args.new_model_filename and args.udc:
        raise ValueError("Cannot specify both --training and --udc options.")

    if args.new_model_filename:
        return TrainingMode(
            model_filename=args.model_filename,
            text_filename=args.text_filename,
            new_model_filename=args.new_model_filename
        )
    if args.udc:
        return UDCComparisonMode(
            model_filename=args.model_filename,
            text_filename=args.text_filename,
            udc=args.udc
        )
    return PredictionMode(
        model_filename=args.model_filename,
        text_filename=args.text_filename
    )
