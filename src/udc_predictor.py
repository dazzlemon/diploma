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
        .filter(lambda chunk:
            all(not token.is_stop for token in chunk if token.is_alpha)
        )\
        .map(lambda chunk: ' ' \
            .join(token.text for token in chunk if not token.is_punct) \
            .strip() \
            .lower()
            # Remove punctuation marks from the chunk
        )\
        .map(lambda chunk_text: chunk_text.rstrip('.')
        # I had the same word appear twice, once with a dot at the end
        )\
        .filter(lambda chunk_text: len(chunk_text) > 1)\
        .map(lambda e: (e, 1))\
        .reduce_by_key(lambda a, b: a + b)\
        .sorted(lambda x: x[1], True)\
        .take(top_k)\
        .map(lambda pair: pair[0])
