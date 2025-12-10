import fileinput
import re
import pulp
from collections import deque


def split(line):
    light = [1 if c == '#' else 0 for c in line[line.index('[')+1:line.index(']')]]
    paren_pattern = r'\(([^)]+)\)'
    paren_groups = re.findall(paren_pattern, line)
    jolt = line[line.rindex('{')+1:line.rindex('}')].split(',')
    return light, [list(map(int, x.split(','))) for x in paren_groups], jolt


lines = list(split(line.replace('\n', '')) for line in fileinput.input())


def solve1(i):
    expected, buttons, _ = i
    start = tuple([0] * len(expected))
    target = tuple(expected)
    
    if start == target:
        return 0
        
    queue = deque([(start, 0)])
    visited = {start}
    
    while queue:
        state, steps = queue.popleft()
        
        for b in buttons:
            new_state = list(state)
            for idx in b:
                new_state[idx] ^= 1
            new_state = tuple(new_state)
            
            if new_state == target:
                return steps + 1
            
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, steps + 1))


def solve2(line):
    _, steps, jolt = line
    
    def impl(start, expected, steps):
        n = len(start)
        m = len(steps)
        target = [expected[i] - start[i] for i in range(n)]
        
        prob = pulp.LpProblem("min_steps", pulp.LpMinimize)
        x = [pulp.LpVariable(f"x{j}", lowBound=0, cat="Integer") for j in range(m)]
        for i in range(n):
            prob += sum(x[j] for j in range(m) if i in steps[j]) == target[i]
        prob += sum(x)

        prob.solve(pulp.PULP_CBC_CMD(msg=False))
        if pulp.LpStatus[prob.status] != "Optimal":
            return None

        return int(sum(v.value() for v in x))
    return impl([0]*len(jolt), list(map(int, jolt)), steps)

total = total2 = 0

for line in lines:
    total += solve1(line)
    total2 += solve2(line)

print(total, total2)