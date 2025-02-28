# Training the AI

## Reinforcement Learning?

This project makes use of a machine learning approach called **Reinforcement Learning** (RL), in which an AI agent learns to make optimal decisions by interacting with its environment. The agent takes actions, receives feedback (in the form of rewards or penalties), and adjusts its strategy over time to maximise cumulative rewards.

## Q-Learning

**Q-Learning** is a type of Reinforcement Learning that follows a model-free approach, meaning the AI agent doesn't need any prior knowledge of the environment. Instead, it learns an optimal policy by exploring predefined possible actions and updating values in a **Q-table** based on the feedback it receives. These values, called **Q-values**, estimate the expected cumulative reward for taking a specific action in a given state.

## How This Applies to the Game

- The **agent**: The AI making decisions about how many coins to add to the tower.
- The **environment**: The tower itself, where:
  - The **state** represents the current height of the tower.
  - The **possible actions** represent the number of coins that can be added.
- The agent receives:
  - A **penalty** if its action causes the tower to reach or exceed the Topple Height.
  - A **reward** if its action forces the opponent into a situation where they must exceed the Topple Height on their turn.

## What the Q-Table Looks Like

The Q-table holds a Q-value for each possible state-action combination. 

For example, if the game used a **Topple Height** of `11` with a **Possible Actions** list of `1,2,3`, the Q-Table would look something like this:

| State | Action 1 | Action 2 | Action 3 |
| ----- | ----- | ----- | ----- | 
| 1 | 0.0 | -0.25 | -0.25 |
| 2 | -0.25 | -0.25 | -0.25 |
| 3 | -0.25 | -0.25 | 0.0 |
| 4 | -0.25 | 0.0 | -0.5 |
| 5 | 0.0 | -0.5 | -0.5 |
| 6 | -0.5 | -0.5 | -0.5 |
| 7 | -0.5 | -0.5 | 0.0 |
| 8 | -0.5 | 0.0 | -1.0 |
| 9 | 0.0 | -1.0 | -1.0 |
| 10 | -1.0 | -1.0 | -1.0 |

***NOTE:*** *There is no need to record values for expected future reward for states greater than or equal to the Topple Height as the game is now over*

The same Q-table can be represented with a Python `dictionary` where:
- **Key:** A `(state, action)` **tuple**
- **Value:** The **Q-value**

``` python
q_values = {
    (1,1): 0.0, 
    (1,2): -0.25,
    (1,3): -0.25,
    (2,1): -0.25,
    (2,2): -0.25,
    (2,3): -0.25,
    (3,1): -0.25,
    (3,2): -0.25,
    (3,3): 0.0,
    (4,1): -0.25,
    (4,2): 0.0,
    (4,3): -0.5,
    (5,1): 0.0,
    (5,2): -0.5,
    (5,3): -0.5,
    (6,1): -0.5,
    (6,2): -0.5,
    (6,3): -0.5,
    (7,1): -0.5,
    (7,2): -0.5,
    (7,3): 0.0,
    (8,1): -0.5,
    (8,2): 0.0,
    (8,3): -1.0,
    (9,1): 0.0,
    (9,2): -1.0,
    (9,3): -1.0,
    (10,1): -1.0,
    (10,2): -1.0,
    (10,3): -1.0
}
```

## How to Update Q-Values

There are two common approaches to updating Q-values:
