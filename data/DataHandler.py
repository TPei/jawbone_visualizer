__author__ = 'TPei'
import json

from helper.helper import *


class DataHandler:

    def __init__(self, time_type="asleep_time"):
        """
        parse json files (meals, sleep, moves) and put
        all data into an embedded dict
        :param time_type:
        :return:
        """
        self.d = {}

        json_data = open('../res/sleep.json')
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

            self.d[date] = {'date': date}

            self.d[date]['bed'] = to_hours(item['duration'])

            # put all sleep data for one night into a single dictionary
            sound = to_hours(item['sound'])
            light = to_hours(item['light'])

            self.d[date]['sleep'] = sound + light

            self.d[date]['sound'] = sound
            self.d[date]['light'] = light
            self.d[date]['awake'] = to_hours(item['awake'])

        json_data = open('../res/meals.json')
        data = json.load(json_data)
        items = data['data']['items']

        for item in items:
            if item['title'] == "Coffee":
                key = item['date']

                if key in self.d:
                    if 'coffee' in self.d[key]:
                        self.d[key]['coffee'] += 1
                    else:
                        self.d[key]['coffee'] = 1


        json_data = open('../res/moves.json')
        data = json.load(json_data)
        items = data['data']['items']
        for item in items:
            key = item['date']
            if key in self.d:
                if 'steps' in self.d[key]:
                    self.d[key]['steps'] += item['details']['steps']
                else:
                    self.d[key]['steps'] = item['details']['steps']

    def get_all(self):
        """
        returns dict containing all data
        return: {date: {steps: 11234, sleep: 5.9, coffee: 2, ...}, ...}
        """
        return self.d

    def get_by_category(self, category_name):
        """
        category can be 'sleep', 'light, 'awake', 'sound', 'bed', 'steps' or 'coffee'
        """
        category = {}
        for day in self.d:
            if category_name not in self.d[day]:
                category[day] = 0
            else:
                category[day] = self.d[day][category_name]
        return category


def get_all_the_data(time_type="asleep_time"):
    """
    parse json files (meals, sleep, moves) and put
    all data into an embedded dict
    :param time_type:
    :return: {date: {steps: 1234, sleep: 1235, coffee: 2, ...}, ...}
    """
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
                year, month, day = decrease_day(date.year, date.month, day)
            else:
                year = date.year
                month = date.month
            day = "{0:0=2d}".format(day)
            month = "{0:0=2d}".format(int(month))

            date = int(str(year) + str(month) + str(day))

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
    for i in d:
        print(d[i])
    return d


def decrease_day(year, month, day):
    if day > 1:
        return year, month, day - 1
    from calendar import monthrange
    month = month - 1
    if month == 0:
        year -= 1
        month = 12
    return year, month, monthrange(year, month)[1]


if __name__ == '__main__':
    handler = DataHandler()
    print(handler.get_by_category('coffee'))