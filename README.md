**Description**

Scripts for caculating 10 most frequent words in the dataset.
- simple_count.py - single threaded calculation
- pool_count.py - using multiprocessing
- celery_count.py - using celery

**Requirements**
- python 3.4+
- rabbimq-server 2.7.1+

**Deployment**
- git clone https://github.com/pavlov-aleksey/count_words.git
- cd count_words
- virtualenv env -p "python3_path"
- . env/bin/activate
- pip install -r ./requirements.txt
- python -m nltk.downloader punkt
- unpack dataset into 'count_words/data' folder
- celery worker --config=celery_config -P processes -l info -c 8 --detach

**Results**

Most frequent words are
- '0'
- ','
- 'the'
- '$'
- '.'
- ')'
- '(',
- '-'
- 'to'
- 'of'

**Execution time**
- simple_count.py - 344 min
- pool_count.py - 193 min
- celery_count.py - 199 min
