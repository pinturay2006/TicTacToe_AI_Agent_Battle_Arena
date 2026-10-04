class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9

    def reset(self):
        self.board = [" "] * 9

    def display(self):
        print()

        for row in range(3):
            i = row * 3

            print(
                f" {self.board[i]} | "
                f"{self.board[i + 1]} | "
                f"{self.board[i + 2]} "
            )

            if row < 2:
                print("---+---+---")

        print()

    def get_valid_moves(self):
        return [
            i for i, cell in enumerate(self.board)
            if cell == " "
        ]

    def make_move(self, position, player):
        if position in self.get_valid_moves():
            self.board[position] = player
            return True

        return False

    def check_winner(self):
        winning_lines = (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        )

        for a, b, c in winning_lines:
            if (
                self.board[a] != " "
                and self.board[a] == self.board[b]
                and self.board[b] == self.board[c]
            ):
                return self.board[a]

        return None

    def is_draw(self):
        return (
            self.check_winner() is None
            and not self.get_valid_moves()
        )

    def is_terminal(self):
        return (
            self.check_winner() is not None
            or self.is_draw()
        )