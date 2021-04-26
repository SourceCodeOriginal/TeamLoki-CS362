class Board:
    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def __str__(self):#For position of numbers in the board
        return("\n 0 | 1 | 2     %s | %s | %s\n"
               " 3 | 4 | 5     %s | %s | %s\n"
               " 6 | 7 | 8     %s | %s | %s" % (self.board[0], self.board[1], self.board[2],
                                                self.board[3], self.board[4], self.board[5],
                                                self.board[6], self.board[7], self.board[8]))

    def valid_move(self, move):
        try:
            move = int(move)
        except ValueError:
            return False
        if 0 <= move <= 8 and self.board[move] == ' ':
            return True
        return False

    def winning(self):
        return ((self.board[0] != ' ' and
                 ((self.board[0] == self.board[1] == self.board[2]) or
                  (self.board[0] == self.board[3] == self.board[6]) or
                  (self.board[0] == self.board[4] == self.board[8])))
                or (self.board[4] != ' ' and
                    ((self.board[1] == self.board[4] == self.board[7]) or
                     (self.board[3] == self.board[4] == self.board[5]) or
                     (self.board[2] == self.board[4] == self.board[6])))
                or (self.board[8] != ' ' and
                    ((self.board[2] == self.board[5] == self.board[8]) or
                     (self.board[6] == self.board[7] == self.board[8]))))

    def draw(self):
        return all((x != ' ' for x in self.board))

    def play_move(self, position, marker):
        self.board[position] = marker

    def board_string(self):
        return ''.join(self.board)