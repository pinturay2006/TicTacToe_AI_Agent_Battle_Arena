class Minimax:
    def __init__(self, heuristic, max_depth):
        self.heuristic = heuristic
        self.max_depth = max_depth

        self.nodes_evaluated = 0
        self.nodes_pruned = 0

    def reset_stats(self):
        self.nodes_evaluated = 0
        self.nodes_pruned = 0

    @staticmethod
    def _winner(board):
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
                board[a] != " "
                and board[a] == board[b]
                and board[b] == board[c]
            ):
                return board[a]

        return None

    @staticmethod
    def _draw(board):
        return all(cell != " " for cell in board)

    def _terminal_score(
        self,
        board,
        root_player,
        opponent,
        depth_remaining
    ):
        winner = self._winner(board)

        if winner == root_player:
            return 1000 + depth_remaining

        if winner == opponent:
            return -1000 - depth_remaining

        if self._draw(board):
            return 0

        return None

    def _search(
        self,
        board,
        current_player,
        root_player,
        opponent,
        depth_remaining,
        alpha,
        beta
    ):
        terminal_score = self._terminal_score(
            board,
            root_player,
            opponent,
            depth_remaining
        )

        if terminal_score is not None:
            self.nodes_evaluated += 1
            return terminal_score

        if depth_remaining == 0:
            self.nodes_evaluated += 1

            return self.heuristic(
                board,
                root_player,
                opponent
            )

        valid_moves = [
            i for i, cell in enumerate(board)
            if cell == " "
        ]

        maximizing = current_player == root_player

        if maximizing:
            best_value = float("-inf")

            for move in valid_moves:
                board[move] = current_player

                value = self._search(
                    board,
                    opponent,
                    root_player,
                    opponent,
                    depth_remaining - 1,
                    alpha,
                    beta
                )

                board[move] = " "

                best_value = max(best_value, value)
                alpha = max(alpha, best_value)

                if beta <= alpha:
                    self.nodes_pruned += 1
                    break

            return best_value

        else:
            best_value = float("inf")

            for move in valid_moves:
                board[move] = current_player

                value = self._search(
                    board,
                    root_player,
                    root_player,
                    opponent,
                    depth_remaining - 1,
                    alpha,
                    beta
                )

                board[move] = " "

                best_value = min(best_value, value)
                beta = min(beta, best_value)

                if beta <= alpha:
                    self.nodes_pruned += 1
                    break

            return best_value

    def choose_move(self, board, player):
        self.reset_stats()

        valid_moves = [
            i for i, cell in enumerate(board)
            if cell == " "
        ]

        if not valid_moves:
            return None

        opponent = "O" if player == "X" else "X"

        best_move = valid_moves[0]
        best_value = float("-inf")

        alpha = float("-inf")
        beta = float("inf")

        for move in valid_moves:
            board[move] = player

            value = self._search(
                board,
                opponent,
                player,
                opponent,
                max(0, self.max_depth - 1),
                alpha,
                beta
            )

            board[move] = " "

            if value > best_value:
                best_value = value
                best_move = move

            alpha = max(alpha, best_value)

        return best_move