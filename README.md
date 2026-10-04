# 🤖 AI Agent Battle — Tic-Tac-Toe

> **B.Tech 5th Semester — Artificial Intelligence / Machine Learning Laboratory**

A Python-based **AI Agent Battle Arena** where two intelligent Tic-Tac-Toe agents play against each other using **Minimax, Alpha-Beta Pruning, configurable search depth, and heuristic evaluation**.

---

## 📌 Project Overview

This project implements an autonomous Tic-Tac-Toe environment in which two AI agents play against each other without human intervention.

The project focuses on studying:

- Minimax decision-making
- Alpha-Beta pruning
- Heuristic evaluation
- Search depth
- Number of nodes evaluated
- Number of nodes pruned
- Execution time
- AI-vs-AI performance

Two agents, **NOVA** and **PULSE**, use the same Minimax + Alpha-Beta framework but use different heuristic evaluation strategies.

---

## 🎯 Objectives

The main objectives of this project are:

- Implement a complete Tic-Tac-Toe game engine.
- Implement the Minimax algorithm.
- Implement Alpha-Beta pruning.
- Implement heuristic evaluation functions.
- Make search depth configurable.
- Create two meaningful AI agents.
- Run automatic AI-vs-AI matches.
- Compare different search depths.
- Record computational statistics.
- Store experimental results in CSV files.
- Analyze the effect of search depth and heuristic evaluation.

---

## 🗂️ Project Structure

```text
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
    ├── main_output.png
    ├── depth_experiment.png
    └── battle_results.png
📄 File Description
File / Folder	Description
main.py	Main entry point of the project
game.py	Implements the Tic-Tac-Toe board and game rules
minimax.py	Implements Minimax with Alpha-Beta pruning
heuristic.py	Contains the heuristic evaluation functions
agents.py	Defines the AI agents
experiment.py	Runs experiments and stores statistics
results/	Contains generated CSV result files
screenshots/	Contains screenshots of actual experimental output
REPORT.md	Detailed experimental analysis
🧠 AI Agents
🔵 NOVA

NOVA is the first AI agent.

Property	Value
Algorithm	Minimax
Optimization	Alpha-Beta Pruning
Heuristic	Heuristic 1
Search Depth	3
Heuristic 1

Heuristic 1 evaluates the board using:

Winning lines
Possible winning opportunities
Opponent threats
Potential winning positions

The heuristic assigns higher scores to positions favorable to the AI and lower scores to positions favorable to the opponent.

🟢 PULSE

PULSE is the second AI agent.

Property	Value
Algorithm	Minimax
Optimization	Alpha-Beta Pruning
Heuristic	Heuristic 2
Search Depth	3
Heuristic 2

Heuristic 2 evaluates the board using winning-line evaluation and additionally considers:

Center control
Corner control
Potential winning positions
Opponent threats

The two agents therefore use different evaluation strategies while using the same basic search framework.

🔍 Minimax Algorithm

Minimax is used to select the best possible move by exploring future game states.

The AI considers itself as the maximizing player and the opponent as the minimizing player.

The search continues until:

A terminal game state is reached, or
The configured search depth is reached.

The heuristic function is then used to evaluate non-terminal positions.

✂️ Alpha-Beta Pruning

Alpha-Beta pruning is used to improve Minimax efficiency.

It removes branches of the search tree that cannot affect the final decision.

The program records:

Nodes evaluated
Nodes pruned
Execution time

This makes it possible to study the computational cost of the AI search.

🧪 Experiment 1 — Search Depth

The first experiment studies the effect of changing the search depth.

The game, algorithm, and heuristic are kept fixed, while only the search depth is changed.

The tested depths are:

Depth 1, Depth 2, Depth 3, and Depth 4

The experiment records:

Result
Nodes evaluated
Nodes pruned
Execution time
📊 Search Depth Results
Search Depth	Result	Nodes Evaluated	Nodes Pruned	Execution Time
1	Draw	25	0	0.000118 s
2	Draw	65	16	0.000334 s
3	Draw	251	51	0.000982 s
4	Draw	653	231	0.002727 s
🔎 Observation

All four depth experiments resulted in a draw.

However, the computational cost increased as the search depth increased.

Nodes Evaluated
Depth 1 → 25 nodes
Depth 2 → 65 nodes
Depth 3 → 251 nodes
Depth 4 → 653 nodes

The number of evaluated nodes increased significantly with deeper search.

Execution Time
Depth 1 → 0.000118 s
Depth 2 → 0.000334 s
Depth 3 → 0.000982 s
Depth 4 → 0.002727 s

The execution time also increased as the search depth increased.

Alpha-Beta Pruning
Depth 1 → 0 nodes pruned
Depth 2 → 16 nodes pruned
Depth 3 → 51 nodes pruned
Depth 4 → 231 nodes pruned

The number of pruned nodes increased at deeper search levels.

Conclusion of Experiment 1

The experiment shows that deeper search increases computational cost because the AI examines more possible future game states.

In this particular experiment, increasing the depth from 1 to 4 did not change the final result, because all four experiments ended in a draw.

⚔️ Experiment 2 — AI Agent Battle

The second experiment consists of 10 automatic AI-vs-AI games between NOVA and PULSE.

Both agents use:

Minimax
Alpha-Beta pruning
Search depth 3

To reduce first-player bias, the starting player is alternated between the two agents.

Starting Player Pattern
Game 1  → NOVA
Game 2  → PULSE
Game 3  → NOVA
Game 4  → PULSE
Game 5  → NOVA
Game 6  → PULSE
Game 7  → NOVA
Game 8  → PULSE
Game 9  → NOVA
Game 10 → PULSE
📊 10-Game Battle Results
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
🏆 Final Battle Summary
Result	Count
🟦 NOVA Wins	0
🟩 PULSE Wins	0
🤝 Draws	10
🎮 Total Games	10
Result

Both agents produced a draw in every game.

Therefore, this experiment did not show a winning advantage for either NOVA or PULSE.

📈 Overall Observations
1. Effect of Search Depth

Increasing the search depth resulted in more nodes being evaluated.

25 → 65 → 251 → 653

This shows that deeper search requires the AI to explore a larger search tree.

2. Effect on Execution Time

Execution time increased as search depth increased.

0.000118 s → 0.000334 s → 0.000982 s → 0.002727 s

Therefore, deeper search required more computational time.

3. Alpha-Beta Pruning

Alpha-Beta pruning eliminated branches that did not need to be explored.

The number of pruned nodes increased from:

0 at Depth 1

to:

231 at Depth 4
4. Different Heuristics

NOVA and PULSE use different heuristic evaluation functions.

This allows the project to compare how different board evaluations behave within the same Minimax + Alpha-Beta framework.

5. First-Player Advantage

Each agent started exactly five games.

All ten games were draws.

Therefore, no clear first-player advantage appeared in this experiment.

📝 Conclusion

This project demonstrates the implementation of an autonomous Tic-Tac-Toe AI system using Minimax, Alpha-Beta pruning, configurable search depth, and heuristic evaluation.

The search-depth experiment showed that increasing the depth increased the number of evaluated nodes and execution time. Alpha-Beta pruning also removed a significant number of unnecessary search branches at deeper depths.

In the 10-game AI battle, both NOVA and PULSE produced draws in all games.

Therefore, the experiment did not establish that one agent was superior to the other. Instead, it demonstrated the relationship between search depth, computational cost, heuristic evaluation, and AI decision-making.

All conclusions in this README are based on the actual experimental results generated by the program.