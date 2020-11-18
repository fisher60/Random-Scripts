import random


def make_connections(data_set):
    connections = []
    for _ in data_set:
        connections.append((random.choice(data_set), random.choice(data_set)))
    return connections


# Slow, N^2 array access
class QuickFind:
    def __init__(self, n: int):
        self.id = [x for x in range(0, n)]
        self.connections = make_connections(self.id)

    def __str__(self):
        return str(self.id)

    def is_connected(self, p, q):
        return p == q

    def union(self, p, q):
        p_id = self.id[p]
        q_id = self.id[q]

        for count in self.id:
            if self.id[count] == p_id:
                self.id[count] = q_id


# also slow, N array access
class QuickUnion:
    def __init__(self, n: int, connections=None):
        self.id = [x for x in range(0, n)]
        if not connections:
            self.connections = self.create_sample_connections()

    def __str__(self):
        return str(self.id)

    def create_sample_connections(self):
        connections = []
        data_set = self.id
        for _ in data_set:
            connections.append((random.choice(data_set), random.choice(data_set)))
        return connections

    def root(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]  # one-pass path compression improvement
            i = self.id[i]
        return i

    def is_connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)

        if i == j:  # weighted to join smaller trees to larger
            return
        else:
            self.id[i] = j


if __name__ == '__main__':
    test = QuickUnion(5)
    print(test.connections)
    for connection in test.connections:
        test.union(connection[0], connection[1])
    print(test)
