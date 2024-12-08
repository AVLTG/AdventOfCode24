def reorderCalculation():
    with open('puzzle5.txt') as f:
        lines = [line.strip() for line in f if line.strip()]

    rules = []
    updates = []

    for line in lines:
        if '|' in line:
            first, second = line.split('|')
            rules.append((int(first), int(second)))
        else:
            updates.append(list(map(int, line.split(','))))

    def isUpdateValid(update):  # should have probably made this a separate function in day5_1 so i could import and
        # call but I was lazy
        for x, y in rules:
            if x in update and y in update:  # Check if both pages are in the update
                if update.index(x) > update.index(y):  # Ensure x comes before y
                    return False
        return True

    def reorderUpdate(update):
        graph = {page: [] for page in update}
        in_degree = {page: 0 for page in update}

        for x, y in rules:
            if x in update and y in update:
                graph[x].append(y)
                in_degree[y] += 1

        sorted_update = []
        zero_in_degree = [node for node in update if in_degree[node] == 0]

        while zero_in_degree:
            current = zero_in_degree.pop(0)
            sorted_update.append(current)
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    zero_in_degree.append(neighbor)

        return sorted_update

    total = 0

    for update in updates:
        if not isUpdateValid(update):
            sorted_update = reorderUpdate(update)
            middle_index = len(sorted_update) // 2
            total += sorted_update[middle_index]

    print(total)


reorderCalculation()
