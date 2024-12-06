class TicTacToeGameLogic:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return True

        return False

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def make_move(self, row, col):
        # Validate the move
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def toggle_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_current_player(self):
        return self.current_player
