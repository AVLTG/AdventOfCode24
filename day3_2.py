import re


def calculateConditionalMults():
    f = open('puzzle3.txt')
    memory = f.read()

    pattern = re.compile(r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)")

    total = 0
    mul_enabled = True

    for match in pattern.finditer(memory):
        if match.group(0) == 'do()':
            mul_enabled = True
        elif match.group(0) == "don't()":
            mul_enabled = False
        else:
            x, y = int(match.group(1)), int(match.group(2))
            if mul_enabled:
                product = x * y
                total += product

    print(total)


calculateConditionalMults()
