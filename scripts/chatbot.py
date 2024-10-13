import json
import random
import os
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from learning import learn_from_feedback, choose_best_response
from optimization import find_optimal_solution

# Load GPT-2 model and tokenizer once at the start
model_name = "gpt2"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = GPT2LMHeadModel.from_pretrained(model_name).to(device)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Load feedback memory
if os.path.exists('data/feedback_memory.json'):
    with open('data/feedback_memory.json', 'r') as f:
        feedback_memory = json.load(f)
else:
    feedback_memory = {}

# Chatbot class with self-learning and optimization capabilities
class AIPoweredChatbot:
    def __init__(self):
        self.learning_rate = 0.1  # How fast the bot learns from feedback

    def ai_response(self, user_input):
        inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt").to(device)
        
        with torch.no_grad():
            outputs = model.generate(
                inputs, 
                max_length=100, 
                pad_token_id=tokenizer.eos_token_id,
                num_return_sequences=1,
                temperature=0.7
            )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response.strip()

    def chatbot(self):
        print("Hi! I am your self-learning AI-powered chatbot. Type 'quit' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "quit":
                print("Bot: Goodbye! Have a nice day!")
                break

            # Check if feedback exists and choose the best response
            response = choose_best_response(user_input, feedback_memory)
            if response:
                print(f"Bot: {response}")
            else:
                # Fall back to AI for complex questions
                response = self.ai_response(user_input)
                print(f"Bot: {response}")
            
            # Ask for feedback
            feedback = input("Was this answer helpful? (yes/no): ")
            learn_from_feedback(user_input, response, feedback, feedback_memory)

            # Optional: Save feedback memory to file after each interaction
            with open('data/feedback_memory.json', 'w') as f:
                json.dump(feedback_memory, f, indent=4)

            # Example of an optimization query
            if "find optimal solution" in user_input:
                print(f"Bot: {find_optimal_solution(user_input)}")

# Initialize and start the chatbot
if __name__ == "__main__":
    ai_chatbot = AIPoweredChatbot()
    ai_chatbot.chatbot()
