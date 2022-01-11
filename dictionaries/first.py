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



def add_new_countr(country, amount_visits, list_of_cities):
    travel_log.append({"country": country, "visits": amount_visits, "cities": list_of_cities})
    print(travel_log)


add_new_countr("Russia", 2, ["Moscow", "Saint Peters", "Sochi"])