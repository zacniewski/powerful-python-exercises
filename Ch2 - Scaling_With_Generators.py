# Iteration with iter()
print("Powerful Python has just started!")

numbers = [7 , 4 , 11 , 3]
numbers_iter = iter(numbers)

print(f"{list(numbers_iter)=}")

print(f"{id(numbers)=}")

print(f"{id(numbers_iter)=}")

print(f"{numbers.__iter__=}")

print(f"{numbers_iter.__iter__=}")

names = ["Tom", "Shelly", "Garth"]
names_iter = iter(names)
print(f"{next(names_iter)=}")

print(f"{next(names_iter)=}")

print(f"Squares numbers with generator")


def gen_squares(max_num: int):
    for num in range(max_num):
        yield num ** 2


MAX = 50
for square in gen_squares(MAX):
    print(f"{square=}")
