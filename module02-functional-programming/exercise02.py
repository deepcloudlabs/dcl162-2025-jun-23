countries = [
    {"code": "tur", "name": "turkey", "continent": "asia", "population": 80000000},
    {"code": "fra", "name": "france", "continent": "europe", "population": 67000000},
    {"code": "ita", "name": "italy", "continent": "europe", "population": 60000000}
]

# total population of European countries

# I. imperative programming: procedural programming
total_population_of_european_countries = 0
for country in countries:  # outer loop
    if country["continent"] == "europe":
        population = country["population"]
        total_population_of_european_countries += population
print(f"total population of European countries is {total_population_of_european_countries}.")


# II. declarative programming: functional programming
#                              1. HoF 2. Pure
#                              Method Chain -> Pipeline
#                              MapReduce Framework: filter, map, reduce, flatten, ...
def is_european(country):
    return country["continent"] == "europe"


def to_population(country):
    return country["population"]


total_population_of_european_countries = sum(map(to_population, filter(is_european, countries)))
print(f"total population of European countries is {total_population_of_european_countries}.")
# if-else -> reducer: partitioning: HoF
# if-elif-elif-*-else -> reducer: grouping: HoF
