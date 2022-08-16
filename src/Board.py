

# Chess board
class Board:
    empty_board = [[' ' for x in range(8)] for y in range(8)]
    black_spots = '□'
    white_spots = '■'
    for i in range(8):
        black_spots = '■' if i%2 == 0 else '□'
        white_spots = '□' if i%2 == 0 else '■'
        for j in range(8):
            if j%2 == 0:
                empty_board[i][j] = black_spots
            else:
                empty_board[i][j] = white_spots
                
    def __init__(self):
        self.board = self.empty_board
        self.board[0][0] = '♜'
        self.board[0][1] = '♞'
        self.board[0][2] = '♝'
        self.board[0][3] = '♛'
        self.board[0][4] = '♚'
        self.board[0][5] = '♝'
        self.board[0][6] = '♞'
        self.board[0][7] = '♜'
        for i in range(8):
            self.board[1][i] = '♟'
        for i in range(8):
            self.board[6][i] = '♙'
        self.board[7][0] = '♖'
        self.board[7][1] = '♘'
        self.board[7][2] = '♗'
        self.board[7][3] = '♕'
        self.board[7][4] = '♔'
        self.board[7][5] = '♗'
        self.board[7][6] = '♘'
        self.board[7][7] = '♖'
    
    def move(self, start, end):
        if self.board[start[0]][start[1]] == self.empty_board[start[0]][start[1]]:
            return False
        self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
        self.board[start[0]][start[1]] = self.empty_board[start[0]][start[1]]
        return self.board
    
    def __str__(self):
        board_str = '\n'.join([f"{8-i}|{'|'.join(row)}|" for i, row in enumerate(self.board)]).replace(' ', '_')
        board_str += '\n' + f"  {' '.join(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])}"
        return board_str