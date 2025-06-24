import json
from collections import defaultdict
from functools import reduce

def groupByContinentAndSumPopulation(groups, element):
    continent, population = element
    if continent not in groups:
        groups[continent] = 0
    groups[continent] += population
    return groups

def groupByContinentAndSumPopulation2(groups, element):
    groups[element[0]] = groups.get(element[0], 0) + element[1]
    return groups

with open("resources/countries.json","r",encoding="utf-8") as f:
    countries = json.load(f)
    continentPopulation = reduce(groupByContinentAndSumPopulation2, map(lambda country : (country["continent"],country["population"]),countries),defaultdict(int))
    print(continentPopulation)
