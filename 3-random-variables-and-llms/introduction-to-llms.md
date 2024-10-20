# Part 1: Introduction to Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG)

Lecture Date:: 2024-10-02

Instructors:: Marco Lehmann

Course:: AI Foundations

Week:: 3

## Learning Objectives:

- Provide a high-level understanding of how LLMs, such as _ChatGPT_, function.
- Introduce the concept of **Retrieval-Augmented Generation (RAG)** and how it extends LLM capabilities by accessing external data sources.

## Key Topics Covered:

1. What are large language models (LLMs)?
   - LLMs are massive neural networks based on the Transformer architecture, introduced in 2017. They have up to trillions of parameters, enabling them to generate and understand human-like text.
   - **Example**: The Mistral 7B model has 7 billion parameters, a much smaller size compared to competitors but still significant.
2. How Do LLMs Generate Text?
   - **Sequential Generation**: LLMs generate output word-by-word (or token-by-token) by predicting the next word based on prior words.
   - **Auto-regressive Process**: The model takes the generated text so far as context for predicting the next word.
   - The output is sampled from a probability distribution over possible next tokens, making the result plausible but not necessarily factually correct.
3. Where Is LLM Knowledge Stored?
   - The knowledge is encoded in the model's weights, not stored as explicit data. LLMs generalize knowledge learned during training and apply it to new inputs.
4. Retrieval-Augmented Generation (RAG)
   - **RAG** enhances LLMs by allowing them to retrieve external information (such as private data or up-to-date content) when generating responses.

- Useful for applications where up-to-date or domain-specific knowledge is needed, but the LLM was trained without access to that information.

5. Agents vs. GPTs
   - **Agents**: Designed to be integrated into applications using APIs and can perform actions (e.g., API calls, generating Python code).
   - **GPTs**: Self-contained models deployed on platforms like OpenAI, which can process inputs and perform specific tasks based on predefined instructions.

## Practical Applications:

- **Prompt Engineering**: Modifying the structure of prompts can enhance LLM outputs, making them more specific or factually correct.
- **Semantic Data Extraction**: An example of a GPT that extracts dates from certificates, generates Python code, runs OCR, and outputs JSON data.

## Resources

- [OpenAI Platform Documentation on GPTs](https://platform.openai.com/docs/assistants/overview)
- [Best Practices in Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering/six-strategies-for-getting-better-results)
