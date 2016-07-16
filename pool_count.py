from collections import Counter
from multiprocessing import Pool

import config
import utils


def count_words(text_blocks):
    pool = Pool(config.POOL_SIZE)
    results = [pool.apply_async(utils.count_words, (text_block,)) for text_block in text_blocks]

    return sum([result.get() for result in results], Counter())


if __name__ == '__main__':
    print('Most frequent words are ', utils.frequent_words(count_words(utils.text_blocks())))
