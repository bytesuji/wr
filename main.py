import json
import datetime
from urllib.request import urlopen
from auxiliary import *

# API_URL = \
#     'http://api.openweathermap.org/data/2.5/forecast/daily?zip=02635,us&APPID=a42e83259c77ea994ccc6891cdf13525'
API_URL = \
    'http://api.openweathermap.org/data/2.5/forecast/daily?lat=61&lon=149&APPID=a42e83259c77ea994ccc6891cdf13525'


def main():
    json_str = urlopen(API_URL).read()
    json_dict = json.loads(json_str)
    weekday = datetime.datetime.today().weekday()

    expl_string = "Weekday    │ Temp  │ Info"
    print()
    print(expl_string)
    for i, day in zip(range(7), json_dict['list']):
        k_temp = float(day['temp']['day'])
        conv_temp = convert_kelvin(k_temp)
            
        description = day['weather'][0]['description']
        description = description[0].upper() + description[1:]

        temp_string = temp_colorizer(conv_temp) + "°" + (' ' * (5 - len(str(conv_temp)))) + '│ '

        print('─' * 11, '┼', '─' * 7, '┼', '─' * 17, sep='')
        print(date_indexer((weekday + i) % 6), temp_string + description)
    print('─' * 11, '┴', '─' * 7, '┴', '─' * 17, sep='')
    print()


if __name__ == '__main__':
    main()
#(temp_colorizer(conv_temp) + "° │ ") 
