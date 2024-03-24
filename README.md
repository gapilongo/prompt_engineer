# LangChain Prompt Examples

This repository contains examples of using the LangChain library with OpenAI's API to create various natural language processing prompts. The examples demonstrate how to set up and invoke different types of prompts using the LangChain and OpenAI integration.

## Overview

- `prompt1.py`: Explains basic concepts in software engineering in a simple way.
- `prompt2.py`: Translates sentences into a specified target language.
- `prompt3.py`: Finds antonyms of given words using few-shot learning.

## Setup

1. Clone this repository.
2. Install Python and the necessary libraries:
   `pip install langchain_openai`
3. Set the OpenAI API key as an environment variable:
   `export OPENAI_API_KEY='your_api_key_here'`

## Usage

Execute the scripts with Python, for example:
`python prompt1.py`

## Script Details

- `prompt1.py`: Uses a `PromptTemplate` with `LLMChain` to generate explanations on software engineering topics.
- `prompt2.py`: Uses a `PromptTemplate` for sentence translation, leveraging `LLMChain`.
- `prompt3.py`: Employs `FewShotPromptTemplate` with `LLMChain` to generate antonyms based on examples.

## Contributing

Contributions are welcome. Please fork the repository and submit pull requests.
