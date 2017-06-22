import colorama
from colorama import Fore
colorama.init()

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
        f_temp = int((temp * 9/5) + 32)
    else:
        f_temp = temp

    if f_temp < 0:
        color_string = Fore.BLUE + '{}' + Fore.RESET
    elif f_temp in range(0, 25):
        color_string = Fore.CYAN + '{}' + Fore.RESET
    elif f_temp in range(25, 50):
        color_string = Fore.GREEN + '{}' + Fore.RESET
    elif f_temp in range(50, 75):
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
