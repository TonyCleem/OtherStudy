import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def is_shorten_link(url):
    parse = urlparse(url)
    test = 'vk.cc'
    if test in parse.netloc:
        return parse.path[1:]
    else:
        return False


def shorten_link(token, user_input):
    params = {
        'access_token': token,
        'url': user_input,
        'v': '5.131',
    }
    url = 'https://api.vk.com/method/utils.getShortLink'
    request_on_url = requests.get(url, params=params)
    request_on_url.raise_for_status()
    data_in_json = request_on_url.json()
    shortened_link = data_in_json['response']['short_url']
    return shortened_link


def get_clicks_count(token, key):
    params = {
        'access_token': token,
        'key': key,
        'interval': 'forever',
        'v': '5.131',
    }
    url = 'https://api.vk.com/method/utils.getLinkStats'
    request_on_url = requests.get(url, params=params)
    request_on_url.raise_for_status()
    data_in_json = request_on_url.json()
    clicks_count = data_in_json['response']['stats'][0]['views']
    return clicks_count


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['VK_TOKEN']
    user_input = input('Enter your URL: ')
    if is_shorten_link(user_input):
        key_for_vk = is_shorten_link(user_input)
        clicks_count = get_clicks_count(token, key_for_vk)
        print('Clicks count: ', clicks_count)
    else:
        shortened_link = shorten_link(token, user_input)
        print(shortened_link)



