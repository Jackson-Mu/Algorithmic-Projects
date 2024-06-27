#=========================================================================================================
# Name         : Detecting Cycle in a Directed Graph by DFS
# Author       : Jackson Mukeshimana
# Version      : 01
# Date Created : 09/03/2024
# Date Modified: 09/03/2024
# Description  : Algorithm for Detecting Cycle in a directed graph by DFS
#==========================================================================================================

#QUESTION 6: DETECTING CYCLE IN THE DIRECTED GRAPH 


# Strategy for Detecting Cycle in Directed Graph:

# 1. Start DFS traversal from each node.
# 2. Keep track of visited nodes and nodes in the current recursion stack.
# 3. If a node is visited and present in the recursion stack, a cycle is detected.
# 4. Repeat this process for all nodes in the graph.


from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[v] = False
        return False

    def is_cyclic(self):
        visited = {node: False for node in self.graph}
        rec_stack = {node: False for node in self.graph}
        
        for node in self.graph:
            if not visited[node]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        return False

    def print_cycle_detection(self):
        if self.is_cyclic():
            print("Great News: Cycle detected in the graph.")
        else:
            print("Bad News: No cycle found in the graph.")

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 1)
    
    g.print_cycle_detection()
