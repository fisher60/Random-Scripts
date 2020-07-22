def create_board():
    board = []
    y = 0
    first = True
    for value in range(64):
        x = value % 8
        if x == 0 and not first:
            y += 1
        first = False
        board.append((x, y))
    return board


class Knight:
    move_x = [2, 2, -2, -2, 1, 1, -1, -1]
    move_y = [1, -1, 1, -1, 2, -2, 2, -2]
    moves = []

    def __init__(self, start_pos, destination):
        self.x = start_pos[0]
        self.y = start_pos[1]


def in_boundaries(x, y):
    if 0 <= x < 8 and 0 <= y < 8:
        return True
    else:
        return False


class Cell:
    cells = {}

    def __init__(self, x=0, y=0, distance=0):
        self.x = x
        self.y = y
        self.distance = distance
        self.visited = False
        self.cells[(self.x, self.y)] = self

    def was_visited(self, x, y):
        if (x, y) in self.cells:
            return self.cells[(x, y)].visited
        else:
            return False


def solution(src, dest):
    board = create_board()

    src = board[src]
    dest = board[dest]

    knight = Knight(src, dest)
    knight.moves.append(Cell(src[0], src[1]))
    knight.moves[0].visited = True

    while len(knight.moves) > 0:

        this_cell = knight.moves[0]
        knight.moves.pop(0)

        if this_cell.x == dest[0] and this_cell.y == dest[1]:
            return this_cell.distance

        for i in range(8):
            x = this_cell.x + knight.move_x[i]
            y = this_cell.y + knight.move_y[i]
            if in_boundaries(x, y) and not this_cell.was_visited(x, y):
                this_cell.visited = True
                knight.moves.append(Cell(x, y, this_cell.distance + 1))


print(solution(0, 1))