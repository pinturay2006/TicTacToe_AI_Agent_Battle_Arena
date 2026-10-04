WINNING_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
)


def _line_counts(board, player, opponent):
    score = 0

    for a, b, c in WINNING_LINES:
        cells = (
            board[a],
            board[b],
            board[c]
        )

        own = cells.count(player)
        enemy = cells.count(opponent)
        empty = cells.count(" ")

        # Player's possible winning lines
        if own == 3:
            score += 100
        elif own == 2 and empty == 1:
            score += 10
        elif own == 1 and empty == 2:
            score += 1

        # Opponent's possible winning lines
        if enemy == 2 and empty == 1:
            score -= 10
        elif enemy == 1 and empty == 2:
            score -= 1

    return score


def heuristic_one(board, player, opponent):
    """
    Heuristic 1:
    Evaluates winning lines and immediate threats.
    """
    return _line_counts(board, player, opponent)


def heuristic_two(board, player, opponent):
    """
    Heuristic 2:
    Uses winning-line potential plus center and corner control.
    """
    score = _line_counts(board, player, opponent)

    # Center control
    if board[4] == player:
        score += 3
    elif board[4] == opponent:
        score -= 3

    # Corner control
    corners = (0, 2, 6, 8)

    score += 2 * sum(
        board[i] == player for i in corners
    )

    score -= 2 * sum(
        board[i] == opponent for i in corners
    )

    return score