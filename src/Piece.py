import os

TEXTURE = {
    ('pawn', 'white'): '♙',
    ('pawn', 'black'): '♟',
    
    ('knight', 'white'): '♘',
    ('knight', 'black'): '♞',
    
    ('bishop', 'white'): '♗',
    ('bishop', 'black'): '♝',

    ('rook', 'white'): '♖',
    ('rook', 'black'): '♜',

    ('queen', 'white'): '♕',
    ('queen', 'black'): '♛',

    ('king', 'white'): '♔',
    ('king', 'black'): '♚',
}

class Piece:

    def __init__(self, name, color, value):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.captured = False
        self.set_texture()
        
    def add_move(self, move):
        self.moves.append(move)

    def clear_moves(self):
        self.moves = []
        
    def set_texture(self):
        self.texture = TEXTURE[(self.name, self.color)]
    
    def __str__(self):
        return self.texture
        
class Pawn(Piece):

    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        self.en_passant = False
        super().__init__('pawn', color, 1.0)

class Knight(Piece):

    def __init__(self, color):
        super().__init__('knight', color, 3.0)

class Bishop(Piece):

    def __init__(self, color):
        super().__init__('bishop', color, 3.001)

class Rook(Piece):

    def __init__(self, color):
        super().__init__('rook', color, 5.0)

class Queen(Piece):

    def __init__(self, color):
        super().__init__('queen', color, 9.0)

class King(Piece):

    def __init__(self, color):
        self.left_rook = None
        self.right_rook = None
        super().__init__('king', color, 10000.0)