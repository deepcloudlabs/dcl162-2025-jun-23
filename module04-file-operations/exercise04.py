import pickle

countries = [
    ("tur", "turkey", "asia", 80000000.0),
    ("fra", "france", "europe", 67000000),
    ("ita", "italy", "europe", 60000000)
]

# binary i/o + read
with open("countries.pkl", "rb") as f:
    countries = pickle.load(f)
    for code,name,continent,population in countries:
        print(type(code), type(name), type(continent), type(population))
        print(f"{code},{name},{continent},{population}")