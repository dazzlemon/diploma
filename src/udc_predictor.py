"""
Core logic of the application
"""

from typing import List, Tuple
import spacy
from functional import seq
from udc_predictor_text_input import UdcPredictorTextInput
from udc_predictor_model import UdcPredictorModel, UdcPredictorModelRecord
from udc_code import UdcCode
from keywords import Keywords

def extract_keywords(
    text: UdcPredictorTextInput, top_k=50
) -> List[Tuple[str, int]]:
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
        .take(top_k)


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


def predict(text: UdcPredictorTextInput, model: UdcPredictorModel) -> UdcCode:
    """
    predict UdcCode for `text` using `model`.
    """
    classes = []
    keywords = extract_keywords(text)

    for keyword, f in keywords:
        for record in model.records:
            if record.keyword == keyword:
                classes.append((record.udc_class, record.weight))

    return seq(classes)\
        .reduce_by_key(lambda a, b: a + b)\
        .sorted(lambda x: x[1], True)\
        .to_list()


def train(
    text: UdcPredictorTextInput,
    model: UdcPredictorModel,
    udc: UdcCode,
    keywords: Keywords,
) -> UdcPredictorModel:
    """
    Build upon `model` using `text`, `udc`, and `keywords`.
    """
    new_model_records = seq(extract_keywords(text))\
        .where(lambda pair: pair[0] in keywords.strings)\
        .flat_map(lambda pair: seq(udc.classes)\
            .map(lambda cl: UdcPredictorModelRecord(pair[0], cl, pair[1]))
        )\
        .to_list()

    for old_record in model.records:
        for i, new_record in enumerate(new_model_records):
            if new_record.keyword == old_record.keyword \
                    and new_record.udc_class == old_record.udc_class:
                new_model_records[i] = UdcPredictorModelRecord(
                    new_record.keyword,
                    new_record.udc_class,
                    new_record.weight + old_record.weight
                )
                break
        else:
            new_model_records.append(old_record)

    for i in new_model_records:
        print(i)

    return UdcPredictorModel(new_model_records)
