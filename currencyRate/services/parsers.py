import requests
import lxml.html as html


async def parse_bank_web(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            page = response.content
            parsed = html.fromstring(page)
            return parsed
        else:
            raise ValueError('Error: ' + str(response.status_code))
    except ValueError as ve:
        print(ve)


async def parse_text_that_contains_money_info_from_atlantida(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            text = response.content.decode('utf-8').replace('\n', '')
            return text.replace('\t', '').replace('\r', '').replace(' ', '')
        else:
            raise ValueError('Error: ' + str(response.status_code))
    except ValueError as ve:
        print(ve)


