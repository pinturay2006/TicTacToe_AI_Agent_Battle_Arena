import time

from minimax import Minimax
from heuristic import heuristic_one, heuristic_two


class Agent:
    def __init__(self, name, depth, heuristic):
        self.name = name
        self.depth = depth
        self.heuristic = heuristic

        self.nodes_evaluated = 0
        self.nodes_pruned = 0
        self.execution_time = 0.0

    def reset_stats(self):
        self.nodes_evaluated = 0
        self.nodes_pruned = 0
        self.execution_time = 0.0

    def choose_move(self, board, symbol):
        start_time = time.perf_counter()

        search = Minimax(
            self.heuristic,
            self.depth
        )

        move = search.choose_move(
            board,
            symbol
        )

        self.nodes_evaluated += search.nodes_evaluated
        self.nodes_pruned += search.nodes_pruned

        self.execution_time += (
            time.perf_counter() - start_time
        )

        return move


def create_agents():
    agent1 = Agent(
        "NOVA",
        3,
        heuristic_one
    )

    agent2 = Agent(
        "PULSE",
        3,
        heuristic_two
    )

    return agent1, agent2