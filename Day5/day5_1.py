from math import floor

def correctMiddles():
    with open('puzzle5.txt') as f:
        lines = [line.strip() for line in f if line.strip()]  # Remove newline characters and ignore empty lines

    total = 0
    rules = []
    updates = []

    for line in lines:
        if '|' in line:
            first, second = line.split('|')
            rules.append((int(first), int(second)))
        else:
            updates.append(list(map(int, line.split(','))))
    def isUpdateValid(update):
        for x, y in rules:
            if x in update and y in update:
                if update.index(x) > update.index(y):
                    return False
        return True

    for update in updates:
        if isUpdateValid(update):
            middle_index = len(update) // 2
            total += update[middle_index]

    print(total)

correctMiddles()
