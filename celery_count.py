from collections import Counter

from celery import Celery

import utils


def count_words(text_blocks):
    celery = Celery(backend='amqp')
    results = [celery.send_task('celery_tasks.count_words', (text_block,)) for text_block in text_blocks]

    return sum([result.get() for result in results], Counter())


if __name__ == '__main__':
    print('Most frequent words are ', utils.frequent_words(count_words(utils.text_blocks())))
