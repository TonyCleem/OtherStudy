import os
import time
import datetime
import json

import requests


class Event():

  def __init__(self, serialized_event=None):
    serialized_event = serialized_event or {}
    self.id = serialized_event.get('id', '')
    self.department = serialized_event.get('department', '')
    self.phenomenon_time = serialized_event.get('phenomenon_time', '')
    self.phenomenon_dates = serialized_event.get('phenomenon_dates', '')
    self.phenomenon_area = serialized_event.get('phenomenon_area', '')
    self.phenomenon_description = serialized_event.get(
        'phenomenon_description', '')

  def get_date(self):
    return self.phenomenon_dates

  def get_time(self):
    return self.phenomenon_time

  def get_area(self):
    return self.phenomenon_area

  def get_phenomenon(self):
    return self.phenomenon_description

  def __str__(self):
    return f'Регион: {self.department} Погода: {self.phenomenon_description}'


def get_new_event(token, town_title):
  params = {'department': town_title}
  headers = {'token': token}
  endpoint = 'https://d5dsaolj35tv1tdu7fmd.apigw.yandexcloud.net/weather/check'
  response = requests.get(endpoint, params=params, headers=headers)
  if not response.ok:
    return Event()
  return Event(response.json())


def render_progressbar(total,
                       iteration,
                       prefix='',
                       suffix='',
                       length=30,
                       fill='█',
                       zfill='░'):
  iteration = min(total, iteration)
  percent = "{0:.1f}"
  percent = percent.format(100 * (iteration / float(total)))
  filled_length = int(length * iteration // total)
  pbar = fill * filled_length + zfill * (length - filled_length)
  return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


class SMSServer():

  def __init__(self, token):
    self._check_token(token)
    self.token = token

  def _check_token(self, token):
    headers = {'token': token}
    endpoint = 'https://d5dsaolj35tv1tdu7fmd.apigw.yandexcloud.net/sms/check_token'
    response = requests.get(endpoint, headers=headers)
    return True

  def send(self, message):
    receivers = 3249
    print(f'Рассылаю сообщение:\n {message}')
    for i in range(receivers):
      print(render_progressbar(receivers, i), end='')
      print('	\u001b[45D', end='')
      if not i % 100:
        time.sleep(0.1)
