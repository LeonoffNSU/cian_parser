import requests
import json
import math
from bs4 import BeautifulSoup


all_links = []
with open('url.txt', 'r') as url_in:
    for index, raw in enumerate(url_in):
        split = raw.split()
        response_url = split[0]
        number_of_offers = int(split[1])
        number_of_pages = math.ceil(number_of_offers / 28)

        if number_of_offers <= 28 * 53:
            stop_cycle = number_of_pages
        else:
            stop_cycle = 54

        all_info = {}
        cnt = 0
        for page in range(1, stop_cycle + 1):
            params_to_get = {'p': page}
            response = requests.get(response_url, params=params_to_get)
            downloaded_data = response.text

            soup = BeautifulSoup(downloaded_data, 'lxml')
            catalog = soup.find('div', class_='_93444fe79c--wrapper--W0WqH')

            while catalog is None:
                response = requests.get(response_url, params=params_to_get)
                downloaded_data = response.text
                soup = BeautifulSoup(downloaded_data, 'lxml')
                catalog = soup.find('div', class_='_93444fe79c--wrapper--W0WqH')

            all_links_text = catalog.find_all('a')

            for tag_link in all_links_text:
                link = tag_link.get('href')
                info = []

                if 'novosibirsk.cian.ru/sale' in link and link not in all_links:
                    cnt += 1
                    div_upper = tag_link.find_parent()
                    list_of_a_text = div_upper.find_all('a')
                    for a in list_of_a_text:
                        info.append(a.text)

                    info = list(filter(lambda x: len(x) > 0, info))

                    span_tag_with_price = div_upper.find('span', {'data-mark': 'MainPrice'})
                    price = span_tag_with_price.text

                    description_tag = div_upper.find('div', {'data-name': 'Description'})
                    description = description_tag.text

                    all_links.append(link)
                    all_info[cnt] = [info, price, description, link]

            print(f'Пройдено веб-страниц: {page} из {stop_cycle}')

        print(f'Парсинг завершен, промежуточные данные находятся в файле intermediate_data{index + 1}.json')
        with open(f'intermediate_data{index + 1}.json', 'w', encoding='utf-8') as f_out:
            json.dump(all_info, f_out, indent=2, ensure_ascii=False)
