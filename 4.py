import fileinput
import copy


grid = list(map(lambda x: x.replace('\n', ''), fileinput.input()))

def neighbours(x, y, xn, yn, grid):
    out = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < xn and 0 <= ny < yn:
                if grid[ny][nx] == '@':
                    out += 1
    return out

def remove_rolls(grid):
    new_grid = [list(row) for row in grid]

    z1 = 0
    for i in range(len(grid)):
        row = list(grid[i])
        for j in range(len(row)):
            if row[j] == '@' and neighbours(j, i, len(row), len(grid), grid) < 4:
                new_grid[i][j] = 'x'
                z1 += 1
    
    new_grid = [''.join(row) for row in new_grid]
    return new_grid, z1


_, z1 = remove_rolls(grid)

z2 = 0
while True:
    grid, removed = remove_rolls(grid)
    if removed == 0:
        break
    z2 += removed

print(z1, z2)