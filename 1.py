import fileinput

z1, z2 = 0, 0
s = 50

for i in list(map(lambda x: x[:-1], fileinput.input())):
    v = int(i[1:])
    d = 1 if i[0] == 'R' else -1 

    while v > 0:
        s = (s + d) % 100
        if s == 0:
            z2 += 1
        v -= 1

    if s == 0:
        z1 += 1
    
print (z1, z2)
