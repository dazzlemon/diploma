"""
UDC classes predictor for scientific works in english
"""

from udc_arg_parser import UDCArgParser

if __name__ == '__main__':
    udc_parser = UDCArgParser()

    if udc_parser.is_training_mode():
        print('training')
        print(f'\t{udc_parser.get_text_filename()=}')
        print(f'\t{udc_parser.get_model_filename()=}')
        print(f'\t{udc_parser.get_new_model_filename()=}')
    elif udc_parser.is_udc_comparison_mode():
        print('UDC comparison')
        print(f'\t{udc_parser.get_text_filename()=}')
        print(f'\t{udc_parser.get_model_filename()=}')
        print(f'\t{udc_parser.get_udc_code()=}')
    else:
        print('prediction')
        print(f'\t{udc_parser.get_text_filename()=}')
        print(f'\t{udc_parser.get_model_filename()=}')
        print(f'\t{udc_parser.get_new_model_filename()=}')
        print(f'\t{udc_parser.get_udc_code()=}')
