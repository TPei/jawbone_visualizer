__author__ = 'TPei'
import datetime


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