import os
import string

import numpy as np
from nltk.corpus import stopwords
from nltk import word_tokenize


DOC_PATH = "docs/"


def get_sentences_from_doc(filepath):
    """
    function that returns a list of sentences given a doc
    """
    with open(os.path.join(DOC_PATH, filename)) as file:
        # read the file into a list of sentences
        sentences = file.readlines()
        return sentences


def clean_sentences(sentences):
    """
    function to remove stop words and punctuation from every sentence.
    sentences is a list of sentences (string)
    """
    # create list of stop words and punctuation to remove
    stop_words = set(stopwords.words('english')) | set(string.punctuation)

    # remove stop words and punctuation from every sentence
    cleaned_sentences = [[word for word in word_tokenize(sentence) \
                        if word not in stop_words] for sentence in sentences]

    return cleaned_sentences


if __name__ == "__main__":
    for filename in os.listdir(DOC_PATH):
        if filename.endswith('.txt'):
            # read the sentences from the doc
            sentences = get_sentences_from_doc(filename)

            # convert all the sentences to lowercase
            sentences = [sentence.lower() for sentence in sentences]

            # remove stop words and punctuation from clean_sentences
            cleaned_sentences = clean_sentences(sentences)
