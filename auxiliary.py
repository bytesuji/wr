# -*- coding: utf-8 -*-
import os
import sys
import colorama
from colorama import Fore
os.chdir('/opt/wr')
import joblib

colorama.init()


API_URL_COORD = \
    'http://api.openweathermap.org/data/2.5/forecast/daily?lat={}&lon={}&cnt=10&\
    APPID=a42e83259c77ea994ccc6891cdf13525'
API_URL_ZIP = \
    'http://api.openweathermap.org/data/2.5/forecast/daily?zip={},us&APPID=a42e83259c77ea994ccc6891cdf13525'
API_URL_HOURLY_ZIP = \
    'http://api.openweathermap.org/data/2.5/forecast?zip={},us&APPID=a42e83259c77ea994ccc6891cdf13525'
API_URL_HOURLY_COORD = \
    'http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&APPID=a42e83259c77ea994ccc6891cdf13525'


def convert_kelvin(temp, to='C', rounding=1):
    to = to.lower()
    assert to in ('f', 'c')

    if to == 'c':
        t = temp - 273.15
    else:
        t = (temp * 9/5) - 459.67
    return round(t, rounding)

def temp_colorizer(temp, units='C'):
    units = units.lower()
    assert units in ('f', 'c')
    if units != 'f':
        f_temp = (temp * 9/5) + 32
    else:
        f_temp = temp

    if f_temp < 0:
        color_string = Fore.BLUE + '{}' + Fore.RESET
    elif f_temp >= 0 and f_temp < 25:
        color_string = Fore.CYAN + '{}' + Fore.RESET
    elif f_temp >= 25 and f_temp < 50:
        color_string = Fore.GREEN + '{}' + Fore.RESET
    elif f_temp >= 50 and f_temp < 75:
        color_string = Fore.YELLOW + '{}' + Fore.RESET
    elif f_temp >= 75:
        color_string = Fore.RED + '{}' + Fore.RESET

    return color_string.format(temp)


def date_indexer(day_num):
    # returns strigns which are all the same width
    day_names = [
        "Monday     │",
        "Tuesday    │",
        "Wednesday  │",
        "Thursday   │",
        "Friday     │",
        "Saturday   │",
        "Sunday     │"
    ]
    return day_names[day_num]


def handle_loc_type():
    homedir = os.path.expanduser('~')
    wrrc = homedir + '/.wrrc'

    if '--coords' in sys.argv:
        (lat, lon) = (sys.argv[sys.argv.index('--coords') + 1], sys.argv[sys.argv.index('--coords') + 2])
        api_url = API_URL_COORD.format(lat, lon)
    elif '--zip' in sys.argv:
        zipcode = sys.argv[sys.argv.index('--zip') + 1]
        api_url = API_URL_ZIP.format(zipcode)
    elif os.path.exists(wrrc):
        api_url = joblib.load(wrrc)
    else:
        print("Error: User must specify either --zip or --coords!")
        exit(-1)
    if '--save' in sys.argv:
        joblib.dump(api_url, wrrc)

    return api_url


