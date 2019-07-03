import collections


class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict


# Check for the visisted and unvisited nodes
def depth_fist_search(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        depth_fist_search(graph, next, visited)
    return visited


def breadth_first_search(graph, startnode):
    # Track the visited and unvisited nodes using queue
    seen, queue = set([startnode]), collections.deque([startnode])
    while queue:
        vertex = queue.popleft()
        marked(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)


def marked(n):
    print(n)


gdict = { "a" : set(["b","c"]),
          "b" : set(["a", "d"]),
          "c" : set(["a", "d"]),
          "d" : set(["e"]),
          "e" : set(["a"])
          }

depth_fist_search(gdict, 'a')
# a b d e c

breadth_first_search(gdict, 'a')
# a c b d e
