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

colorama.init()


def default():
    api_url = handle_loc_type()
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


def hourly():
    pass        


def main():
    if '--help' in sys.argv:
        print("""
-f            displays temps in fahrenheit
--today       displays the three-hourly forecast for the day
--zip         specifiy location with ZIP code
--coords      or with lat/lon
--save        saves the location and forecast type specified so you don't have to enter it again
--show-loc    shows the name of the city along with the weather report
        """)
        exit(0)
    if '--hourly' in sys.argv:
        hourly()
    else:
        default()



if __name__ == '__main__':
    main()
