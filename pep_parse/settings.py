BOT_NAME = 'pep_parse'
SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'
FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        # ваш pytest снова противоречит ТЗ
        # {'number': 'Номер', 'name': 'Название', 'status': 'Статус'},
        'overwrite': True
    }
}
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
