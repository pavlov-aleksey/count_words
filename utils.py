from collections import Counter
from itertools import chain, islice
import os

from nltk import word_tokenize

import config


def count_words(text_block):
    counter = Counter()

    for item in text_block:
        for word in word_tokenize(item):
            counter[word] += 1

    return counter


def frequent_words(counter, number=config.FREQUENT_WORDS):
    return sorted(counter, key=counter.get, reverse=True)[:number]


def get_texts():
    for root, dirs, files in os.walk(config.DATA_ROOT):
        for name in files:
            with open(os.path.join(root, name), 'r') as text_file:
                yield text_file.read()


def text_blocks():
    iterator = iter(get_texts())
    for first in iterator:
        yield chain([first], list(islice(iterator, config.BLOCK_SIZE - 1)))
