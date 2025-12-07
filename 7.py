import fileinput
import copy

grid = list(map(lambda x: x.replace('\n', ''), fileinput.input()))
particles = {grid[0].index('S'): 1}
splits = paths = 0

def add(d, k, v):
    if k in d:
        d[k] += v
    else:
        d[k] = v


for row in grid[1:]:
    new_particles = copy.deepcopy(particles)
    for k, v in particles.items():
        if row[k] == '^':
            splits += 1
            paths += v

            add(new_particles, k + 1, v)
            add(new_particles, k - 1, v)
            new_particles.pop(k)

    particles = new_particles

print(splits, paths + 1)
