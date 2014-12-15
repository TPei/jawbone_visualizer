__author__ = 'TPei'
import csv
import datetime
from date_parser import *
from csv_parser import *
from plotter import *
import json
from pprint import pprint
from helper import *
from data_handler import get_all_the_data

def plot_sleep_from_csv():
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


def plot_sleep():
    json_data = open('res/sleep.json')
    data = json.load(json_data)
    items = data['data']['items']

    time_in_bed = []
    total_sleep = []
    deep_times = []
    light_times = []
    awake_times = []
    labels = []
    timestamps = []

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
        date = to_datetime(item['asleep_time'])

        day = date.day
        if date.hour < 10:
            day -= 1

        timestamps.append(int(str(date.year) + str(date.month) + str(day)))

    print(timestamps)

    # json data is from now -> past, dirty array reverse here
    #plot_line_graph(time_in_bed[::-1], total_sleep[::-1], deep_times[::-1], light_times[::-1], awake_times[::-1])
    composite_line_bar(time_in_bed[::-1], total_sleep[::-1], deep_times[::-1], light_times[::-1], awake_times[::-1])
    #plot_bar_chart(total_sleep, deep_times, light_times, awake_times, labels)
    json_data.close()


def weekday_list():
    json_data = open('res/sleep.json')
    data = json.load(json_data)
    items = data['data']['items']

    total_sleep = []

    for item in items:
        item = item['details']

        sound = to_hours(item['sound'])
        light = to_hours(item['light'])
        total_sleep.append([item['asleep_time'], sound + light])

    added_times = [0, 0, 0, 0, 0, 0, 0]
    average_times_counter = [0, 0, 0, 0, 0, 0, 0]
    average_times = [0, 0, 0, 0, 0, 0, 0]

    for entry in total_sleep:
        entry[0] = get_weekday(entry[0])
        added_times[entry[0]] += entry[1]
        average_times_counter[entry[0]] += 1

    for i in range(0, len(added_times)):
        average_times[i] = (added_times[i] / float(average_times_counter[i]))

    '''
    print(total_sleep)
    print(added_times)
    print(average_times_counter)
    print(average_times)
    '''

    return average_times


def visualize_sleep_per_weekday():
    plot_bar_chart('Average sleep per weekday', 'Sleep in hours', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], weekday_list())


def coffee_analyzer():
    json_data = open('res/meals.json')
    data = json.load(json_data)
    items = data['data']['items']

    d = {}

    for item in items:
        if item['title'] == "Coffee":
            key = item['date']

            if key in d:
                d[key] += 1
            else:
                d[key] = 1

    return d


def plot_step_graph():
    """
    plots a total steps per day
    vs average over time
    step graph
    """
    json_data = open('res/moves.json')
    data = json.load(json_data)
    items = data['data']['items']
    steps = []
    for item in items:
        steps.append(item['details']['steps'])

    #remove first (latest) step entry (current, not yet finished day)
    steps = steps[1:]
    steps_line(steps[::-1])



if __name__ == '__main__':
    #visualize_sleep_per_weekday()
    #plot_sleep()
    #plot_step_graph()
    #plot_all(get_all_the_data())
    #print(get_all_the_data('awake_time'))
    #compareDicts(get_all_the_data(), get_all_the_data('awake_time'))
    coffee_effect_sleep(get_all_the_data())
