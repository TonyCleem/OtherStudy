import os
import json
import requests
import folium
from dotenv import load_dotenv
from geopy import distance
from pprint import pprint
from flask import Flask


def get_list_all_cofee(file_content):
    for coordinates in file_content:
        coffee_coord = dict()
        coffee_coord = {
            'title': coordinates['Name'],
            'latitude': coordinates['geoData']['coordinates'][0],
            'longitude': coordinates['geoData']['coordinates'][1],
        }
        coffee_list.append(coffee_coord)
    return coffee_list


def fetch_coordinates(apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": apikey,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json()['response']['GeoObjectCollection']['featureMember']

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lon, lat


def get_min_distance(coffee_list):
    return coffee_list['distance']


def distance_calculation(coffee_list, first_location):
    for coords in coffee_list:
        second_location = coords['longitude'], coords['latitude']
        new_distance = distance.distance(first_location, second_location).km
        coords['distance'] = new_distance
    return coffee_list


def get_list_nearest_coffees(get_min_distance, list_nearest_coffees):
    nearest = sorted(coffee_list, key=get_min_distance)
    for cofee in nearest[0:5]:
        list_nearest_coffees.append(cofee)
    return list_nearest_coffees


def make_map(latitude, longitude):
    m = folium.Map([latitude, longitude], zoom_start=15)
    folium.Marker(
        location=[latitude, longitude],
        tooltip="Click me!",
        popup="Its me",
        icon=folium.Icon(color="blue"),
    ).add_to(m)

    for coords in list_nearest_coffees:
        folium.Marker(
            location=[coords['longitude'], coords['latitude']],
            tooltip="Click me!",
            popup=coords['title'],
            icon=folium.Icon(color="green"),
        ).add_to(m)

    return m.save("index.html")


def open_map():
    with open("index.html", "r") as map:
        return map.read()


def find_coffees(
        location, coffee_list,
        list_nearest_coffees, file_content):
    get_list_all_cofee(file_content)

    coords = fetch_coordinates(apikey, location)
    longitude, latitude = coords
    first_location = latitude, longitude

    distance_calculation(coffee_list, first_location)

    get_list_nearest_coffees(get_min_distance, list_nearest_coffees)
    make_map(latitude, longitude)


if __name__ == '__main__':
    load_dotenv()
    API = os.getenv('APIKEY')
    apikey = API

    with open("coffee.json", "r", encoding="CP1251") as json_file:
        file_read = json_file.read()
        file_content = json.loads(file_read)

    coffee_list, list_nearest_coffees = [], []

    location = input("Где Вы находитесь? ")
    find_coffees(location, coffee_list, list_nearest_coffees, file_content)

    app = Flask(__name__)
    app.add_url_rule('/', 'map', open_map)
    app.run('0.0.0.0')















