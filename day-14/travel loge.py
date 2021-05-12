travel_loge=[
  {"country": "France",
   "Visits": 12,
   "cities":["Paris", "Lille", "Dijon"],
  },
  {"country":"Germany",
   "Visits":5,
    "Cities":["Berlin", "Hamburg", "Stuttgart"],
  },
]
def add_new_country(country_visited, times_visited, cities_visited):
  new_country={}
  new_country["country"]=country_visited
  new_country["visits"]=times_visited
  new_country["cities"]=cities_visited
  travel_loge.append(new_country)

add_new_country("Russia", 2, ["Mosco", "Kazan"])
print(travel_loge)