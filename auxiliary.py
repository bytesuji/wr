def convert_kelvin(temp, to='C', rounding=1):
    to = to.lower()
    assert to in ('f', 'c')

    if to == 'c':
        t = temp - 273.15
    else:
        t = (temp * 9/5) - 459.67
    return round(t, rounding)


def date_indexer(day_num):
    # returns strigns which are all the same width
    day_names = [
        "Monday     ",
        "Tuesday    ",
        "Wednesday  ",
        "Thursday   ",
        "Friday     ",
        "Saturday   ",
        "Sunday     "
    ]
    return day_names[day_num]
