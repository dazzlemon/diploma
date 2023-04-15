"""
UDC classes predictor for scientific works in english.
"""
from udc_arg_parser import parse_args
from mode import TrainingMode, UDCComparisonMode

if __name__ == '__main__':
    mode = parse_args()

    print(mode.mode_name)
    print(f'\t{mode.text_filename=}')
    print(f'\t{mode.model_filename=}')
    if isinstance(mode, TrainingMode):
        print(f'\t{mode.new_model_filename=}')
    elif isinstance(mode, UDCComparisonMode):
        print(f'\t{mode.udc_code=}')
    else:
        print(f'\t{mode.new_model_filename=}')
