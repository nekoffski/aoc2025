import fileinput

db = []

f = list(map(lambda x: x.replace('\n', ''), fileinput.input()))
sep = f.index('')
ranges = f[:sep]
ids = f[sep + 1:]

for r in ranges:
    lo, hi = r.split('-')
    db.append((int(lo), int(hi)))

def merge_ranges(db):
    db.sort()
    merged = []
    current_lo, current_hi = db[0]

    for lo, hi in db[1:]:
        if lo <= current_hi + 1:
            current_hi = max(current_hi, hi)
        else:
            merged.append((current_lo, current_hi))
            current_lo, current_hi = lo, hi
    merged.append((current_lo, current_hi))
    return merged

db = merge_ranges(db)

z1  = z2 = 0
for id in ids:
    for lo, hi in db:
        if lo <= int(id) <= hi:
            z1 += 1
            break

for lo, hi in db:
    z2 += hi - lo + 1
    
print(z1, z2)


