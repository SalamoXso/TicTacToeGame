class GameUI:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
    
    def draw_board(self):
        # Function to display the current state of the Tic Tac Toe board
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def update_board(self, row, col, player):
        # Function to update the board with the player's move
        if self.board[row][col] == " ":
            self.board[row][col] = player
        else:
            print("Invalid move! Position already taken.")

def get_player_input():
    while True:
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if 0 <= row < 3 and 0 <= col < 3:
                return row, col
            else:
                print("Invalid input. Please enter a number between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter integers only.")
