"""
CLI interface for udc predictor for scientific works in english
"""
import argparse

parser = argparse.ArgumentParser(description='UDC Classifier')
parser.add_argument('model_filename',
                    help='the name of the existing model file')
parser.add_argument('text_filename',
                    help='the name of the input text file')
parser.add_argument('--training', dest='new_model_filename',
                    help='the name of the output file for the updated model')
parser.add_argument('--udc',
                    help='the input UDC code to compare against the predicted classes')
args = parser.parse_args()

def get_mode() -> str:
    """
    Determines the mode of the program based on the provided arguments.
    Returns: str: The mode of the program. One of 'training', 'prediction', or 'UDC comparison'.
    Raises: ValueError: If none or more than one of the mode flags are specified.
    """
    if args.new_model_filename:
        return 'training'
    if args.udc:
        return 'udc_comparison'
    return 'prediction'

print(get_mode())
print(f'\t{args.text_filename=}')
print(f'\t{args.model_filename=}')
print(f'\t{args.new_model_filename=}')
print(f'\t{args.udc=}')
