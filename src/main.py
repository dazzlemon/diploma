"""UDC classes predictor for scientific works in english"""
import pprint
from parse_args import parse_args
from udc_predictor_text_input import read_text
from udc_predictor import extract_keywords

def main():
    """main duh"""
    mode = parse_args()

    pretty_printer = pprint.PrettyPrinter(indent=4)
    pretty_printer.pprint(mode)

    print('')

    text = read_text(mode.text_filename)
    for word in extract_keywords(text):
        print(word)


if __name__ == '__main__':
    main()
