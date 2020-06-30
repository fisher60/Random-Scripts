import platform, os, subprocess

pieces_setup = {
    'pn': {
        'count': 8,
        'movement': {'x': [0], 'y': [1, 2]},
        'passthrough': False,
        'starting_positions': [(i, 1) for i in range(8 + 1)] + [(i, 6) for i in range(8 + 1)]
    },
    'rk': {
        'count': 2,
        'movement': {'x': list(range(-8, 8 + 1)), 'y': list(range(-8, 8 + 1))},
        'passthrough': False,
        'starting_positions': [(0, 0), (7, 0), (0, 7), (7, 7)]
    },
    'kt': {
        'count': 2,
        'movement': 'special',
        'passthrough': True,
        'starting_positions': [(1, 0), (6, 0), (1, 7), (6, 7)]
    },
    'bp': {
        'count': 2,
        'movement': {'x': [], 'y': []},
        'passthrough': False,
        'starting_positions': [(2, 0), (5, 0), (2, 7), (5, 7)]
    },
    'kg': {
        'count': 1,
        'movement': {'x': [], 'y': []},
        'passthrough': False,
        'starting_positions': [(3, 0), (3, 7)]
    },
    'qn': {
        'count': 1,
        'movement': {'x': [], 'y': []},
        'passthrough': False,
        'starting_positions': [(4, 0), (4, 7)]
    }
}


def clear_command():
    if platform.system() == 'Windows':
        return os.system('cls')
    else:
        return subprocess.call('clear', shell=True)


class Piece:
    def __init__(self, name):
        self.name = name
        setup = pieces_setup[name]

        if setup["movement"] != 'special':
            self.move_x = setup["movement"]['x']
            self.move_y = setup['movement']['y']
        else:
            self.move_x = 'special'
            self.move_y = 'special'

        self.count = setup["count"]
        self.passthrough = setup['passthrough']
        self.start_pos = setup["starting_positions"]

    def __repr__(self):
        return self.name


class Pawn(Piece):
    def __init__(self, start_position):
        self.player = 1 if start_position[1] < 2 else 2
        super().__init__('pn')

    def movement(self, start_position: tuple, end_position: tuple):
        return True if end_position[0] - start_position[0] == self.move_x and \
                       end_position[1] - start_position[1] == self.move_y else False


class Rook(Piece):
    def __init__(self, start_position):
        self.player = 1 if start_position[1] < 2 else 2
        super().__init__('rk')

    def movement(self, start_position: tuple, end_position: tuple):
        pass


class Knight(Piece):
    def __init__(self, start_position):
        self.player = 1 if start_position[1] < 2 else 2
        super().__init__('kt')

    def movement(self, start_position: tuple, end_position: tuple):
        pass


class Bishop(Piece):
    def __init__(self, start_position):
        self.player = 1 if start_position[1] < 2 else 2
        super().__init__('bp')

    def movement(self, start_position: tuple, end_position: tuple):
        pass


class King(Piece):
    def __init__(self, start_position):
        self.player = 1 if start_position[1] < 2 else 2
        super().__init__('kg')

    def movement(self, start_position: tuple, end_position: tuple):
        pass


class Queen(Piece):
    def __init__(self, start_position):
        self.player = 1 if start_position[1] < 2 else 2
        super().__init__('qn')

    def movement(self, start_position: tuple, end_position: tuple):
        pass


class Board:
    def __init__(self):

        self.pieces = [Pawn, Rook, Knight, Bishop, King, Queen]

        self.board = {}
        self.restart_board()

        self.current_player = 1

        self.game_active = True

    def __str__(self):
        visual_board = '0   '
        visual_board += (' ' * 8).join([chr(x) for x in range(97, 105)]) + '\n'

        new_row = True

        for each in self.board:

            if new_row:
                start = str(each[1] + 1)
            else:
                start = ''
            new_row = False

            item = self.board[each] if self.board[each] else '   '

            if (each[0] + 1) % 8 == 0:
                next_string = '\n\n'
                new_row = True
            else:
                next_string = ' ' * 3

            if self.board[each] is not None:
                visual_board += f'{start} [{item}{item.player}]' + next_string
            else:
                visual_board += f'{start} [{item}]' + next_string

        return visual_board

    # def grid(self, piece, *, x, y):
    #     self.board[(x, y)] = piece

    def refresh(self):
        print(self)

    def move(self, start_position: tuple, end_position: tuple):
        if self.board[start_position] is not None and self.board[start_position].movement(start_position, end_position):
            self.board[end_position], self.board[start_position] = self.board[start_position], None
            print(f'moved to {end_position}')
        else:
            print(f'cannot move to {end_position}')

    def restart_board(self):
        clear_command()

        for i in range(64):
            this_grid = (i % 8, i // 8)
            self.board[this_grid] = None

            if i < 16 + 1 or i > 47:
                for piece in self.pieces:
                    piece = piece(this_grid)
                    if this_grid in piece.start_pos:
                        self.board[this_grid] = piece
                        break

    def turn(self):
        this_from = input(f'{self.current_player} choose a grid to move from')
        this_to = input(f'{self.current_player} choose a grid to move to')
        print(f'you moved from {this_from} to {this_to}')
        self.current_player = 1 if self.current_player > 1 else 2


# if __name__ == '__main__':
#     board = Board()
#     board.refresh()
#     while board.game_active:
#         board.turn()

print(Board())
