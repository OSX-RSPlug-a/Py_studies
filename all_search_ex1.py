
neighbors_dict = {
    'START': ['B', 'C'],
    'B': ['GOAL'],
    'C': ['GOAL'],
    'GOAL': []
}

def neighbors(node):
    return neighbors_dict.get(node, [])

def min_f(open_set):
    return next(iter(open_set))


start = 'START'
goal = 'GOAL'
inf = float('inf')

gp = {start: 0}
parent = {}


open_set = {start}

print("Starting algorithm tracking:")
print("=" * 40)

while open_set:
    cur = min_f(open_set)
    print(f"\n Visiting node: {cur}")
    
    if cur == goal:
        print("Goal reached")
        break
        

    open_set.remove(cur)

    for nb in neighbors(cur):
        g2 = gp[cur] + 1

        
        if g2 < gp.get(nb, inf):
            parent[nb] = cur
            gp[nb] = g2       
            open_set.add(nb)  
            print(f" -> Found better path to {nb} via {cur} (g={g2})")
        else:
            print(f" -> Path to {nb} via {cur} is not shorter.")


print("=" * 40)
print("Parents dictionary for path reconstruction:", parent)