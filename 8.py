import fileinput
import math

coords = list(map(lambda x: x.replace('\n', '').split(','), fileinput.input()))
coords = [tuple(c) for c in coords]

def dist3(a, b):
    return  math.sqrt(
        (int(a[0]) - int(b[0])) ** 2 +
        (int(a[1]) - int(b[1])) ** 2 +
        (int(a[2]) - int(b[2])) ** 2
    )


distances = []

for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        a = coords[i]
        b = coords[j]
        distances.append((dist3(a, b), a, b))

distances.sort(key=lambda x: x[0])

parent = {}

def find(x):
    if x not in parent:
        parent[x] = x
    if parent[x] != x:
        parent[x] = find(parent[x]) 
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a

for coord in coords:
    find(coord)

n = 1000
for i in range(n):
    _, a, b = distances[i]
    union(a, b)

sizes = {}
for coord in coords:
    root = find(coord)
    if root in sizes:
        sizes[root] += 1
    else:
        sizes[root] = 1

sizes = list(sizes.values())
sizes.sort()

a = 1
for s in sizes[-3:]:
    a *= s

print(a)

def count_circuits():
    circuits = set()
    for coord in coords:
        circuits.add(find(coord))
    return len(circuits)

last_a = None
last_b = None

for i in range(len(distances)):
    _, a, b = distances[i]
    if find(a) != find(b):
        union(a, b)
        last_a = a
        last_b = b
        if count_circuits() == 1:
            break

result = int(last_a[0]) * int(last_b[0])
print(result)
