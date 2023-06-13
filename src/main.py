"""UDC classes predictor for scientific works in english"""
from parse_args import parse_args
from udc_predictor_text_input import read_text
from udc_predictor_model import read_model, write_model
from udc_predictor import predict, train
from mode import PredictionMode, UDCComparisonMode, TrainingMode

def main():
    """main duh"""
    mode = parse_args()

    text = read_text(mode.text_filename)
    model = read_model(mode.model_filename)

    print(f'{mode.model_filename=}')
    print(f'{mode.text_filename=}')

    match mode:
        case PredictionMode(_, _):
            print('predict')
            print('')

            print_keywords(predict(text, model))
        case UDCComparisonMode(_, _, udc):
            print('predict+compare')
            print(f'{udc=}')
            print('')

            prediction = predict(text, model)
            just_classes = [cl for cl, _ in prediction]
            print(f'similarity (0-1, more is better) = '
                f'{jaccard(set(udc.classes), set(just_classes))}'
            )
            print('')

            print_keywords(prediction)
        case TrainingMode(
            _,
            _,
            new_model_filename,
            udc,
            keywords
        ):
            print('traing')
            print(f'{udc=}')
            print(f'{new_model_filename=}')
            print(f'{keywords=}')
            new_model = train(text, model, udc, keywords)
            write_model(new_model_filename, new_model)


def print_keywords(keywords_and_freqs):
    """
    Prints keywords and frequencies in pairs formatted for human understanding.
    """
    for the_class, count in keywords_and_freqs:
        print(f'class = {the_class}')
        print(f'weight = {count}')
        print('')


def jaccard(set_a, set_b):
    """Jaccard index"""
    intersection = set_a & set_b
    union = set_a.union(set_b)
    return len(intersection) / len(union)


if __name__ == '__main__':
    main()
