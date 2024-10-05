import requests
import os
import pprint
from dotenv import load_dotenv
from urllib.parse import urlparse




def test_user_link(user_input):
    test_user_link = requests.get(user_input)
    test_user_link.raise_for_status()
    test_user_link = test_user_link.ok
    return test_user_link


def shorten_link(token, link):
    params = {
        'access_token': token,
        'url': link,
        'v': '5.131',
    }
    url = 'https://api.vk.com/method/utils.getShortLink'
    shorten_link = requests.get(url, params=params)
    shorten_link.raise_for_status()
    shorten_link = shorten_link.json()
    shorten_link = shorten_link['response']['short_url']

    url = '{key}'
    url = url.format(key=shorten_link)
    parsed = urlparse(url)
    parsed = parsed.path[1:]
    return parsed

def count_clicks(token, link, key, interval):
    params = {
        'access_token': token,
        'url': link,
        'key': key,
        'interval': interval,
        'v': '5.131',
    }
    url = 'https://api.vk.com/method/utils.getLinkStats'

    count_clicks = requests.get(url, params=params)
    count_clicks.raise_for_status()
    count_clicks = count_clicks.json()
    return count_clicks



if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('API_TOKEN')
    method = 'utils.getShortLink'
    url = 'https://api.vk.com/method/{method}'
    user_input = input('Enter your URL: ')

    try:
        test_user_link(user_input)
        if test_user_link:
            shorten_link = shorten_link(token, user_input)
            interval_input = input('Enter interval (hour, day, week, month, forever): ')
            count_clicks = count_clicks(token, user_input, shorten_link, interval_input)
            pprint.pprint(count_clicks)
    except requests.exceptions.HTTPError:
        print('Invalid URL')




#      https://dvmn.org/modules
#                                 https://dvmns.org/modules