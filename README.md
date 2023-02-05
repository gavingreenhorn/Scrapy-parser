# Асинхронный парсер PEP
## Автор
[Злобин Иван](https://github.com/gavingreenhorn)
## Стек
- Python 3.9
- [Scrapy](https://docs.scrapy.org/)
## Развертывание
>`git clone git@github.com:gavingreenhorn/scrapy_parser_pep`

>`python -m venv venv`

>`$ source venv/bin/activate`

>`python -m pip install -r requirements.txt`
## Запуск
>`scrapy crawl pep`
## Результат
- парсинг документов PEP со страницы https://peps.python.org/
- создание файла pep_<время запуска>.csv в корне проекта со списком PEP.
- создание файла status_summary_<время запуска>.csv в корне проекта со количеством PEP в каждом статусе.


