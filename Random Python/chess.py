class Piece:
    def __init__(self, name, setup):
        self.name = name

        if setup["movement"] != 'special':
            self.move_x = setup["movement"]['x']
            self.move_y = setup['movement']['y']
        else:
            self.move_x = 'special'
            self.move_y = 'special'

        self.count = setup["count"]
        self.passthrough = setup['passthrough']


class Board:
    def __init__(self):
        self.board = {i: None for i in range(64)}
        self.current_player = None

    def __str__(self):
        visual_board = ''
        for count in self.board:
            item = self.board[count] if self.board[count] else ' '

            next_string = '\n' if (count + 1) % 8 == 0 else ' '

            visual_board += f'[{item}]' + next_string

        return visual_board


pieces  = {
    'pawn': {
        'count': 8,
        'movement': {'x': [], 'y': [1, 2]},
        'passthrough': False
    },
    'rook': {
        'count': 2,
        'movement': {'x': list(range(-8, 8 + 1)), 'y': list(range(-8, 8 + 1))},
        'passthrough': False
    },
    'knight': {
        'count': 2,
        'movement': 'special',
        'passthrough': True
    },
    'bishop': {
        'count': 2,
        'movement': {'x': [], 'y': []},
        'passthrough': False
    },
    'queen': {
        'count': 1,
        'movement': {'x': [], 'y': []},
        'passthrough': False
    },
    'king': {
        'count': 1,
        'movement': {'x': [], 'y': []},
        'passthrough': False
    }
}

print(Board())

