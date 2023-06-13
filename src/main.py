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

            for cl, count in predict(text, model):
                print(cl)
                print(count)
                print('')
        case UDCComparisonMode(_, _, udc):
            print('predict+compare')
            print(f'{udc=}')
            prediction = predict(text, model)
            just_classes = [cl for cl, _ in prediction]
            intersection = set(udc.classes) & set(just_classes)
            union = set(udc.classes).union(set(just_classes))
            jaccard = len(intersection) / len(union)
            print(jaccard)
            for cl, count in prediction:
                print(cl)
                print(count)
                print('')
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


if __name__ == '__main__':
    main()
