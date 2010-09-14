import random

# categories
# 0 - decimal number comparisons
# 0a - uneven decimal comparisons
# 1 - positive numbers
# 1a - addition and subtraction
# 1b - multiplication and devision
# 1c - order and brackets
# 2 - negative numbers
# 2a - addition and subtraction
# 2b - multiplication and devision
# 2c - repeated negative multiplication
# 3 - si units
# 3a - multiplication and devision by powers of 10
# 3b - converting between si magnitude regardless of base
# 3c - comparison of different magnitude si units
# 4 - rounding
# 4a - rounding to whole numbers
# 4b - rounding to d.p.
# 4c - rounding to s.f.

categories = []
category_generators = {}
category_descriptions = {}


def _add_category(name, description):
    categories.append(name)
    def decorator(func):
        category_generators[name] = func
        category_descriptions[name] = description
        return func
    return decorator


def generate_question(category):
    return category_generators[category]()


def describe_category(category):
    return category_descriptions[category]


@_add_category("0", "Decimal comparison")
def category_0():
    a = random.randint(0, 1000)/100
    b = random.randrange(0, 1000)/100 
    while b == a:
        b = random.randrange(0, 1000)/100 
    goal = random.choice(["bigger", "smaller"])
    answer = bool(a > b) ^ bool(goal == "smaller")
    return "Which is {0} a) {1:.2f} or b) {2:.2f}?".format(goal, a, b,), "a" if answer else "b"


@_add_category("0a", "Decimal comparison")
def category_0():
    a = random.randint(0, 1000)/100
    b = random.randrange(0, 1000)/100 
    while b == a:
        b = random.randrange(0, 1000)/100 
    goal = random.choice(["bigger", "smaller"])
    answer = bool(a > b) ^ bool(goal == "smaller")
    return "Which is {0} a) {1} or b) {2}?".format(goal, a, b,), "a" if answer else "b"


if __name__ == "__main__":
    for i in range(10):
        print(generate_question("0"))
