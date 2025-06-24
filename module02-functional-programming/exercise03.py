def fun(numbers):
    evens = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
    return evens

def gun(numbers):
    cubed = []
    for n in numbers:
        cubed.append(n**3)
    return cubed

lost = [4, 8, 15, 16, 23, 42]

total = sum(gun(fun(numbers=lost)))

