import random


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        self.total_friendships = 0

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            self.total_friendships += 1

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        self.total_friendships = 0
        # !!!! IMPLEMENT ME

        # Add users
        for num_user in range(numUsers):
            self.addUser("User " + str(num_user))

        # Create friendships
        while self.total_friendships < (numUsers * avgFriendships) / 2:
            choices = (random.choice(list(self.users.keys())),
                       random.choice(list(self.users.keys())))
            if choices[0] != choices[1] and choices[0] < choices[1] and choices[1] not in self.friendships[choices[0]]:
                self.addFriendship(choices[0], choices[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        for id_user in self.users.keys():
            path = self.bfs(userID, id_user)
            if path is not None:
                visited[id_user] = path
        return visited

    def bfs(self, starting_vertex, destination_vertex):
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
                for neighbor in self.friendships[vertex]:
                    path_copy = list(path)
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
