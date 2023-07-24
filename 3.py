from bs4 import BeautifulSoup
import requests

def count_html_tags(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    all_tags = soup.find_all()
    tags_with_attrs_count = 0
    for tag in all_tags:
        if tag.attrs:
            tags_with_attrs_count += 1
    return [len(all_tags), tags_with_attrs_count]

URL = 'https://greenatom.ru/'
tag_count = count_html_tags(URL)
if tag_count is not None:
    print(f'Количество HTML тегов на странице: {tag_count[0]}\n'
          f'Количество HTML тегов с атрибутами на странице: {tag_count[1]}')

#Количество HTML тегов на странице: 26
#Количество HTML тегов с атрибутами на странице: 22
