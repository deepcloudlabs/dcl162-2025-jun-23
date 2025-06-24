import json

with open("countries.json", "rt") as file:
    countries = json.load(file)
    for country in countries:
        print(type(country["population"]))
        print(country)