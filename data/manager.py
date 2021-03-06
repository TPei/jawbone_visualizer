__author__ = 'TPei'
import json

from helper.csv_parser import *
from plotting.plotter import *
from data.DataHandler import get_all_the_data
from helper.helper import *


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


def plot_sleep(data):

    import collections

    od = collections.OrderedDict(sorted(data.items()))

    time_in_bed = []
    total_sleep = []
    deep_times = []
    light_times = []
    awake_times = []
    labels = []
    timestamps = []

    for day in od:
        sound = od[day]['sound']
        light = od[day]['light']
        total_sleep.append(sound + light)
        deep_times.append(sound)
        light_times.append(light)
        time_in_bed.append(od[day]['bed'])
        awake_times.append(od[day]['awake'])


    # json data is from now -> past, dirty array reverse here
    #plot_line_graph(time_in_bed[::-1], total_sleep[::-1], deep_times[::-1], light_times[::-1], awake_times[::-1])
    composite_line_bar(time_in_bed, total_sleep, deep_times, light_times, awake_times)
    #plot_bar_chart(total_sleep, deep_times, light_times, awake_times, labels)


def coffee_per_weekday(data):
    added_times = [0, 0, 0, 0, 0, 0, 0]
    average_times_counter = [0, 0, 0, 0, 0, 0, 0]
    for date in data:

        d = str(data[date]['date'])
        day = datetime.datetime(int(d[0:4]), int(d[4:6]), int(d[6:8]))
        weekday = day.weekday()

        if 'coffee' in data[date]:
            coffee = data[date]['coffee']
        else:
            coffee = 0

        added_times[weekday] += coffee
        average_times_counter[weekday] += 1

    average_times = averages(added_times, average_times_counter)

    return average_times, average_times_counter


def weekday_list():
    json_data = open('res/sleep.json')
    data = json.load(json_data)
    items = data['data']['items']

    total_amount = []

    for item in items:
        item = item['details']

        sound = to_hours(item['sound'])
        light = to_hours(item['light'])
        total_amount.append([item['asleep_time'], sound + light])


    added_times = [0, 0, 0, 0, 0, 0, 0]
    average_times_counter = [0, 0, 0, 0, 0, 0, 0]

    for entry in total_amount:
        entry[0] = get_weekday(entry[0])
        added_times[entry[0]] += entry[1]
        average_times_counter[entry[0]] += 1

    average_times = averages(added_times, average_times_counter)

    '''
    print(total_sleep)
    print(added_times)
    print(average_times_counter)
    print(average_times)
    '''

    return average_times, average_times_counter


def visualize_sleep_per_weekday():
    sleeps, counter = weekday_list()
    days = ['Mon -\nTue', 'Tue -\nWed', 'Wed -\nThu', 'Thu -\nFri', 'Fri -\nSat', 'Sat -\nSun', 'Sun -\n Mon']

    # move night Sunday - Monday to front
    sleeps.insert(0, sleeps.pop())
    days.insert(0, days.pop())

    # make weeknights red and weekend nights blue
    colors = ['#FF4D4D', '#FF4D4D', '#FF4D4D', '#FF4D4D', '#FF4D4D', '#0066CC', '#0066CC']
    plot_sleep_per_weekday('Average sleep per weeknight', 'Sleep in hours', days, sleeps, counter, colors)


def visualize_coffee_per_weekday():
    coffees, counter = coffee_per_weekday(get_all_the_data())
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    # make weeknights red and weekend nights blue
    colors = ['#FF4D4D', '#FF4D4D', '#FF4D4D', '#FF4D4D', '#FF4D4D', '#0066CC', '#0066CC']
    plot_coffee_per_weekday('Average Coffee per weekday', 'Cups of coffee', days, coffees, counter, colors)


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


def step_sleep_total():
    json_data = open('res/moves.json')
    data = json.load(json_data)
    items = data['data']['items']
    steps = []
    for item in items:
        steps.append(item['details']['steps'])

    json_data.close()
    json_data = open('res/sleep.json')
    data = json.load(json_data)
    items = data['data']['items']

    total_sleep = []

    for item in items:
        item = item['details']

        sound = to_hours(item['sound'])
        light = to_hours(item['light'])
        total_sleep.append(sound + light)

    # reverse
    total_steps_sleep_line(steps[::-1], total_sleep[::-1])


if __name__ == '__main__':
    visualize_sleep_per_weekday()
    #plot_sleep()
    #plot_step_graph()
    plot_all(get_all_the_data())
    #print(get_all_the_data('awake_time'))
    #compareDicts(get_all_the_data(), get_all_the_data('awake_time'))
    #coffee_effect_sleep(get_all_the_data())
