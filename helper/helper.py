__author__ = 'TPei'
from helper.date_parser import *

def to_hours(seconds):
    return seconds / 60 / 60


def get_weekday(unixtimestamp):
    # if bedtime is before 10 am, it's probably
    # from the day before
    time = to_datetime(unixtimestamp)
    if time.hour < 10:
        return time.weekday() - 1
    return time.weekday()


def to_datetime(unixtimestamp):
    return datetime.datetime.fromtimestamp(
        int(str(unixtimestamp))
    )

def compareDicts(dict1, dict2):
    for key in dict1:
        try:
            print(dict1[key])
            print(dict2[key])
        except KeyError:
            print("{}")


def averages(values, counter):
    average = []
    if len(values) != len(counter):
        raise Exception("lists must be of equal lengths")
    else:
        for i in range(0, len(values)):
            if counter[i] == 0:
                average.append = 0
            else:
                average.append(values[i] / float(counter[i]))

    return average