import random
from model.questions import Question


categories = []
category_generators = {}
category_descriptions = {}
category_dependancy = {}


def generate_questions(category, number):
    for i in range(number):
        q = category_generators[category]()
        q.guid = "{0}".format(i)
        yield q


def describe_category(category):
    return category_descriptions[category]


def _add_category(name, description, dependancy=[]):
    categories.append(name)
    category_dependancy[name] = dependancy
    def decorator(func):
        category_generators[name] = func
        category_descriptions[name] = description
        return func
    return decorator


@_add_category("0", "Decimal comparison")
def category_0():
    magnitude = random.choice([0.1, 1.0, 10.0, 100.0, 1000.0])
    a = random.randint(0, 1000)
    diff = int(random.triangular(-100, 100, 0))
    while not diff:
        diff = int(random.triangular(-100, 100, 0))
    b = (a - diff)/magnitude
    a = a/magnitude
    goal = random.choice(["bigger", "smaller"])
    answer = bool(a > b) == bool(goal == "bigger")
    return Question("Which is {0}?".format(goal), "0" if answer else "1", "0", "single_choice", [a, b])


@_add_category("0a", "Uneven length decimal comparison", ["0"])
def category_0():
    magnitude = random.choice([0.1, 1.0, 10.0, 100.0, 1000.0])
    a = random.randint(0, 1000)
    diff = int(random.triangular(-100, 100, 0))
    while not diff:
        diff = int(random.triangular(-100, 100, 0))
    b = (a - diff/10)/magnitude
    a = a/magnitude
    goal = random.choice(["bigger", "smaller"])
    answer = bool(a > b) == bool(goal == "bigger")
    return Question("Which is {0}?".format(goal), "0" if answer else "1", "0a", "single_choice", [a,b])


# 1 - positive numbers
# 1a - addition and subtraction
# 1b - multiplication and devision
# 1c - order and brackets -1a, 1b
# 2 - negative numbers
# 2a - addition and subtraction - 1a
# 2b - multiplication and devision -1b
# 2c - repeated negative multiplication - 2b
# 2d - complex ordered questions with brackets and negatives - 2a, 2c, 1c
# 3 - si units
# 3a - multiplication and devision by powers of 10
# 3b - converting between si magnitude regardless of base - 3a
# 3c - comparison of different magnitude si units - 3b, 0a
# 4 - rounding
# 4a - rounding to whole numbers
# 4b - rounding to d.p. - 4a
# 4c - rounding to s.f. -4b

if __name__ == "__main__":
    for i in range(10):
        print(generate_question("0a"))
