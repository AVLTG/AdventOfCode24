def countXmas():
    with open('puzzle4.txt', 'r') as f:
        grid = [line.strip() for line in f]

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    word = "XMAS"
    word_length = len(word)
    count = 0

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'X':
                for dr, dc in directions:
                    found = True
                    for i in range(1, word_length):
                        new_r = row + dr * i
                        new_c = col + dc * i
                        if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                            found = False
                            break
                        if grid[new_r][new_c] != word[i]:
                            found = False
                            break
                    if found:
                        count += 1

    print("The word 'XMAS' appears this many times in the grid: " + str(count))


countXmas()
