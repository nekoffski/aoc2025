import fileinput


def max2(r):
    l = len(r)
    v = max(r)
    vp = r.find(v)

    if vp != l - 1:
        return int(v), int(max(r[vp + 1:]))
    else:
        return int(max(r[:-1])), int(v)


def max_window(rec):
    out = ''
    n = len(rec)

    l = 0
    r = n - 12

    while r < n:
        window = rec[l:r + 1]
        m = max(window)
        out += m
        l += window.index(m) + 1
        r += 1
    return int(out)

z1 = z2 = 0 
for r in map(lambda x: x.replace('\n', ''), fileinput.input()):
    v1, v2 = max2(r)
    z1 += v1 * 10 + v2
    z2 += max_window(r)

print(z1, z2)