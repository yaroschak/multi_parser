from typing import List
from main import pars


def get_urls(file: str) -> List[str]:
    return ['https://rulya-bank.com.ua', 'https://cs231n.github.io']


urls = get_urls('test.txt')

for url in urls:
    print(url)
    pars.delay(url=url)
