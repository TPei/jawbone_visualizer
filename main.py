__author__ = 'TPei'
import csv
import datetime


def handle_data():
    column_names = ['start_date', 'end_date', 'total_sleep_time', 'total_sleep_val', 'light_sleep_time',
                    'light_sleep_val', 'light_sleep_percent', 'sound_sleep_time', 'sound_sleep_val',
                    'sound_sleep_percent', 'wake_time', 'wake_val', 'wake_percent', 'graphic']

    # parse csv
    with open('res/sleep.csv', newline='') as csvfile:
        sleep_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        print(column_names)

        for row in sleep_reader:
            # parse all time strings to datetimes / timedeltas
            row[0] = parse_date(row[0])
            row[1] = parse_date(row[1])
            row[2] = parse_hm_time(row[2])
            row[4] = parse_hm_time(row[4])
            row[7] = parse_hm_time(row[7])
            row[10] = parse_hm_time(row[10])
            print(row)


def parse_date(date):
    # used to get month no
    # '' at beginning of list so that month count starts at 1
    months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # split by whitespace
    date = date.split()

    # get hour from hh:mm[AM/PM] substring
    hour = int(date[4][0:2])

    # convert to 24h format
    if hour == 12:
        if date[4][5:7] == 'AM':
            hour = 0
    elif date[4][5:7] == 'PM':
        hour += 12

    # create datetime object
    date_time = datetime.datetime(int(date[2]), months.index(date[0]), int(date[1][:-1]), hour, int(date[4][3:5]))

    return date_time


def parse_hm_time(hm_string):
    hm = hm_string.split()
    if len(hm) == 1:
        return datetime.timedelta(minutes=int(hm[0][:-1]))
    return datetime.timedelta(hours=int(hm[0][:-1]), minutes=int(hm[1][:-1]))


# quick and dirty unittest for myself
def test_parse_date():
    date = 'December 06, 2014 at 12:17AM'
    assert parse_date(date) == datetime.datetime(2014, 12, 6, 00, 17)

    date = 'December 06, 2014 at 12:17PM'
    assert parse_date(date) == datetime.datetime(2014, 12, 6, 12, 17)

    date = 'December 06, 2014 at 01:17PM'
    assert parse_date(date) == datetime.datetime(2014, 12, 6, 13, 17)

if __name__ == '__main__':
    handle_data()