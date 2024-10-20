# Language and Text Sequences

Lecture Date:: 2024-09-25

Instructors:: Marco Lehmann

Course:: AI Foundations

Week:: 2

## Learning Objectives:

- Understand how to turn text into machine learning-ready data.
- Learn different word representations in NLP
  1. **One-Hot Encoding**
  2. **Distributed Representations** (Distributed Semantics)
- Compare words using cosine similarity and how this plays into machine learning tasks.

## Key Concepts in Machine Learning

The lecture discusses the 4 fundamental ingredients of any machine-learning system:

1. **Data**: This is the pre-processed dataset, including cleansing, feature engineering, and augmentation.
2. **Cost Function (Loss)**: Mathematical function representing the difference between "good" and "bad" predictions (e.g., Mean Squared Error).
3. **Model**: Can range from simple linear models to complex neural networks with millions of parameters.
4. **Optimization Procedure**: Methods such as Stochastic Gradient Descent (SGD) or ADAM to minimize the cost function and improve the model.

Additionally, three more practical aspects of successful machine learning were highlighted:

5. **Performance Optimization**: Efficient pipeline-building is crucial.
6. **Visualization & Evaluation**: Monitoring training processes (e.g., using Tensorboard).
7. **Cross-Validation & Regularization**: Ensuring models generalize well to unseen data.

## Natural Language Processing (NLP)

### What is NLP?

NLP allows computers to understand and process human language. One common NLP task is **Sentiment Analysis**, where the system classifies text as positive or negative. The lecture provides an example using a binary classifier that determines the sentiment of movie reviews.

### Word Representation:

1. **One-Hot Encoding**
   - Words are represented as high-dimensional, sparse vectors, where only one element is `1`, and the rest are `0`
   - **Disadvantages**:
     - **High Dimensionality**: Each word in a large corpus like Wikipedia requires its own unique vector (e.g. 100'000 dimensions).
     - **Sparsity**: Most of the vector is zeros, which is different.
     - **No Generalization**: One-hot vectors cannot capture similarities between words (e.g. "hummus" is no closer to "chickpea" than "Zeus")
2. **Indexing**
   - Words are assigned indices in a list (dense equivalent of one-hot encoding).
   - **Limitation**: Indexing by itself does not improve meaning representation. It is often a processing step before learning embeddings.
3. **Distributed Representation (Word Embedding)**
   - Words are embedded into a continuous vector space where similar words are located closer to each other.
   - **Distributional Hypothesis**: Words that occur in similar contexts have similar meanings (J.R. Firth's principle: "You shall know a word by the company it keeps.")
   - _Example_: Algorithms like **Word2Vec** learn these representations, which enable efficient mathematical operations like dot products to compare word meanings.

## How Do Machines Understand Words?

Although machines do not "understand" words in the human sense, they can infer **semantic similarity** between words through embeddings. For example, a model trained on the phrase "I want a large coffee" might infer that "huge" is similar to "large" and make the correct inference for "I want a huge coffee".

### Cosine Similarity

- Cosine similarity is a key method used to measure the similarity between word vectors-
- It is calculated based on the dot product between vectors, with values ranging from:
  - `+1` for identical vectors
  - `0` for orthogonal (completely unrelated) vectors.
  - `-1` for opposing vectors

## Practical Applications:

1. **Sentiment Analysis**: Predict whether a sentence conveys a positive or negative sentiment based on word embeddings.
2. **Chatbots**: For example, a chatbot could infer that "large" and "huge" have similar meanings, enabling it to process requests like "I want a huge coffee" accurately.
3. **Cosine Similarity in Practice**: The class was encouraged to try out the game on [Contexto.me](https://contexto.me/), where they had to guess the target word based on similarity.

## Training Word Embeddings:

- **Pre-trained Models**: Many NLP tasks use pre-trained embeddings (e.g. from large models like `LLaMA` or `GPT`) to avoid training from scratch.
- **Custom Embeddings**: Alternatively, embeddings can be learned using frameworks like `Keras` with embedding layers optimized for the task at hand.

## Additional Resources:

- [Tensor Flow Guide](https://www.tensorflow.org/text/guide/word_embeddings)
