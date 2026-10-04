from experiment import Experiment


def main():
    print("Starting Tic-Tac-Toe AI experiments...")

    experiment = Experiment()

    # Experiment 1:
    # Search depth = 1, 2, 3, 4
    depth_results = (
        experiment.run_depth_experiment()
    )

    experiment.print_depth_results(
        depth_results
    )

    # Experiment 2:
    # 10 AI vs AI games
    battle_results = (
        experiment.run_battle(games=10)
    )

    experiment.print_battle_results(
        battle_results
    )

    print()
    print("Results saved in the 'results' folder.")
    print(" - results/depth_experiment.csv")
    print(" - results/battle_results.csv")


if __name__ == "__main__":
    main()