import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def is_shorten_link(url):
    is_shorten_link = urlparse(url)
    if is_shorten_link.netloc == 'vk.cc':
        return is_shorten_link.path[1:]
    else:
        return False


def test_user_input(user_input):
    try:
        test_user_input = requests.get(user_input)
        test_user_input.raise_for_status()
        return True
    except requests.exceptions.HTTPError:
        return False
    except requests.exceptions.SSLError:
        return False
    except Exception:
        return False


def shorten_link(token, user_input):
    params = {
        'access_token': token,
        'url': user_input,
        'v': '5.131',
    }
    url = 'https://api.vk.com/method/utils.getShortLink'
    shorten_link = requests.get(url, params=params)
    shorten_link.raise_for_status()
    shorten_link = shorten_link.json()
    shorten_link = shorten_link['response']['short_url']
    return shorten_link


def count_clicks(token, key):
    params = {
        'access_token': token,
        'key': key,
        'interval': 'forever',
        'v': '5.131',
    }
    url = 'https://api.vk.com/method/utils.getLinkStats'
    count_clicks = requests.get(url, params=params)
    count_clicks.raise_for_status()
    count_clicks = count_clicks.json()
    count_clicks = count_clicks['response']['stats'][0]['views']
    return count_clicks


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('API_TOKEN')
    user_input = input('Enter your URL: ')
    if test_user_input(user_input):
        if is_shorten_link(user_input):
            is_shorten_link = is_shorten_link(user_input)
            count_clicks = count_clicks(token, is_shorten_link)
            print('Count clicks: ', count_clicks)
        else:
            shorten_link = shorten_link(token, user_input)
            print(shorten_link)
    else:
        print('Invalid URL')