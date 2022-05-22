# Iteration with iter()
print("Powerful Python has just started!")

numbers = [7, 4, 11, 3]
numbers_iter = iter(numbers)

# Checking __iter__ magic method
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


def lines_from_file (path):
    with open(path) as handle:
        for line in handle:
            yield line.rstrip('\n')


def matching_lines(lines, pattern):
    for line in lines:
        if pattern in line:
            yield line


lines = lines_from_file('poem.txt')
matching = matching_lines(lines, 'with')
for line in matching:
    print(line)


def house_records():
    pass
