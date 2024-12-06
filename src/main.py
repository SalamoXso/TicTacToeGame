import game_logic
import game_ui

def main():
    print("Welcome to Tic Tac Toe Game!")

    # Create instances of the GameUI and TicTacToeGameLogic classes
    game = game_logic.TicTacToeGameLogic()
    ui = game_ui.GameUI()

    # Initialize the game (reset board and set player to 'X')
    game.reset_game()

    while not game.check_winner() and not game.is_board_full():
        ui.draw_board()  # Display the board state after each turn
        current_player = game.get_current_player()
        print(f"It's {current_player}'s turn.")

        # Get and validate player input
        position = game_ui.get_player_input()
        while not game.make_move(position[0], position[1]):
            print("Invalid position. Please try again.")
            position = game_ui.get_player_input()

        game.toggle_player()  # Switch to the next player

    ui.draw_board()  # Display the final board after the game ends
    if game.check_winner():
        print(f"Congratulations! {game.get_current_player()} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
