# + edges:
# 0--1 1--2 1--4 3--5 3--6 4--6 5--6 0--7 6--7 1--9 4--9 7--9
# takes an igraph graph object and start vertex as the id of a vertex in said graph
#
def graph_search(graph, start_vertex, search_type = 'breadth_first'):
    visited = []
    unvisited = map(lambda x: x.index, graph.vs)
    stack = [start_vertex]
    while len(stack) > 0:
        current = stack.pop(0)
        visited.append(current)
        unvisited.remove(current)
        neighbors = graph.neighbors(current)
        for neighbor in neighbors:
            if neighbor not in visited and neighbor not in stack:
                if search_type == 'breadth_first':
                    stack.append(neighbor)
                elif search_type == 'depth_first':
                    stack.insert(0, neighbor)
    return [visited, unvisited]
