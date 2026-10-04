import csv
import os
import time

from agents import Agent, create_agents
from game import TicTacToe
from heuristic import heuristic_one, heuristic_two


class Experiment:
    def __init__(self, results_dir="results"):
        self.results_dir = results_dir

        os.makedirs(
            self.results_dir,
            exist_ok=True
        )

    def run_single_game(
        self,
        first_agent,
        second_agent,
        game_number=1
    ):
        game = TicTacToe()

        first_agent.reset_stats()
        second_agent.reset_stats()

        symbols = {
            first_agent.name: "X",
            second_agent.name: "O"
        }

        current_agent = first_agent
        moves = 0

        start_time = time.perf_counter()

        while not game.is_terminal():

            symbol = symbols[current_agent.name]

            move = current_agent.choose_move(
                game.board,
                symbol
            )

            if move is None:
                break

            game.make_move(
                move,
                symbol
            )

            moves += 1

            if current_agent is first_agent:
                current_agent = second_agent
            else:
                current_agent = first_agent

        total_time = (
            time.perf_counter() - start_time
        )

        winner_symbol = game.check_winner()

        if winner_symbol == symbols[first_agent.name]:
            winner = first_agent.name

        elif winner_symbol == symbols[second_agent.name]:
            winner = second_agent.name

        else:
            winner = "Draw"

        stats = {
            first_agent.name: {
                "nodes": first_agent.nodes_evaluated,
                "pruned": first_agent.nodes_pruned,
                "time": first_agent.execution_time
            },

            second_agent.name: {
                "nodes": second_agent.nodes_evaluated,
                "pruned": second_agent.nodes_pruned,
                "time": second_agent.execution_time
            }
        }

        return {
            "game": game_number,
            "first_player": first_agent.name,
            "winner": winner,
            "moves": moves,

            "NOVA_nodes": stats["NOVA"]["nodes"],
            "NOVA_pruned": stats["NOVA"]["pruned"],
            "NOVA_time": round(
                stats["NOVA"]["time"],
                6
            ),

            "PULSE_nodes": stats["PULSE"]["nodes"],
            "PULSE_pruned": stats["PULSE"]["pruned"],
            "PULSE_time": round(
                stats["PULSE"]["time"],
                6
            ),

            "total_time": round(
                total_time,
                6
            )
        }

    def run_battle(self, games=10):
        agent1, agent2 = create_agents()

        results = []

        for game_number in range(1, games + 1):

            # Odd games:
            # NOVA starts.
            #
            # Even games:
            # PULSE starts.
            if game_number % 2 == 1:
                first = agent1
                second = agent2
            else:
                first = agent2
                second = agent1

            result = self.run_single_game(
                first,
                second,
                game_number
            )

            results.append(result)

        path = os.path.join(
            self.results_dir,
            "battle_results.csv"
        )

        with open(
            path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=results[0].keys()
            )

            writer.writeheader()
            writer.writerows(results)

        return results

    def run_depth_experiment(self):
        results = []

        # PULSE remains fixed.
        # Only NOVA's search depth changes.
        fixed_opponent = Agent(
            "PULSE",
            3,
            heuristic_two
        )

        for depth in (1, 2, 3, 4):

            tested_agent = Agent(
                "NOVA",
                depth,
                heuristic_one
            )

            result = self.run_single_game(
                tested_agent,
                fixed_opponent,
                game_number=depth
            )

            results.append({
                "depth": depth,
                "result": result["winner"],
                "nodes_evaluated": result["NOVA_nodes"],
                "nodes_pruned": result["NOVA_pruned"],
                "execution_time": result["NOVA_time"]
            })

        path = os.path.join(
            self.results_dir,
            "depth_experiment.csv"
        )

        with open(
            path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "depth",
                    "result",
                    "nodes_evaluated",
                    "nodes_pruned",
                    "execution_time"
                ]
            )

            writer.writeheader()
            writer.writerows(results)

        return results

    @staticmethod
    def print_depth_results(results):
        print()
        print("=== SEARCH DEPTH EXPERIMENT ===")

        print(
            f"{'Depth':<8}"
            f"{'Result':<12}"
            f"{'Nodes':<12}"
            f"{'Pruned':<12}"
            f"{'Time (s)':<12}"
        )

        print("-" * 56)

        for row in results:
            print(
                f"{row['depth']:<8}"
                f"{row['result']:<12}"
                f"{row['nodes_evaluated']:<12}"
                f"{row['nodes_pruned']:<12}"
                f"{row['execution_time']:<12.6f}"
            )

    @staticmethod
    def print_battle_results(results):
        print()
        print("=== 10-GAME AI BATTLE ===")

        print(
            f"{'Game':<7}"
            f"{'First':<10}"
            f"{'Winner':<10}"
            f"{'Moves':<8}"
            f"{'NOVA Nodes':<13}"
            f"{'PULSE Nodes':<13}"
        )

        print("-" * 70)

        for row in results:
            print(
                f"{row['game']:<7}"
                f"{row['first_player']:<10}"
                f"{row['winner']:<10}"
                f"{row['moves']:<8}"
                f"{row['NOVA_nodes']:<13}"
                f"{row['PULSE_nodes']:<13}"
            )

        nova_wins = sum(
            row["winner"] == "NOVA"
            for row in results
        )

        pulse_wins = sum(
            row["winner"] == "PULSE"
            for row in results
        )

        draws = sum(
            row["winner"] == "Draw"
            for row in results
        )

        print()
        print("Summary:")
        print(f"NOVA wins : {nova_wins}")
        print(f"PULSE wins: {pulse_wins}")
        print(f"Draws     : {draws}")