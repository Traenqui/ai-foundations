# Tree Diagrams Of Sequential Events

Lecture Date:: 2024-10-09

Instructors:: Marco Lehmann

Course:: AI Foundations

Week:: 4

## Learning Objectives:

Many real-world situations can be modeled as sequences of random events (multi-step experiments). Examples include:

- Selecting a random card from one of two decks after randomly choosing a deck.
- Deciding where to eat using a coin flip, followed by rolling a dice to choose a menu item.

These scenarios, known as **multi-step experiments**, are common and involve applying basic rules of probability. The goal is to:

- Learn how to visualize these experiments using **Tree Diagrams**.
- Understand the probability rules behind such sequences of events, especially in **two-step experiments** (German: _zweistufiges Zufallsexperiment_).
- Develop a method to **model the generative process** of random outcomes, linking domain knowledge with data. This leads to the broader concept of **Generative Models** in probability and AI.

## Visualization with Tree Diagrams

Tree diagrams help us:

- Visualize how data is generated in a probabilistic setting.
- Understand relationships between random variables.

## Example Problem

You are given three coins with different probabilities of showing heads:

- Red Coin: $P(Head) = 0.5$
- Blue Coin: $P(Head) = 0.7$
- Green Coin: $P(Head) = 0.1$

You randomly select one coin and toss it. What is the probability of getting heads?  
Using the tree diagram approach, we can visualize and calculate each path's outcome probability.

```mermaid
graph TD
    A[Pick a coin] --> B[Red Coin]
    A --> C[Blue Coin]
    A --> D[Green Coin]
    B --> B1[Head: 0.5]
    B --> B2[Tail: 0.5]
    C --> C1[Head: 0.7]
    C --> C2[Tail: 0.3]
    D --> D1[Head: 0.1]
    D --> D2[Tail: 0.9]

```

## Formula:

We multiply the probabilities along each branch:
$$Pr(X, Y) = Pr(X) * Pr(Y | X)$$

The final probabilities for observing heads will be summed across all paths that lead to heads.

```mermaid
graph TD
    A[Pick a coin] --> B[Red Coin]
    A --> C[Blue Coin]
    A --> D[Green Coin]
    B --> B1[Head: 0.5]:::note1
    B --> B2[Tail: 0.5]:::note1
    C --> C1[Head: 0.7]:::note2
    C --> C2[Tail: 0.3]:::note2
    D --> D1[Head: 0.1]:::note3
    D --> D2[Tail: 0.9]:::note3

    classDef note1 fill:#fff,stroke:#f66,stroke-width:2px;
    classDef note2 fill:#ff6,stroke:#333,stroke-width:2px;
    classDef note3 fill:#f9f,stroke:#333,stroke-width:2px;

    %% Annotations for calculations
    B1:::note1 --> Note1["P(Red and Head) = 1/3 × 0.5 = 1/6"]
    B2:::note1 --> Note2["P(Red and Tail) = 1/3 × 0.5 = 1/6"]
    C1:::note2 --> Note3["P(Blue and Head) = 1/3 × 0.7 = 7/30"]
    C2:::note2 --> Note4["P(Blue and Tail) = 1/3 × 0.3 = 3/30"]
    D1:::note3 --> Note5["P(Green and Head) = 1/3 × 0.1 = 1/30"]
    D2:::note3 --> Note6["P(Green and Tail) = 1/3 × 0.9 = 9/30"]
```
