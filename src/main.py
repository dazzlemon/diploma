"""UDC classes predictor for scientific works in english"""
import pprint
from parse_args import parse_args

if __name__ == '__main__':
    mode = parse_args()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(mode)
