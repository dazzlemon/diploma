"""
Core logic of the application
"""

from collections import Counter
import spacy
from udc_predictor_text_input import UdcPredictorTextInput

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
            chunk_text = ' ' \
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
