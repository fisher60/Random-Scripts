

# Slow, N^2 array access
class QuickFind:
    def __init__(self, n):
        self.id = [x for x in range(0, n - 1)]

    def is_connected(self, p, q):
        return p == q

    def union(self, p, q):
        p_id = self.id[p]
        q_id = self.id[q]

        for count, each in self.id:
            if self.id[count] == p_id:
                self.id[count] = q_id


#also slow, N array access
class QuickUnion:
    def __init__(self, n):
        self.id = [x for x in range(0, n - 1)]

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
