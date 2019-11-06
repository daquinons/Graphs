from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
        self.visited = set()

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise KeyError("That vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vertex in self.vertices[v]:
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vertex in self.vertices[v]:
                    s.push(next_vertex)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        self.visited = set()

        def dft_recursive_print(starting_vertex):
            if starting_vertex not in self.visited:
                self.visited.add(starting_vertex)
                print(starting_vertex)
            for v in self.vertices[starting_vertex]:
                if v not in self.visited:
                    print(v)
                    self.visited.add(v)
                    dft_recursive_print(v)

        dft_recursive_print(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        visited = set()
        q.enqueue([starting_vertex])

        while q.size() > 0:
            path = q.dequeue()
            vertex = path[-1]

            if vertex == destination_vertex:
                return path

            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.vertices[vertex]:
                    path_copy = list(path)
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        path = []
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                path.append(vertex)
                if vertex == destination_vertex:
                    break
                for next_vert in self.vertices[vertex]:
                    stack.push(next_vert)
        return path


def earliest_ancestor(ancestors, starting_node):
    members = []
    graph = Graph()
    # Setting up the Graph
    for ancestor in ancestors:
        if ancestor[0] not in members:
            graph.add_vertex(ancestor[0])
            members.append(ancestor[0])
        if ancestor[1] not in members:
            graph.add_vertex(ancestor[1])
            members.append(ancestor[1])
        graph.add_edge(ancestor[0], ancestor[1])

    earliest = {}
    for member in members:
        # Using bfs to find possible paths
        path = graph.bfs(member, starting_node)
        if path is not None and len(path) > 1:
            if len(path) not in earliest or earliest[len(path)] > path[0]:
                earliest[len(path)] = path[0] # Interested in only the first element of the path

    if len(earliest) == 0:
        return -1

    return earliest[max(earliest)] # The longest path is the one that will have the earliest ancestor
