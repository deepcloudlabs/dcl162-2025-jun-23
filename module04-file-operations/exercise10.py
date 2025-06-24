import csv

with open("countries.csv", "rt", newline="") as file:
    reader = csv.reader(file)
    for code,name,continent,population in reader:
        print(type(code), type(name), type(continent), type(population))
        print(f"{code},{name},{continent},{population}")