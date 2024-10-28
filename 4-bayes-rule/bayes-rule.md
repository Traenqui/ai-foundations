# Bayes' Rule

Lecture Date:: 2024-10-09

Instructors:: Marco Lehmann

Course:: AI Foundations

Week:: 4

## Learning Objectives:

- Understand how to visualize multi-step experiments using **Tree Diagrams**, which represent the sequence of random events.
- Learn how to use **Bayes Theorem** to invert probabilistic models, allowing us to infer hidden causes from observed outcomes.
- Apply **Bayesian reasoning** to real-world examples, such as:
  - Determining which coin was selected based on observed flips.
  - Estimating the likelihood of an airplane's approach from noisy radar signals.
  - Inferring brain activity based on observed behavior in reinforcement learning.
- Recognize the broad applications of Bayesian techniques in both science and AI, where they are used to connect data with hidden generative processes.

## Bayes' Theorem

$$P(H | E) = \frac{P(E | H) \cdot P(H)}{P(E)}$$

Where:

- **P(H | E)** is the probability of the hypothesis (H) given the evidence (E).
- **P(E | H)** is the probability of observing evidence (E) given hypothesis (H).
- **P(H)** is the prior probability of the hypothesis.
- **P(E)** is the probability of the evidence.

### Problem Context

In the 2-step experiment from Week 4, you randomly pick one coin from a set of three (Red, Blue, Green). Each coin has a different probability of showing heads or tails:

- **Red Coin**: $P(Head) = 0.5, P(Tail) = 0.5$ (fair coin).
- **Blue Coin**: $P(HEAD) = 0.7$, $P(Tail) = 0.3$ (biased towards heads)
- **Green Coin**: $P(Head) = 0.1$, $P(Tail) = 0.9$ (biased towards tails).

Now, we observe the outcome of the toss, which is tail. Our goal is to determine which coin was most likely drawn using Bayes’ Theorem.

### Step-by-Step Application of Bayes' Rule

#### Step 1: Define Hypotheses

Our hypotheses are the three possible coins that could have been drawn:

- H1: Red coin was drawn.
- H2: Blue coin was drawn.
- H3: Green coin was drawn.

#### Step 2: Known Probabilities

We know the prior probabilities $(P(H))$ for each coin being drawn. Since the coins are drawn randomly, the prior for each hypothesis is:

$$P(H1) = P(H2) = P(H3) = \frac{1}{3}$$

We also know the likelihoods $(P(E|H))$ for observing "tail" based on each hypothesis:

- $P(Tail | Red \ Coin) = 0.5$
- $P(Tail | Blue\ Coin) = 0.3$
- $P(Tail | Green\  Coin) = 0.9$

#### Step 3: Calculate the Evidence

The total probability of observing "tail" (denoted as P(E)) is computed by summing up the probabilities of "tail" for all hypotheses, weighted by their prior probabilities:

$$P(E) = P(E|H1)P(H1) + P(E|H2)P(H2) + P(E|H3)P(H3)$$

Substitute the known values:

$$P(E) = (0.5 * \frac{1}{3}) + (0.3 * \frac{1}{3}) + (0.9 * \frac{1}{3})$$

$$
P(E) = \frac{1}{6} + \frac{0.3}{3} + \frac{0.9}{3} = \frac{1}{6} + \frac{0.1}{1} + \frac{9}{30} \approx 0.4333
$$

#### Step 4: Apply Bayes' Theorem

Now we apply **Bayes’ Theorem** to calculate the posterior probabilities for each hypothesis:

- $P(H1|E) = \frac{P(E|H1) * P(H1)}{P(E)}$
- $P(H2|E) = \frac{P(E|H2) * P(H2)}{P(E)}$
- $P(H3|E) = \frac{P(E|H3) * P(H3)}{P(E)}$

Substituting the values:

- **For the Red Coin**:
  $$P(H1|E) = \frac{0.5 * \frac{1}{3}}{0.4333} \approx 0.385$$
- **For the blue Coin**:
  $$P(H2|E) = \frac{0.3 * \frac{1}{3}}{0.4333} \approx 0.231$$
- **For the Green Coin**:
  $$P(H3|E) = \frac{0.9 * \frac{1}{3}}{0.4333} \approx 0.692$$

#### Conclusion

Given that we observed "tail," the most likely coin drawn is the **Green Coin** with a probability of approximately **0.692**. This makes sense because the Green Coin is heavily biased toward tails. While it is still possible that the Red or Blue coins were drawn, the probabilities for these are significantly lower.

Bayes' Rule helps us update our initial assumptions about which coin was drawn based on the observed outcome, using both prior knowledge and the likelihood of each outcome.

## Sequential Bayesian Updates

If we observe multiple flips, we can use **sequential updates** to refine our probability estimates. Each new observation updates the prior distribution.
