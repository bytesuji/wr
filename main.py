#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import datetime
import colorama 
from colorama import Style
from urllib.request import urlopen

os.chdir('/opt/wr')
import joblib
from auxiliary import *

API_URL_COORD = \
    'http://api.openweathermap.org/data/2.5/forecast/daily?lat={}&lon={}&cnt=10&\
    APPID=a42e83259c77ea994ccc6891cdf13525'
API_URL_ZIP = \
    'http://api.openweathermap.org/data/2.5/forecast/daily?zip={},us&APPID=a42e83259c77ea994ccc6891cdf13525'

colorama.init()


def main():
    homedir = os.path.expanduser('~')
    wrrc = homedir + '/.wrrc'
    if '--coords' in sys.argv:
        (lat, lon) = (sys.argv[sys.argv.index('--coords') + 1], sys.argv[sys.argv.index('--coords') + 2])
        api_url = API_URL_COORD.format(lat, lon)

        if '--save-loc' in sys.argv:
            joblib.dump(api_url, wrrc)
    elif '--zip' in sys.argv:
        zipcode = sys.argv[sys.argv.index('--zip') + 1]
        api_url = API_URL_ZIP.format(zipcode)

        if '--save-loc' in sys.argv:
            joblib.dump(api_url, wrrc)
    elif os.path.exists(wrrc):
        api_url = joblib.load(wrrc)
    else:
        print("Error: User must specify either --zip or --coords!")
        exit(-1)

    json_str = urlopen(api_url).read().decode()
    json_dict = json.loads(json_str)
    weekday = datetime.datetime.today().weekday()

    expl_string = Style.BRIGHT + "Weekday" + Style.RESET_ALL + "    │ " + Style.BRIGHT + \
        "Temp" + Style.RESET_ALL + "  │ " + Style.BRIGHT + "Info" + Style.RESET_ALL

    print()
    if '--show-loc' in sys.argv:
        print(Style.BRIGHT + json_dict['city']['name'] + Style.RESET_ALL + '\n')
    print(expl_string)
    for i, day in zip(range(7), json_dict['list']):
        k_temp = float(day['temp']['day'])
        if '-f' in sys.argv:
            conv_temp = convert_kelvin(k_temp, 'f')
        else:
            conv_temp = convert_kelvin(k_temp)
            
        description = day['weather'][0]['description']
        description = description[0].upper() + description[1:]

        if '-f' in sys.argv:
            temp_string = temp_colorizer(conv_temp, 'f') + "°" + (' ' * (5 - len(str(conv_temp)))) + '│ '
        else:
            temp_string = temp_colorizer(conv_temp) + "°" + (' ' * (5 - len(str(conv_temp)))) + '│ '
        # TODO fix that redundancy

        print('─' * 11, '┼', '─' * 7, '┼', '─' * 23, sep='')
        print(date_indexer((weekday + i) % 6), temp_string + description)
    print()


if __name__ == '__main__':
    main()
