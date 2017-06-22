import os
import sys
import json
import datetime
from urllib.request import urlopen

import joblib
from auxiliary import *

API_URL_COORD = \
    'http://api.openweathermap.org/data/2.5/forecast/daily?lat={}&lon={}&cnt=10&APPID=a42e83259c77ea994ccc6891cdf13525'
API_URL_ZIP = \
    'http://api.openweathermap.org/data/2.5/forecast/daily?zip={},us&APPID=a42e83259c77ea994ccc6891cdf13525'


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
        raise Exception("User must specify either --coords or --zip")

    json_str = urlopen(api_url).read()
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

        print('─' * 11, '┼', '─' * 7, '┼', '─' * 27, sep='')
        print(date_indexer((weekday + i) % 6), temp_string + description)
    print('─' * 11, '┴', '─' * 7, '┴', '─' * 27, sep='')
    print()


if __name__ == '__main__':
    main()
