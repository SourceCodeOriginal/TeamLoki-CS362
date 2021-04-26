class HumanPlayer:
    def __init__(self):
        pass

    def start_game(self):
        print("Be Ready!!!!")

    def get_move(self, board):
        while True:
            move = input('Make move : ')
            if board.valid_move(move):
                break
            print("Invalid move")
        return int(move)

    def win_game(self):
        print("WON BY YOU")

    def draw_game(self):
        print("DRAW")

    def lose_game(self):
        print("YOU LOSE")