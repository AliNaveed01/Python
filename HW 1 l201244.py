from collections import defaultdict


class Graph:
    def _init_(self):
        # list isliye because we any node can be connected with anyone of the node
        # it is same as we make
        # graph = {0:[1,2], 1:[2,3,4,0]}
        self.graph = defaultdict(list)

    def addEdge(self, key, value):
        # this will simply add a key value pair in graph
        self.graph[key].append(value)

    def bfs(self, s):
        #making a list of the size 1 more than the actual size of the graph nodes
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


if _name_ == '_main_':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Breadth First Traversal")
    g.bfs(2)