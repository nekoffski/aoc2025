import fileinput
import math

def is_invalid(id) -> bool:
    l = len(id)
    return id[0:l//2] == id[l//2:]

def is_invalid2(id) -> bool:
    l = len(id)
    chunk_size = math.floor(l / 2)
    while chunk_size >= 1:
        if l % chunk_size != 0:
            chunk_size -= 1
            continue

        all_same = True
        for i in range(0, len(id), chunk_size):
            if id[i:i+chunk_size] != id[0:chunk_size]:
                all_same = False
                break

        if all_same:
            return True

        chunk_size -= 1
    return False

z1, z2 = 0, 0
for i in list(fileinput.input())[0].split(','):
    s, e = i.split('-')
    for j in range(int(s), int(e) + 1):
        z1 += is_invalid(str(j)) * j
        z2 += is_invalid2(str(j)) * j
print(z1, z2)
