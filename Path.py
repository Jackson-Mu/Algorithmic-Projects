#=========================================================================================================
# Name         : path
# Author       : Jackson Mukeshimana
# Version      : 01
# Date Created : 09/03/2024
# Date Modified: 09/03/2024
# Description  : Finding a path in a directed graph by DFS 
#==========================================================================================================


class DirectedGraph:
    def __init__(self):
        # Initialize the graph with an empty adjacency list
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        # Add a new vertex to the graph if it doesn't already exist
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, start, end):
        # Add an edge between two vertices in the graph
        if start in self.adjacency_list:
            self.adjacency_list[start].append(end)
        else:
            self.adjacency_list[start] = [end]

    def find_path(self, start, end):
        # Find a path from the start node to the end node in the graph
        if start not in self.adjacency_list or end not in self.adjacency_list:
            return "Start or end node not found in the graph"

        visited = set()
        path = []

        def dfs(current):
            visited.add(current)
            path.append(current)

            if current == end:
                return True

            if current not in self.adjacency_list:
                return False

            for neighbor in self.adjacency_list[current]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

            path.pop()
            return False

        if dfs(start):
            return path
        else:
            return "No path found"


def main():
    # Create a DirectedGraph instance and build a sample graph
    graph = DirectedGraph()
    graph.add_edge('X', 'Y')
    graph.add_edge('X', 'Z')
    graph.add_edge('Y', 'A')
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'D')

    start_node = 'X'
    end_node = 'B'

    # Find and print the path from start_node to end_node
    path = graph.find_path(start_node, end_node)
    print("Path from", start_node, "to", end_node, ":", path)


if __name__ == "__main__":
    main()

