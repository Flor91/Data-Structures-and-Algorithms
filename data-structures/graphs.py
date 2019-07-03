# Generate a graph with:
# Vertices
V = {"a", "b", "c", "d", "e"}
# Edges
E = {"ab", "ac", "bd", "cd", "de"}

class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def get_vertices(self):
        """
            Print graph vertices
        """
        return list(self.gdict.keys())
    
    def find_edges(self):
        edges_list = []
        for k in self.gdict:
            for v in self.gdict[k]:
                if {k, v} not in edges_list:
                    edges_list.append({v, k})
        return edges_list
    
    def add_node(self, key):
        if key not in self.gdict.keys():
            self.gdict[key] = []

    def add_edge(self, edge):
        node1, node2 = edge
        if node1 in self.gdict:
            self.gdict[node1].append(node2)
        else:
            self.gdict[node1] = [node2]

# Create the dictionary with graph elements
graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

g = graph(graph_elements)

print(g.get_vertices())
# ['a', 'b', 'c', 'd', 'e']
print(g.find_edges())
# [{'b', 'a'}, {'a', 'c'}, {'b', 'd'}, {'c', 'd'}, {'e', 'd'}]

g.add_node('f')
g.add_edge({'a', 'f'})

print(g.find_edges())