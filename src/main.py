"""
UDC classes predictor for scientific works in english.
"""
from udc_arg_parser import parse_args
from mode import TrainingMode, UDCComparisonMode

if __name__ == '__main__':
    mode = parse_args()

    if isinstance(mode, TrainingMode):
        print('training')
        print(f'\t{mode.text_filename=}')
        print(f'\t{mode.model_filename=}')
        print(f'\t{mode.new_model_filename=}')
    elif isinstance(mode, UDCComparisonMode):
        print('UDC comparison')
        print(f'\t{mode.text_filename=}')
        print(f'\t{mode.model_filename=}')
        print(f'\t{mode.udc_code=}')
    else:
        print('prediction')
        print(f'\t{mode.text_filename=}')
        print(f'\t{mode.model_filename=}')
        print(f'\t{mode.new_model_filename=}')
        print(f'\t{mode.udc_code=}')
