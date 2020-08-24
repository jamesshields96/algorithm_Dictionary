# This algorithm traverses a graph breadth ward motion and uses a queue to remember
# to get the next vertex to start a search, when a dead end occurs in any iteration
# We implement BFS for a graph in python using queue data structures
# When we keep visiting the adjacent unvisited nodes and keep adding it to the queue.
# Then we start dequeue only the node which is left with no unvisited nodes
# We stop the program when there is no next adjacent node to be visited.

import collections

class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

def bfs(graph, startnode):
# Track the visited and unvisited nodes using a queue
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

# Graph Dictionary
gdict = { "a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["a"])
                }

bfs(gdict, "a")