import requests


def get(
        article_id, option,
        language,
    ):
    url_template = 'https://wttr.in/{}?{}&{}'
    url = url_template.format(article_id, option, language)
    response = requests.get(url)
    response.raise_for_status()
    result = response.text
    return print(result)


def main():
    option = 'nqmMT'
    language = 'lang=ru'
    article_id = ['Шереметьево', 'Лондон', 'Череповец']
    for point in article_id:
        get(point, option, language)


if __name__ == "__main__":
    main()