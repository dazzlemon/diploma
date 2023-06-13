"""CLI tools for UDC predictor"""
import argparse
from mode import Mode, TrainingMode, PredictionMode, UDCComparisonMode
from udc_code import UdcCode
from keywords import Keywords

def parse_args() -> Mode:
    """App mode from CLI args"""
    parser = argparse.ArgumentParser(description='UDC Classifier')
    parser.add_argument('model_filename', help='the name of the model file')
    parser.add_argument('text_filename', help='the name of the input text file')
    parser.add_argument(
        '--training',
        dest='new_model_filename',
        help='If this parameter is specified, the model will be trained. '
             'You should also specify --keywords and --udc along with it.',
    )
    parser.add_argument(
        '--udc',
        help='the input UDC code to compare against the predicted classes, '
             'or to be used for trainging (see --training)',
    )
    parser.add_argument(
        '--keywords',
        help='the input keywords to be used for training '
             '(string of words delimeted by a comma). '
             'You should also specify --training and --udc along with it.',
    )
    args = parser.parse_args()

    arguments = {
        "model_filename": args.model_filename,
        "text_filename": args.text_filename
    }

    if args.new_model_filename:
        if args.keywords is None:
            parser.error('--keywords should be specified for training mode')
        if args.udc is None:
            parser.error('--udc should be specified for training mode')
        arguments["new_model_filename"] = args.new_model_filename
        arguments["udc"] = UdcCode.from_string(args.udc)
        arguments["keywords"] = Keywords.from_string(args.keywords)
        mode = TrainingMode
    elif args.udc:
        if args.keywords is not None:
            parser.error('--keywords should only be specified with --training')
        arguments["udc"] = UdcCode.from_string(args.udc)
        mode = UDCComparisonMode
    else:
        if args.keywords is not None:
            parser.error('--keywords should only be specified with --training')
        mode = PredictionMode

    return mode(**arguments)
