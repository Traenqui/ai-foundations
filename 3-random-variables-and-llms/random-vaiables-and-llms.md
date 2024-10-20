# Part 2: Random Variables

Lecture Date:: 2024-10-02

Instructors:: Marco Lehmann

Course:: AI Foundations

Week:: 3

## Learning Objectives:

- Introduce the key concepts in statistics needed to understand statistical machine learning.
- Cover the basic principles of **random variables**, **joint probabilities** and **Bayes' Rule**
- Apply these concepts to practical machine learning problems, both in theory and using `Python`

## Key Concepts Covered:

1. What is a random variable?
   - A random variable is a numerical value assigned to outcomes of a random experiment.
   - **Discrete** random variables take specific, countable values, while **continuous** random variables can take any value within a range.
2. **Probability Mass Function (PMF)**
   - PMF is a function that gives the probability for each value a discrete random variable can take.
   - Example: For rolling a die, the PMF assigns each number (1 to 6) a probability of $\frac{1}{6}$
3. **Joint Probability**
   - The probability of two events happening at the same time
   - If the events are independent (e.g. the roll of two dice), the joint probability is the product of their individual probabilities: $P(X,Y) = P(X) * P(Y)$
4. **Conditional Probability**
   - The probability of one event given that another event has occurred.
   - Denoted as $P(X|Y)$, where $Y$ happens given $X$ is known
5. **Marginal Probability**
   - This is derived by summing the joint probabilities over one variable, giving the probability of the other variable independently.
6. **Bayes' Rule**
   - Related conditional probabilities and helps in updating beliefs based on new evidence:
     $$P(X|Y)=\frac{P(Y|X) * P(X)}{P(Y)}$$
   - Useful for reasoning under uncertainty in AI applications, such as spam filtering or classification tasks.

## Practical Examples:

- **Dice Roll**: Understanding discrete probability distributed through dice rolling
- **Dependent Variables**: Modeling real-world events, like the correlation between observing clouds and predicting rain, using joint probabilities.
