# from collections import deque

# # This class represents a directed graph using adjacency list representation
# class Graph:
#     def __init__(self, V):
#         self.V = V                      # Number of vertices
#         self.adj = [[] for _ in range(V)]  # Adjacency list

#     # Function to add an edge to the graph
#     def add_edge(self, v, w):
#         self.adj[v].append(w)  # Add w to v's list

#     # Prints BFS traversal from a given source s
#     def bfs(self, s):
#         # Mark all vertices as not visited
#         visited = [False] * self.V

#         # Create a queue for BFS
#         queue = deque()

#         # Mark the source node as visited and enqueue it
#         visited[s] = True
#         queue.append(s)

#         while queue:
#             # Dequeue a vertex and print it
#             s = queue.popleft()
#             print(s, end=" ")

#             # Get all adjacent vertices of the dequeued vertex s
#             # If an adjacent has not been visited, mark it visited and enqueue it
#             for i in self.adj[s]:
#                 if not visited[i]:
#                     visited[i] = True
#                     queue.append(i)

# # Driver code to test the methods of Graph class
# if __name__ == "__main__":
#     # Create a graph given in the above diagram
#     g = Graph(4)
#     g.add_edge(0, 1)
#     g.add_edge(0, 2)
#     g.add_edge(1, 2)
#     g.add_edge(2, 0)
#     g.add_edge(2, 3)
#     g.add_edge(3, 3)

#     print("Following is Breadth First Traversal (starting from vertex 2):")
#     g.bfs(2)


# from collections import deque

# class Tree:
#     def __init__(self):
#         self.graph = {}

#     def add_edge(self, parent, child):
#         if parent not in self.graph:
#             self.graph[parent] = []
#         self.graph[parent].append(child)

#     def bfs(self, start, goal):
#         visited = set()
#         queue = deque([[start]])

#         while queue:
#             path = queue.popleft()
#             node = path[-1]

#             if node == goal:
#                 return path

#             if node not in visited:
#                 visited.add(node)
#                 for neighbor in self.graph.get(node, []):
#                     new_path = list(path)
#                     new_path.append(neighbor)
#                     queue.append(new_path)

#         return None

# # Build the tree
# tree = Tree()
# tree.add_edge('A', 'B')
# tree.add_edge('A', 'F')
# tree.add_edge('A', 'D')
# tree.add_edge('A', 'E')
# tree.add_edge('B', 'K')
# tree.add_edge('B', 'J')
# tree.add_edge('K', 'N')
# tree.add_edge('K', 'M')
# tree.add_edge('D', 'G')
# tree.add_edge('E', 'C')
# tree.add_edge('E', 'H')
# tree.add_edge('E', 'I')
# tree.add_edge('I', 'L')

# # Run BFS
# path = tree.bfs('A', 'G')

# if path:
#     print("BFS path to G:", " → ".join(path))
# else:
#     print("Goal node not found.")

# import heapq

# class PriorityQueue:
#     def __init__(self):
#         self.queue = []

#     def push(self, item, priority):
#         heapq.heappush(self.queue, (priority, item))

#     def pop(self):
#         if not self.is_empty():
#             return heapq.heappop(self.queue)[1]
#         return None

#     def peek(self):
#         if not self.is_empty():
#             return self.queue[0][1]
#         return None

#     def is_empty(self):
#         return len(self.queue) == 0

# # Example usage:
# pq = PriorityQueue()
# pq.push("Task A", 3)
# pq.push("Task B", 1)
# pq.push("Task C", 2)

# print("Priority Queue Processing Order:")
# while not pq.is_empty():
#     print(pq.pop())


import heapq
class priority_queue:
    def __init__(self):
        self.queue=[]
    def push(self,item,priority):
        heapq.heappush(self.queue,(priority,item))
    def pop(self):
        if not self.is_empty():
         return heapq.heappop(self.queue)[1]
    def seek(self):
       if not self.is_empty():
         return self.queue[0][1]
    def is_empty(self):
       return len(self.queue)==0
    
q=priority_queue()
q.push("taskA",1)
while not q.is_empty():
   print(q.pop())

       
