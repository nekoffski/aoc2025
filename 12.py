import fileinput
data = ''.join(fileinput.input()).split('\n')

shapes = []
regions = []

def parse_input():
    sh = []
    for line in data:
        if line == '':
            continue
        if 'x' in line:
            parts = line.split(': ')
            dims = list(map(int, parts[0].split('x')))
            counts = list(map(int, parts[1].split(' ')))
            regions.append((dims[0], dims[1], counts))
            continue
        if ':' in line:
            sh.append([])
            continue
        sh[-1].append(line)
    
    for shape in sh:
        coords = []
        for y, row in enumerate(shape):
            for x, c in enumerate(row):
                if c == '#':
                    coords.append((x, y))
        shapes.append(coords)

parse_input()


total = 0
for region in regions:
    w, h, counts = region
    c = sum(counts)
    total += (9 * c <= w * h)
print(total)

