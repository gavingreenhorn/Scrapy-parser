import os.path
from pathlib import Path

BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
RESULTS_DIR_NAME = 'results'
STATUS_SUMMARY_NAME = 'status_summary_{now}.csv'
PEP_LIST_NAME = 'pep_%(time)s.csv'

(Path(__name__).absolute().parent / RESULTS_DIR_NAME).mkdir(exist_ok=True)

# AssertionError: Убедитесь, что в ключе словаря `FEEDS`
# перед именем файла указан путь к директории `results/`
# - при использовании конкатенации пути из pathlib
# поэтому используется os.path.join
FEEDS = {
    os.path.join(RESULTS_DIR_NAME, PEP_LIST_NAME): {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
