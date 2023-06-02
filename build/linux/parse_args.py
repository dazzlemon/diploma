"""CLI tools for UDC predictor"""
import argparse
from mode import Mode, TrainingMode, PredictionMode, UDCComparisonMode

def parse_args() -> Mode:
    """App mode from CLI args"""
    parser = argparse.ArgumentParser(description='UDC Classifier')
    parser.add_argument('model_filename', help='the name of the model file')
    parser.add_argument('text_filename', help='the name of the input text file')
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '--training',
        dest='new_model_filename',
        help='If this parameter is specified, the model will be trained.',
    )
    group.add_argument(
        '--udc',
        help='the input UDC code to compare against the predicted classes',
    )
    args = parser.parse_args()

    arguments = {
        "model_filename": args.model_filename,
        "text_filename": args.text_filename
    }

    if args.new_model_filename:
        arguments["new_model_filename"] = args.new_model_filename
        mode = TrainingMode
    elif args.udc:
        arguments["udc"] = args.udc
        mode = UDCComparisonMode
    else:
        mode = PredictionMode

    return mode(**arguments)
