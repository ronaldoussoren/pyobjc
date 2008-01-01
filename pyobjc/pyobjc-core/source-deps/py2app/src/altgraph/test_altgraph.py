#!/usr/bin/env py.test
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from altgraph import Graph, GraphAlgo

def test_altgraph():

    # these are the edges
    edges = [ (1,2), (2,4), (1,3), (2,4), (3,4), (4,5), (6,5), (6,14), (14,15), (6, 15),
    (5,7), (7, 8), (7,13), (12,8), (8,13), (11,12), (11,9), (13,11), (9,13), (13,10) ]

    store = {}
    g = Graph.Graph()
    for head, tail in edges:
        store[head] = store[tail] = None
        g.add_edge(head, tail)

    # check the parameters
    assert g.number_of_nodes() == len(store)
    assert g.number_of_edges() == len(edges)


    # do a forward bfs
    assert g.forw_bfs(1) == [1, 2, 3, 4, 5, 7, 8, 13, 11, 10, 12, 9]


    # diplay the hops and hop numbers between nodes
    assert g.get_hops(1, 8) == [(1, 0), (2, 1), (3, 1), (4, 2), (5, 3), (7, 4), (8, 5)]

    assert GraphAlgo.shortest_path(g, 1, 12) == [1, 2, 4, 5, 7, 13, 11, 12]

if __name__ == '__main__':
    test_altgraph()
