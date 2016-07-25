import pytest
import graph_search as gs
import igraph

def test_function():
    g = igraph.Graph.Erdos_Renyi(n=10, m=12)
    start_vertex = 0
    built_in_bfs_result = g.bfs(start_vertex)[0] # series of nodes visited
    assert(built_in_bfs_result == gs.graph_search(g, start_vertex, 'breadth_first')[0])
