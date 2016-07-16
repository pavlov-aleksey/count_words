from collections import Counter

import utils


def count_words(text_blocks):
    return sum((utils.count_words(text_block) for text_block in text_blocks), Counter())


if __name__ == '__main__':
    print('Most frequent words are ', utils.frequent_words(count_words(utils.text_blocks())))
