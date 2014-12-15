__author__ = 'TPei'
import csv
import datetime
from date_parser import *
from csv_parser import *
from plotter import *
import json
from pprint import pprint
from helper import *

def get_all_the_data(time_type="asleep_time"):
    d = {}

    json_data = open('res/sleep.json')
    data = json.load(json_data)
    items = data['data']['items']

    for item in items:
        date = ''
        if time_type == 'awake_time':
            date = item['date']
        item = item['details']

        # if we want the sleep data for the day we go to bet
        # like coffe on monday, how does that affect the following night
        # we have to get the asleep_time timestamp and get the date_string from there
        if time_type == 'asleep_time':
            date = to_datetime(item[time_type])

            day = date.day
            if date.hour < 10:
                day -= 1
            day = "{0:0=2d}".format(day)

            date = int(str(date.year) + str(date.month) + str(day))

        d[date] = {'date': date}

        d[date]['bed'] = to_hours(item['duration'])

        # put all sleep data for one night into a single dictionary
        sound = to_hours(item['sound'])
        light = to_hours(item['light'])

        d[date]['sleep'] = sound + light

        d[date]['sound'] = sound
        d[date]['light'] = light
        d[date]['awake'] = to_hours(item['awake'])

    json_data = open('res/meals.json')
    data = json.load(json_data)
    items = data['data']['items']

    for item in items:
        if item['title'] == "Coffee":
            key = item['date']

            if key in d:
                if 'coffee' in d[key]:
                    d[key]['coffee'] += 1
                else:
                    d[key]['coffee'] = 1


    json_data = open('res/moves.json')
    data = json.load(json_data)
    items = data['data']['items']
    for item in items:
        key = item['date']
        if key in d:
            if 'steps' in d[key]:
                d[key]['steps'] += item['details']['steps']
            else:
                d[key]['steps'] = item['details']['steps']

    return d