import requests


def get_weather_forecast(
                         url,
                         weather,
                         payload,
                        ):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    weather = response.text
    return weather


def main():
    weather = ''
    payload = {
               'nqmMT': '',
               'lang': 'ru',
               }
    url_template = 'https://wttr.in/{}'
    location_search = ['Шереметьево', 'Лондон', 'Череповец']
    for location in location_search:
        url = url_template.format(location)
        print(get_weather_forecast(url, weather, payload))


if __name__ == "__main__":
    main()