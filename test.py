import json
from urllib.request import urlopen

API_EXAMPLE_URL = \
    'http://api.openweathermap.org/data/2.5/weather?zip=02635,us&APPID=a42e83259c77ea994ccc6891cdf13525'
url_obj = urlopen(API_EXAMPLE_URL)
api_str = url_obj.read()
api_dict = json.loads(api_str)

print(api_dict['name'])
