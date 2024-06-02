# Dataset Overview
The provided dataset encompasses around 2000 rows of data, with a notable partition wherein half of the entries incorporate both descriptive information and accompanying plantUML code, while the remaining half solely contains textual descriptions devoid of any UML code.

# Repository Solutions
In response to the dataset's unique characteristics, the repository hosts two distinct solutions tailored to handle the varied data formats effectively.

## Solution 1
This solution is devised to address the first half of the dataset, which includes both textual descriptions and plantUML code. It involves training a Large Language Model (LLM) using this subset of the data, specifically employing GPT-Neo, and subsequently utilizing the same LLM model to implement both backend and frontend services. The training process for the GPT-Neo model is documented in the accompanying "sol1_plantUML_generation.ipynb" file.

## Solution 2
Contrary to Solution 1, this approach considers the entire dataset, excluding the plantUML code present in the entries, for training the Language Model. Similar to Solution 1, the trained GPT-Neo model is employed to develop backend and frontend services for efficient data processing and analysis. The training procedure for the GPT-Neo model is elaborated upon in the corresponding "sol2_plantUML_generation.ipynb" file.

# Implementation Steps
Both solutions are accompanied by specific steps to execute the code effectively:

- **To Run Backend Code:** Navigate to the backend directory and execute the command "uvicorn main --reload" on the terminal.
- **To Run Frontend Code:** Move to the frontend directory and execute the command "npm run dev" to initiate the frontend service.

# Implementation Objective
Both solutions are implemented with the primary objective of comprehensively understanding and effectively processing the distinct formats present within the dataset. By leveraging appropriate analytical strategies, meaningful insights can be derived to inform decision-making processes and optimize operational efficiencies.

# Huggingface links
Model: [GPT-Neo 125M](https://huggingface.co/EleutherAI/gpt-neo-125m)

Use uploaded weights on huggingface,

[Solution 1](https://huggingface.co/rash24ar/gpt-neo-plantuml_sol1)

[Solution 2](https://huggingface.co/rash24ar/gpt-neo-plantuml)

# Frontend Screenshots

![alt text](https://github.com/rashmi-ar/coding_exercises/blob/main/Screenshots/frontend.png)

![alt text](https://github.com/rashmi-ar/coding_exercises/blob/main/Screenshots/front_end_2.png)
