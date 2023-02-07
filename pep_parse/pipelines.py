import csv
from collections import Counter
from datetime import datetime
from pathlib import Path

from .settings import RESULTS_DIR_NAME, STATUS_SUMMARY_NAME

BASE_DIR = Path(__name__).absolute().parent
CSV_HEADERS = ('Статус', 'Количество')


class PepParsePipeline:
    status_counter = None

    def open_spider(self, spider):
        self.status_counter = Counter()

    def process_item(self, item, spider):
        self.status_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        self.status_counter['Total'] = sum(
            self.status_counter.values())
        file_name = STATUS_SUMMARY_NAME.format(now=datetime.utcnow())
        with open(
            BASE_DIR / RESULTS_DIR_NAME / file_name,
            mode='w',
            encoding='utf-8'
        ) as file:
            writer = csv.writer(
                file,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_MINIMAL)
            writer.writerows([CSV_HEADERS, *self.status_counter.items()])
