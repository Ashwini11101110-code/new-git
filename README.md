# AI-Powered Self-Learning Chatbot

This project is an AI-powered chatbot with self-learning capabilities. It can learn from user interactions, improve its responses based on feedback, and also find optimal solutions using a simple optimization algorithm.

## Features
- GPT-2-based response generation for complex queries
- Self-learning mechanism: learns from user feedback to improve future interactions
- Optimization module to find the best solution for specific queries

## Setup Instructions

1. Clone this repository:
    ```
    git clone https://github.com/your-username/chatbot.git
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Run the chatbot:
    ```
    python scripts/chatbot.py
    ```

## Project Structure

- `scripts/chatbot.py`: Main chatbot script
- `scripts/learning.py`: Self-learning module
- `scripts/optimization.py`: Optimal solution finder module
- `data/`: Stores feedback memory in `feedback_memory.json`
- `models/`: (Optional) Directory to save GPT-2 fine-tuned models

## Future Improvements
- Implement reinforcement learning to make the chatbot more adaptive.
- Fine-tune the GPT-2 model for better domain-specific responses.
