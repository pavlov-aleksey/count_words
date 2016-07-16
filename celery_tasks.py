import celery

import utils


@celery.task
def count_words(text_block):
    return utils.count_words(text_block)
