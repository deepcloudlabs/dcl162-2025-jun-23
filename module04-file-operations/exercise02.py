# text i/o + read
with open("countries.txt", "rt") as countries:
    for line in countries:
        code,name,continent,population = line.strip().split(",")
        print(type(code), type(name), type(continent), type(population))
        print(f"{code},{name},{continent},{population}")