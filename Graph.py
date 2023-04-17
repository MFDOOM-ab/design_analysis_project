from collections import defaultdict
 
 
class Graph():
     
    def __init__(self, vertices, count):
        self.graph = defaultdict(list)
        self.vertices = vertices
        self.count= count
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    def testCyclicUtil(self, v, visited, stack):
        # Sets the current node as visited
        # pushes node to stack
        
        visited[v] = True
        stack[v] = True
       
        # if any neighbor node is visited and in stack then graph is cyclic
        # example neighbor is 2 and 2 in stack, then node was revisited thus cycle
       
        for neighbor in self.graph[v]:
            if visited[neighbor] == False:
                if self.testCyclicUtil(neighbor, visited, stack) == True:
             
                    return True
            elif stack[neighbor] == True:
                self.count= self.count+1
                print(neighbor)
                return True
 
        # The node needs to be popped from
        # recursion stack before function ends
        stack[v] = False
        return False
 
    # If cyclic return true
    def testCyclic(self):
        visited = [False] * (self.vertices + 1)
        stack = [False] * (self.vertices + 1)
        for node in range(self.vertices):
            if visited[node] == False:
                if self.testCyclicUtil(node, visited, stack) == True:
                    return True
        return False
 
 
# Driver code
if __name__ == '__main__':
    g = Graph(12, 0)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 1)
    g.addEdge(2, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 1)
    g.addEdge(3, 6)
    g.addEdge(3, 7)
    g.addEdge(4, 2)
    g.addEdge(4, 8)
    g.addEdge(5, 2)
    g.addEdge(5, 9)
    g.addEdge(5, 10)
    g.addEdge(6, 3)
    g.addEdge(6, 11)
    g.addEdge(7, 3)
    g.addEdge(7, 8)
    g.addEdge(8, 4)
    g.addEdge(8, 7)
    g.addEdge(9, 5)
    g.addEdge(9, 3)
    g.addEdge(10, 5)
    g.addEdge(11, 6)
    g.addEdge(11, 12)
    g.addEdge(12, 11)
   
  
 
    if g.testCyclic() == 1:
        print("This graph contains " + str(g.count) + " cycles")
        
    else:
        print("Graph doesn't contain cycle")
 