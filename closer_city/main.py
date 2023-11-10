from math import sqrt


def make_city(name, lat, lon):
    return [name, lat, lon]


def get_name(city):
    return city[0]


def get_lat(city):
    return city[1]


def get_lon(city):
    return city[2]


def distance(city1, city2):
    lat1 = get_lat(city1)
    lon1 = get_lon(city1)
    lat2 = get_lat(city2)
    lon2 = get_lon(city2)

    distance_final = sqrt(((lat1 - lat2) ** 2) + ((lon1 - lon2) ** 2))

    return distance_final


def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """

    distance_to_city1 = distance(city1, make_city('', lat, lon))
    distance_to_city2 = distance(city2, make_city('', lat, lon))

    if distance_to_city1 < distance_to_city2:
        return get_name(city1)
    else:
        return get_name(city2)
