import fileinput

t = list(map(lambda x: x.replace('\n', '').split(':'), fileinput.input()))
d = {x[0]: x[1].strip().split(' ') if x[1].strip() != '' else [] for x in t}


def traverse(start='you', required=[]):
    required_set = set(required)
    memo = {}
    
    def count_paths_with_required(node, visited_in_path, seen_required):
        if node == 'out':
            if seen_required == required_set:
                return 1
            return 0
        
        if node in visited_in_path:
            return 0
        
        cache_key = (node, frozenset(seen_required))
        if cache_key in memo:
            return memo[cache_key]
        
        new_visited = visited_in_path | {node}
        new_seen = seen_required | ({node} if node in required_set else set())
        
        total = 0
        if node in d:
            for neighbor in d[node]:
                total += count_paths_with_required(neighbor, new_visited, new_seen)
        
        memo[cache_key] = total
        return total
    
    return count_paths_with_required(start, set(), set())

t1 = traverse(start='you')
t2 = traverse(start='svr', required=['dac', 'fft'])
print(t1, t2)


