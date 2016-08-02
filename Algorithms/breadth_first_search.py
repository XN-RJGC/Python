# breath_first_search.py
"""
achieve breath first search
"""

graph = {
    "A": ['B', 'C', 'D'],
    "B": ['A', 'C', 'E'],
    "C": ['A', 'B', 'F'],
    "D": ['A', 'F'],
    "E": ['B', 'G'],
    "F": ['D', 'C', 'H'],
    "G": ['E'],
    "H": ['F', 'I'],
    "I": ['H']
}

def breath_first_search():
    """
    Breath first search.
    :return: list
    """
    global graph
    # visited :Record whether the node is accessed
    visited = set()
    visited.add('A')
    # Vertex into the queue to achieve hierarchical visit
    queue = []
    queue.append('A')
    # to store all unique node
    store = []
    # loop access all nodes
    while len(queue) != 0:
        # pop vertex from queue
        graph_item = queue[0]
        store.append(graph_item)
        queue.pop(0)
        # attain all node about graph_item
        graph_item_list = graph.get(str(graph_item))
        for item in graph_item_list:
            # has visited
            if item in visited:
                continue
            # has not vistied
            else:
                visited.add(item)
                queue.append(item)

    return store

if __name__ == '__main__':
    for item in breath_first_search():
        print item