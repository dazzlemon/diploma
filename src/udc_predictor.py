"""
Core logic of the application
"""

import spacy
from functional import seq
from udc_predictor_text_input import UdcPredictorTextInput

def extract_keywords(text: UdcPredictorTextInput, top_k=50):
    """
    Extract keywords from text (scientific work)
    """
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(text)

    return seq(doc.noun_chunks)\
        .filter(lambda chunk: not contains_stop_words(chunk))\
        .map(remove_chunk_punctuation)\
        .map(strip_punctuation)\
        .filter(lambda chunk_text: len(chunk_text) > 1)\
        .count_by_value()\
        .sorted(lambda x: x[1], True)\
        .take(top_k)\
        .map(lambda pair: pair[0])


def remove_chunk_punctuation(chunk):
    """Remove punctuation marks from the chunk"""
    return ' '\
        .join(seq(chunk)\
            .filter(lambda token: not token.is_punct)\
            .map(lambda token: token.text)\
        )\
        .strip()\
        .lower()


def strip_punctuation(noun_text):
    """Strips noun text from possible punctuation"""
    return noun_text.rstrip('.')


def contains_stop_words(chunk):
    """Whether chunk has any stopwords"""
    return seq(chunk).exists(lambda token: token.is_stop)
