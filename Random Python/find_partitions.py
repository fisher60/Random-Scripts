class Partition:
    def __init__(self, n):
        self.start_n = n
        self.visited = [[-1 for x in range(self.start_n + 2)] for y in range(self.start_n + 2)]

    def p(self, n, m):
        if self.visited[m][n] != -1:
            return self.visited[m][n]

        if n == 0:
            return 1
        elif n < m:
            return 0

        this_result = self.p(n - m, m + 1) + self.p(n, m + 1)
        self.visited[m][n] = this_result
        return this_result


def solution(n):
    this_partition = Partition(n)
    return this_partition.p(n, 1) - 1


print(solution(200))
