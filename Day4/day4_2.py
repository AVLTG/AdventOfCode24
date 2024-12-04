def countCrossMas():
    with open('puzzle4.txt', 'r') as f:
        grid = [line.strip().upper() for line in f]  # Ensure consistency in case

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0

    for row in range(1, rows - 1):  # Start from 1 and end at rows - 1 to avoid borders
        for col in range(1, cols - 1):
            if grid[row][col] == 'A':
                diag1 = grid[row - 1][col - 1] + grid[row + 1][col + 1]
                diag2 = grid[row - 1][col + 1] + grid[row + 1][col - 1]
                if diag1 in ['MS', 'SM'] and diag2 in ['MS', 'SM']:
                    count += 1

    print("The X-MAS appears this many times in the grid: " + str(count))


countCrossMas()
