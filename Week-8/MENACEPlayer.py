class MenacePlayer:
    def __init__(self):
        self.matchboxes = {}
        self.win = 0
        self.draw = 0
        self.lose = 0

    def start_game(self):
        self.moves_played = []

    def get_move(self, board):
        board = board.board_string()
        if board not in self.matchboxes:
            new_beads = [pos for pos, mark in enumerate(board) if mark == ' ']
            self.matchboxes[board] = new_beads * ((len(new_beads) + 2) // 2)

        beads = self.matchboxes[board]
        if len(beads):
            bead = random.choice(beads)
            self.moves_played.append((board, bead))
        else:
            bead = -1
        return bead

    def win_game(self):
        for (board, bead) in self.moves_played:
            self.matchboxes[board].extend([bead, bead, bead])
        self.win += 1
    def lose_game(self):
        for (board, bead) in self.moves_played:
            matchbox = self.matchboxes[board]
            del matchbox[matchbox.index(bead)]
        self.lose += 1
    def draw_game(self):
        for (board, bead) in self.moves_played:
            self.matchboxes[board].append(bead)
        self.draw += 1
