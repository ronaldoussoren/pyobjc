"""
Module defining a topological sort function, see
<http://www.bitformation.com/art/python_toposort.html> for more
information.

Original topological sort code written by Ofer Faigon
(www.bitformation.com) and used with permission
"""

import typing


def topological_sort(
    items: typing.Sequence[str], partial_order: typing.Sequence[tuple[str, str]]
) -> list[str]:
    """
    Perform topological sort.
    items is a list of items to be sorted.
    partial_order is a list of pairs. If pair (a,b) is in it, it means
    that item a should appear before item b.
    Returns a list of the items in one of the possible orders, or None
    if partial_order contains a loop.
    """

    class GraphNode:
        numincoming: int
        outgoing: list[str]

        def __init__(self) -> None:
            self.numincoming = 0
            self.outgoing = []

    def add_node(graph: dict[str, GraphNode], node: str) -> None:
        """Add a node to the graph if not already exists."""
        if node not in graph:
            graph[node] = GraphNode()

    def add_arc(graph: dict[str, GraphNode], fromnode: str, tonode: str) -> None:
        """Add an arc to a graph. Can create multiple arcs.
        The end nodes must already exist."""
        graph[fromnode].outgoing.append(tonode)
        graph[tonode].numincoming += 1

    # step 1 - create a directed graph with an arc a->b for each input
    # pair (a,b).
    # The graph is represented by a dictionary. The dictionary contains
    # a pair item:list for each node in the graph. /item/ is the value
    # of the node. /list/'s 1st item is the count of incoming arcs, and
    # the rest are the destinations of the outgoing arcs. For example:
    #           {'a':[0,'b','c'], 'b':[1], 'c':[1]}
    # represents the graph:   c <-- a --> b
    # The graph may contain loops and multiple arcs.
    # Note that our representation does not contain reference loops to
    # cause GC problems even when the represented graph contains loops,
    # because we keep the node names rather than references to the nodes.
    graph: dict[str, GraphNode] = {}
    for v in items:
        add_node(graph, v)
    for a, b in partial_order:
        add_arc(graph, a, b)

    # Step 2 - find all roots (nodes with zero incoming arcs).
    roots = [node for (node, nodeinfo) in graph.items() if nodeinfo.numincoming == 0]

    # step 3 - repeatedly emit a root and remove it from the graph. Removing
    # a node may convert some of the node's direct children into roots.
    # Whenever that happens, we append the new roots to the list of
    # current roots.
    sorted_items = []
    while len(roots) != 0:
        # If len(roots) is always 1 when we get here, it means that
        # the input describes a complete ordering and there is only
        # one possible output.
        # When len(roots) > 1, we can choose any root to send to the
        # output; this freedom represents the multiple complete orderings
        # that satisfy the input restrictions. We arbitrarily take one of
        # the roots using pop(). Note that for the algorithm to be efficient,
        # this operation must be done in O(1) time.
        roots.sort(reverse=True)
        root = roots.pop()
        sorted_items.append(root)
        for child in graph[root].outgoing:
            graph[child].numincoming -= 1
            if graph[child].numincoming == 0:
                roots.append(child)
        del graph[root]
    if len(graph.items()) != 0:
        # There is a loop in the input.
        raise RuntimeError("input cannot be sorted")
    return sorted_items
