import json
import datetime
from urllib.request import urlopen
from auxiliary import *

API_URL = \
    'http://api.openweathermap.org/data/2.5/forecast/daily?zip=02635,us&APPID=a42e83259c77ea994ccc6891cdf13525'


def main():
    json_str = urlopen(API_URL).read()
    json_dict = json.loads(json_str)

    for i, day in zip(range(7), json_dict['list']):
        k_temp = float(day['temp']['day'])
        c_temp = convert_kelvin(k_temp)
        print(date_indexer(i), c_temp)


if __name__ == '__main__':
    main()
