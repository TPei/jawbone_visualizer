__author__ = 'TPei'
import plotly.plotly as py
from plotly.graph_objs import *
from data_handler import get_all_the_data

"""
Working with the plotly api to create more interactive diagrams
"""


def sleep():

    data = get_all_the_data()

    traces = []

    categories = ['bed', 'sleep', 'sound', 'light', 'awake', 'averages']

    sleep_data = [[], [], [], [], [], []]

    for date in data:
        entry = data[date]
        for i in range(0, len(categories)-1):
            sleep_data[i].append(entry[categories[i]])

    total_sleep = 0
    averages = []
    for i in range(0, len(sleep_data[1])):
        total_sleep += sleep_data[1][i]
        averages.append(total_sleep / float(i+1))

    sleep_data[5] = averages


    for i in range(0, len(sleep_data)):
        traces.append(Scatter(y=sleep_data[i], name=categories[i]))

    data = Data(traces)

    unique_url = py.plot(data, filename='sleep')

    '''
    trace0 = Scatter(
        #x=[1, 2, 3, 4],
        y=sleep
    )
    trace1 = Scatter(
        #x=[1, 2, 3, 4],
        y=[16, 5, 11, 9]
    )
    data = Data([trace0, trace1])

    unique_url = py.plot(data, filename = 'basic-line')'''

def coffee_vs_sleep():
    data = get_all_the_data()
    categories = ['0 cups', '1 or 2 cups', '3 or 4 cups', '5+ cups']
    count = [0, 0, 0, 0]
    average_counter = [0, 0, 0, 0]
    average = [0, 0, 0, 0]

    import collections

    od = collections.OrderedDict(sorted(data.items()))

    print(od)

    category = 'sleep'

    for day in od:

        if 'coffee' in od[day] and category in od[day]:
            #coffee.append(od[day]['coffee'])
            if od[day]['coffee'] == 0:
                count[0] += od[day][category]
                average_counter[0] += 1
            elif od[day]['coffee'] < 3:
                count[1] += od[day][category]
                average_counter[1] += 1
            elif od[day]['coffee'] < 5:
                count[2] += od[day][category]
                average_counter[2] += 1
            else:
                count[3] += od[day][category]
                average_counter[3] += 1
        else:
            count[0] += od[day][category]
            average_counter[0] += 1

    #calculate average
    for i in range(0, len(count)):
        if average_counter[i] == 0:
            average[i] = 0
        else:
            average[i] = (count[i] / float(average_counter[i]))

    trace = Bar(y=average, x=categories)

    data = Data([trace])

    unique_url = py.plot(data, filename='coffee_vs_sleep')

if __name__ == '__main__':
    #sleep()
    coffee_vs_sleep()