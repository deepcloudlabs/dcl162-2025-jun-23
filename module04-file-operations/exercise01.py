countries = [
    ("tur", "turkey", "asia", 80000000.0),
    ("fra", "france", "europe", 67000000),
    ("ita", "italy", "europe", 60000000)
]

# text i/o + write
with open("countries.txt", "wt") as f:
    for code,name,continent,population in countries:
        print(type(code), type(name), type(continent), type(population))
        f.write(f"{code},{name},{continent},{population}\n")