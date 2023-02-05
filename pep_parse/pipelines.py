from collections import Counter
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__name__).absolute().parent


class PepParsePipeline:
    status_counter = Counter()

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.status_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        file = open(
            BASE_DIR / f'results/status_summary_{datetime.utcnow()}.csv',
            mode='w',
            encoding='utf-8')
        file.write('Статус,Количество\n')
        for status, count in self.status_counter.items():
            file.write(f'{status},{count}\n')
        file.write(f'Total,{sum(self.status_counter.values())}')
        file.close()
