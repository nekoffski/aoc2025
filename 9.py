import fileinput

coords = [list(map(lambda x: int(x), line.replace('\n', '').split(','))) for line in fileinput.input()]
n = len(coords)
poly_edges = [(coords[i], coords[(i+1) % n]) for i in range(n)]
EPS = 1e-12


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def on_segment(a, b, p):
    if abs(cross(a, b, p)) > EPS:
        return False
    return (min(a[0], b[0]) - EPS <= p[0] <= max(a[0], b[0]) + EPS and
            min(a[1], b[1]) - EPS <= p[1] <= max(a[1], b[1]) + EPS)


def is_point_inside(p):
    n = len(coords)
    x, y = p
    inside = False

    for i in range(n):
        a = coords[i]
        b = coords[(i + 1) % n]

        if on_segment(a, b, (x, y)):            
            return True

        ay, by = a[1], b[1]

        if (ay > y) != (by > y):
            x_intersect = a[0] + (y - ay) * (b[0] - a[0]) / (by - ay)
            if x_intersect > x:
                inside = not inside
    return inside


def is_inside(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    xmin, xmax = min(x1, x2), max(x1, x2)
    ymin, ymax = min(y1, y2), max(y1, y2)

    rect = [
        (xmin, ymin),
        (xmin, ymax),
        (xmax, ymax),
        (xmax, ymin)
    ]

    for corner in rect:
        if not is_point_inside(corner):
            return False

    rect_edges = [
        (rect[0], rect[1]),
        (rect[1], rect[2]),
        (rect[2], rect[3]),
        (rect[3], rect[0])
    ]
    
    for re in rect_edges:
        for pe in poly_edges:
            o1 = cross(re[0], re[1], pe[0])
            o2 = cross(re[0], re[1], pe[1])
            o3 = cross(pe[0], pe[1], re[0])
            o4 = cross(pe[0], pe[1], re[1])
            
            if (o1 * o2 < -EPS) and (o3 * o4 < -EPS):
                return False
    return True


def area(a, b):
    x = abs(a[0] - b[0]) + 1
    y = abs(a[1] - b[1]) + 1
    return x * y


m1 = m2 = 0

for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        x, y = coords[i], coords[j]
        
        a = area(x, y)
        if a > m1:
            m1 = a

        if is_inside(x, y):
            if a > m2:
                m2 = a

print(m1, m2)
