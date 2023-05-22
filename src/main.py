"""UDC classes predictor for scientific works in english"""
from collections import Counter
import pprint
from pathlib import Path
import spacy
from parse_args import parse_args

UdcPredictorTextInput = str
UdcPredictorModel = str


def extract_keywords(text: UdcPredictorTextInput, top_k=50):
    """
    Extract keywords from text (scientific work)
    """
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(text)
    keywords = []

    noun_chunks = []
    for chunk in doc.noun_chunks:
        is_valid = all(not token.is_stop for token in chunk if token.is_alpha)
        if is_valid:
            # Remove punctuation marks from the chunk
            chunk_text = '' \
                .join(token.text for token in chunk if not token.is_punct) \
                .strip() \
                .lower()

            # I had the same word appear twice, once with a dot at the end
            chunk_text = chunk_text.rstrip('.')

            if len(chunk_text) > 1:
                noun_chunks.append(chunk_text)

    keyword_counts = Counter(noun_chunks)
    sorted_keywords = keyword_counts.most_common(top_k)
    keywords = [keyword for keyword, count in sorted_keywords]

    return keywords


def read_model(filename: str) -> UdcPredictorModel:
    """
    Given filename read that file
    and return its contents parsed as UdcPredictorModel.
    """
    # I don't know the encoding beforehand, and it should be ok anyways
    # pylint: disable-next=unspecified-encoding
    return Path(filename).read_text()


def read_text(filename: str) -> UdcPredictorTextInput:
    """
    Given filename read that file
    and return its contents parsed as UdcPredictorTextInput.
    """
    # I don't know the encoding beforehand, and it should be ok anyways
    # pylint: disable-next=unspecified-encoding
    return Path(filename).read_text()


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
