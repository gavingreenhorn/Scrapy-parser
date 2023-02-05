from collections import Counter
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__name__).absolute().parent
RESULTS = BASE_DIR / 'results'


class PepParsePipeline:
    status_counter = Counter()
    file = open(
        f'{RESULTS}/status_summary_{datetime.utcnow()}.csv',
        mode='w',
        encoding='utf-8')

    def open_spider(self, spider):
        self.file.write('Статус,Количество\n')

    def process_item(self, item, spider):
        self.status_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        for status, count in self.status_counter.items():
            self.file.write(f'{status},{count}\n')
        self.file.write(f'Total,{sum(self.status_counter.values())}')
        self.file.close()
