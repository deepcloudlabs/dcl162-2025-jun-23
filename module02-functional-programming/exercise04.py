# generator functions
def filter(predicate_fun,numbers):
    for n in numbers:
        print(f"[for in fun] {n}")
        if predicate_fun(n):
            yield n


def map(map_fun,numbers):
    for n in numbers:
        print(f"[gun] about to yield {n}")
        yield map_fun(n)


lost = [4, 8, 15, 16, 23, 42]

for number in map(lambda u: u ** 3,filter(lambda n: n%2 == 0,numbers=lost)):
    print(f"[for] {number}")

total = sum(map(lambda u: u ** 3,filter(lambda n: n%2 == 0,numbers=lost)))
print(f"total = {total}")

evens = list(filter(lambda n: n%2 == 0,numbers=lost))
cubed = list(map(lambda u: u ** 3,filter(lambda n: n%2 == 0,numbers=lost)))
