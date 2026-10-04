AI Agent Battle — Tic-Tac-Toe
1. Introduction

This project implements an AI-based Tic-Tac-Toe system in Python.

The system contains two AI agents, NOVA and PULSE, that play Tic-Tac-Toe against each other without human intervention. Both agents use Minimax with Alpha-Beta pruning, but they use different heuristic evaluation strategies.

The main purpose of the project is to investigate the effect of search depth, heuristic evaluation, and computational cost on AI decision-making.

2. Objectives

The main objectives of this project are:

Implement a Tic-Tac-Toe game engine.
Implement the Minimax algorithm.
Implement Alpha-Beta pruning.
Implement heuristic evaluation functions.
Make the search depth configurable.
Create two meaningful AI agents.
Run automatic AI-vs-AI matches.
Perform a search-depth experiment.
Record nodes evaluated, nodes pruned, and execution time.
Save experimental results to CSV files.
Analyze the behavior and computational cost of the agents.
3. Project Structure
TicTacToe_AI_Agent_Battle_Arena/
│
├── main.py
├── game.py
├── minimax.py
├── heuristic.py
├── agents.py
├── experiment.py
├── README.md
├── REPORT.md
│
├── results/
│   ├── depth_experiment.csv
│   └── battle_results.csv
│
└── screenshots/
File Responsibilities
game.py — Tic-Tac-Toe board and game rules.
minimax.py — Minimax search with Alpha-Beta pruning.
heuristic.py — Heuristic evaluation functions.
agents.py — AI Agent class and the two AI agents.
experiment.py — Runs the experiments, collects statistics, and saves CSV results.
main.py — Program entry point.
results/ — Stores experimental results.
screenshots/ — Stores screenshots of program output and experimental results.
4. AI Agents
Agent 1 — NOVA
Algorithm: Minimax + Alpha-Beta pruning
Heuristic: Heuristic 1
Search depth: 3
Agent 2 — PULSE
Algorithm: Minimax + Alpha-Beta pruning
Heuristic: Heuristic 2
Search depth: 3

Both agents use meaningful heuristic functions. Neither agent is deliberately made weak or random.

5. Heuristics
Heuristic 1

Heuristic 1 evaluates a board using winning lines, possible winning opportunities, and opponent threats.

It gives a higher score to positions that are favorable for the AI and a lower score to positions that favor the opponent.

Heuristic 2

Heuristic 2 uses winning-line evaluation and additionally considers center and corner control.

The two heuristics allow the behavior of two otherwise similar AI agents to be compared.

6. Minimax and Alpha-Beta Pruning

The agents use the Minimax algorithm to explore possible future moves.

The maximizing player tries to maximize the board score, while the minimizing player tries to minimize it.

Alpha-Beta pruning removes branches that cannot affect the final Minimax decision.

The program records:

Nodes evaluated
Nodes pruned
Execution time

This allows the computational cost of different search depths and agents to be compared.

7. Experiment 1 — Search Depth

The first experiment investigates the effect of search depth.

The game, algorithm, and heuristic are kept fixed while the search depth is changed.

The tested search depths are:

Depth 1
Depth 2
Depth 3
Depth 4

The following values were recorded:

Depth	Result	Nodes Evaluated	Nodes Pruned	Execution Time (s)
1	Draw	25	0	0.000118
2	Draw	65	16	0.000334
3	Draw	251	51	0.000982
4	Draw	653	231	0.002727
Observation

All four depth experiments resulted in a draw.

However, increasing the search depth increased the number of nodes evaluated:

Depth 1: 25
Depth 2: 65
Depth 3: 251
Depth 4: 653

The execution time also increased as the depth increased.

The number of pruned nodes increased from 0 at depth 1 to 231 at depth 4, showing that Alpha-Beta pruning eliminated unnecessary branches during deeper searches.

The experiment shows that deeper search increases computational cost. In this particular experiment, deeper search did not change the final game result because every tested game ended in a draw.

8. Experiment 2 — AI Agent Battle

NOVA and PULSE played 10 AI-vs-AI games.

Both agents used:

Minimax
Alpha-Beta pruning
Search depth 3

The starting player was alternated between the two agents to reduce first-player bias.

Battle Results
Game	First Player	Winner	Moves	NOVA Nodes	PULSE Nodes	NOVA Pruned	PULSE Pruned
1	NOVA	Draw	9	251	179	51	38
2	PULSE	Draw	9	178	255	38	52
3	NOVA	Draw	9	251	179	51	38
4	PULSE	Draw	9	178	255	38	52
5	NOVA	Draw	9	251	179	51	38
6	PULSE	Draw	9	178	255	38	52
7	NOVA	Draw	9	251	179	51	38
8	PULSE	Draw	9	178	255	38	52
9	NOVA	Draw	9	251	179	51	38
10	PULSE	Draw	9	178	255	38	52
Final Result
NOVA wins: 0
PULSE wins: 0
Draws: 10
9. Conclusion

The experiments demonstrate the effect of search depth and heuristic evaluation in a Minimax-based Tic-Tac-Toe AI.

Increasing search depth resulted in more nodes being evaluated and greater execution time. Alpha-Beta pruning also pruned more nodes at deeper search levels.

In the 10-game AI battle, both agents produced draws in every game. Therefore, this experiment did not show a winning advantage for either heuristic.

The results demonstrate that deeper search increases computational cost, while the final game result depends on the game state, search depth, and heuristic evaluation.

The conclusions are based on the actual experimental results generated by the program.