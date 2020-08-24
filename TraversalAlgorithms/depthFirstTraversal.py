# This algorithm traverses a graph in a depth ward motion and uses a stack to
# remember to get the next vertex to start a search, when a dead end occurs in any iteration.
# We implement DFS for a graph in python using the set data types as they provide
# the required functionalities to keep track of visited and unvisited nodes

class graph:

    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

# Check for the visited and unvisited nodes

def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

gdict = { "a" : set(["b","c"]),
                "b" : set(["a","d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["a"])
                }

dfs(gdict, 'a')

