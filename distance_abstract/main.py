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
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    lat1 = get_lat(city1)
    lon1 = get_lon(city1)
    lat2 = get_lat(city2)
    lon2 = get_lon(city2)

    distance_final = sqrt(((lat1 - lat2) ** 2) + ((lon1 - lon2) ** 2))

    return distance_final
