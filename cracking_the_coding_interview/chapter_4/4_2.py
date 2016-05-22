# Given a directed graph, design an algorithm to find out whether there is a route be- tween two nodes
# Note: this solution is for a directed graph without restrictions that it be a binary tree, which the book suggests it is
# Also we assume the graph is stored as a dictionary {"a":["b"], "b":[]} represents the graph a -> b
def find_path(graph, src, destination):
    adj_vrtcs = graph[src]
    # base cases
    if len(adj_vrtcs) == 0: return None
    if destination in adj_vrtcs: return True
    # Otherwise, initiate and loop:
    next_to_visit = adj_vrtcs
    visted = [src]
    while len(next_to_visit) > 0:
        next_src = next_to_visit.pop()
        adj_vrtcs = graph[next_src]
        if destination in adj_vrtcs:
            return True
        else:
            [next_to_visit.append(adj_vrtcs[i]) if not adj_vrtcs[i] in visited for i in range(len(adj_vrtcs))]
    return None
