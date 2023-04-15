"""
UDC classes predictor for scientific works in english.
"""
from udc_arg_parser import UDCArgParser
from mode import TrainingMode, UDCComparisonMode

if __name__ == '__main__':
    udc_parser = UDCArgParser()

    if udc_parser.mode is TrainingMode:
        print('training')
        print(f'\t{udc_parser.text_filename=}')
        print(f'\t{udc_parser.model_filename=}')
        print(f'\t{udc_parser.new_model_filename=}')
    elif udc_parser.mode is UDCComparisonMode:
        print('UDC comparison')
        print(f'\t{udc_parser.text_filename=}')
        print(f'\t{udc_parser.model_filename=}')
        print(f'\t{udc_parser.udc_code=}')
    else:
        print('prediction')
        print(f'\t{udc_parser.text_filename=}')
        print(f'\t{udc_parser.model_filename=}')
        print(f'\t{udc_parser.new_model_filename=}')
        print(f'\t{udc_parser.udc_code=}')
