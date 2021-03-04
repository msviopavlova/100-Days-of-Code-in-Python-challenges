travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

#challenge solved
#created a function that appends another dictionary to a list allowing to
#dynamically pass their names to it.

def add_new_country(country, visits, cities):
    empty_dict = {}
    empty_dict["country"] = country
    empty_dict["visits"] = visits
    empty_dict["cities"] = cities
    travel_log.append(empty_dict)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

#custom test
add_new_country("Thailand", 15, ["Bangkok","Pattaya","Phuket"])
print(travel_log)