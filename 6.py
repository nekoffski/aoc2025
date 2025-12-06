import fileinput
import functools as fp


def transpose(matrix):
    return list(map(list, zip(*matrix)))


widths = []
raw = list(map(lambda x: x.replace('\n', ''), fileinput.input()))

def calc_widths(row):
    cur = 1
    for x in row[1:]:
        if x != ' ':
            widths.append(cur - 1)
            cur = 1
        else:
            cur += 1
    widths.append(cur)

calc_widths(raw[-1])

def split(row):
    res = []
    idx = 0
    for w in widths:
        res.append(row[idx:idx + w])
        idx += w + 1
    return res

data = transpose(map(split, raw))

ops = {
    '+' : lambda x, y: x + y,
    '*' : lambda x, y: x * y,
}

z1 = z2 = 0

for row in data:
    op = ops.get(row[-1].strip())
    vals = row[:-1]

    z1 += fp.reduce(op, map(int, vals))
    z2 += fp.reduce(op, map(int, [''.join(x) for x in transpose(vals)]))

print(z1, z2)
