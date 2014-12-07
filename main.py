__author__ = 'TPei'
import csv
import datetime
from date_parser import *
from plotter import *

def handle_data():
    column_names = ['start_date', 'end_date', 'total_sleep_time', 'total_sleep_val', 'light_sleep_time',
                    'light_sleep_val', 'light_sleep_percent', 'sound_sleep_time', 'sound_sleep_val',
                    'sound_sleep_percent', 'wake_time', 'wake_val', 'wake_percent', 'graphic']

    # parse csv
    with open('res/sleep.csv', newline='') as csvfile:
        sleep_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        #print(column_names)
        sleep_data = []
        for row in sleep_reader:
            # parse all time strings to datetimes / timedeltas
            row[0] = parse_date(row[0])
            row[1] = parse_date(row[1])
            row[2] = parse_hm_time(row[2])
            row[4] = parse_hm_time(row[4])
            row[7] = parse_hm_time(row[7])
            row[10] = parse_hm_time(row[10])
            sleep_data.append(row)
    return sleep_data


# quick and dirty unittest for myself
def test_parse_date():
    date = 'December 06, 2014 at 12:17AM'
    assert parse_date(date) == datetime.datetime(2014, 12, 6, 00, 17)

    date = 'December 06, 2014 at 12:17PM'
    assert parse_date(date) == datetime.datetime(2014, 12, 6, 12, 17)

    date = 'December 06, 2014 at 01:17PM'
    assert parse_date(date) == datetime.datetime(2014, 12, 6, 13, 17)

if __name__ == '__main__':
    sleep_data = handle_data()
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

    plot_bar_chart(total_times, deep_times, light_times, awake_times, labels)