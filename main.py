__author__ = 'TPei'
import csv
import datetime
from date_parser import *
from csv_parser import *
from plotter import *
import json
from pprint import pprint


def to_hours(seconds):
    return seconds / 60 / 60


def plot_from_csv():
    sleep_data = parse_csv()
    total_times = []
    deep_times = []
    light_times = []
    awake_times = []
    labels = []
    for row in sleep_data:
        # currently I am converting to number of seconds for plotting
        total_times.append(to_hours((row[1] - row[0]).total_seconds()))
        deep_times.append(to_hours((row[4]).total_seconds()))
        light_times.append(to_hours((row[7]).total_seconds()))
        awake_times.append(to_hours((row[10]).total_seconds()))

        # label is month/day
        labels.append(str(row[1].month) + "/" + str(row[1].day))

    #plot_bar_chart(total_times, deep_times, light_times, awake_times, labels)
    plot_line_graph(total_times, total_times, deep_times, light_times, awake_times, labels)


def plot_from_json():
    json_data = open('res/sleep.json')
    data = json.load(json_data)
    items = data['data']['items']

    time_in_bed = []
    total_sleep = []
    deep_times = []
    light_times = []
    awake_times = []
    labels = []

    for item in items:
        labels.append(item['time_completed'])
        item = item['details']
        time_in_bed.append(to_hours(item['duration']))

        sound = to_hours(item['sound'])
        light = to_hours(item['light'])
        total_sleep.append(sound + light)
        deep_times.append(sound)
        light_times.append(light)
        awake_times.append(to_hours(item['awake']))


    # json data is from now -> past, dirty array reverse here
    #plot_line_graph(time_in_bed[::-1], total_sleep[::-1], deep_times[::-1], light_times[::-1], awake_times[::-1])
    composite_line_bar(time_in_bed[::-1], total_sleep[::-1], deep_times[::-1], light_times[::-1], awake_times[::-1])
    #plot_bar_chart(total_sleep, deep_times, light_times, awake_times, labels)
    json_data.close()

if __name__ == '__main__':
    #plot_from_csv()
    plot_from_json()