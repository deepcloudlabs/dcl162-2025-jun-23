# generator functions are lazy
def filter(predicate_fun,numbers):
    for n in numbers:
        print(f"[for in fun] {n}")
        if predicate_fun(n):
            yield n


def map(map_fun,numbers):
    for n in numbers:
        print(f"[gun] about to yield {n}")
        yield map_fun(n)

print("app has been started.")
lost = [4, 8, 15, 16, 23, 42]

result = map(lambda u: u ** 3,filter(lambda n: n%2 == 0,numbers=lost))
print("app has been done.")
total = sum(result) # sum is a special reduce function



