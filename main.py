__author__ = 'TPei'
import csv
import datetime
from date_parser import *
from csv_parser import *
from plotter import *
import json
from pprint import pprint


def plot_from_csv():
    sleep_data = parse_csv()
    total_times = []
    deep_times = []
    light_times = []
    awake_times = []
    labels = []
    for row in sleep_data:
        # currently I am converting to number of seconds for plotting
        total_times.append((row[1] - row[0]).total_seconds())
        deep_times.append((row[4]).total_seconds())
        light_times.append((row[7]).total_seconds())
        awake_times.append((row[10]).total_seconds())

        # label is month/day
        labels.append(str(row[1].month) + "/" + str(row[1].day))

    #plot_bar_chart(total_times, deep_times, light_times, awake_times, labels)
    plot_line_graph(total_times, deep_times, light_times, awake_times, labels)


def plot_from_json():
    json_data = open('res/sleep.json')
    data = json.load(json_data)
    items = data['data']['items']

    total_times = []
    deep_times = []
    light_times = []
    awake_times = []
    labels = []

    for item in items:
        labels.append(item['time_completed'])
        item = item['details']
        total_times.append(item['duration'])
        deep_times.append(item['sound'])
        light_times.append(item['light'])
        awake_times.append(item['awake'])

    plot_line_graph(total_times, deep_times, light_times, awake_times)
    #plot_bar_chart(total_times, deep_times, light_times, awake_times, labels)
    json_data.close()

if __name__ == '__main__':
    #plot_from_csv()
    plot_from_json()