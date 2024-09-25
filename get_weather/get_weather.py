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
    location_search = ['Шереметьево', 'Лондон', 'Череповец']
    url_template = 'https://wttr.in/{}'
    for location in location_search:
        url = url_template.format(location)
        print(get_weather_forecast(url, weather, payload))


if __name__ == "__main__":
    main()