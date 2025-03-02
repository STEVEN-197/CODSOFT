# chatbot.py

import re
import random

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    
    responses = {
        r'hi|hello|hey': [
            "Hello! How's your day going?", 
            "Hey there! What can I do for you?", 
            "Hi! Need any help today?"
        ],
        r'how are you': [
            "I'm just a bot, but I'm doing great! How about you?", 
            "Feeling fantastic! What about you?", 
            "I'm running at 100% efficiency! And you?"
        ],
        r'what is your name': [
            "I'm ChatBot 2.0, your virtual assistant!", 
            "People call me ChatBot, but you can call me your AI buddy!", 
            "I'm a friendly AI designed to assist you!"
        ],
        r'bye|goodbye': [
            "Goodbye! Have an awesome day!", 
            "See you soon! Take care!", 
            "Farewell! Until next time!"
        ],
        r'help|support': [
            "Sure! I can help with basic queries. What do you need assistance with?", 
            "I'm here to help! Ask me anything.", 
            "Need help? Just type your question and I'll do my best!"
        ],
        r'what can you do': [
            "I can chat with you, answer simple questions, and keep you entertained!", 
            "I can provide basic information, assist with FAQs, and have casual conversations!", 
            "I'm here to help! Ask me anything, and I'll do my best!"
        ],
        r'who created you': [
            "I was created by Steven Malla as part of an AI project!", 
            "A brilliant mind named Steven Malla brought me to life!", 
            "I'm a result of Steven Malla's AI expertise!"
        ]
    }
    
    for pattern, response_list in responses.items():
        if re.search(pattern, user_input):
            return random.choice(response_list)
    
    return random.choice([
        "I'm not sure I understand. Can you rephrase?", 
        "Hmm... that's interesting. Tell me more!", 
        "Sorry, I didn't get that. Could you elaborate?",
        "That's a tricky one! Can you ask in a different way?"
    ])

# Running the chatbot with file input/output

def run_chatbot_from_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            user_inputs = file.readlines()
        
        responses = []
        responses.append("Chatbot: Hello! Type 'bye' to exit.")
        for user_input in user_inputs:
            user_input = user_input.strip()
            if user_input.lower() == "bye":
                responses.append("Chatbot: Goodbye! Have an awesome day!")
                break
            responses.append(f"You: {user_input}")
            responses.append(f"Chatbot: {chatbot_response(user_input)}")
        
        with open(output_filename, 'w') as file:
            file.write("\n".join(responses))
        
        print(f"Chatbot responses saved to {output_filename}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
# run_chatbot_from_file("chat_input.txt", "chat_output.txt")

# chat_input.txt
# Hi
# What is your name?
# How are you?
# What can you do?
# Bye

# README.md
# # Rule-Based Chatbot
# This is a simple rule-based chatbot that reads user inputs from a file and generates responses.

# ## How to Run
# 1. Place your inputs in `chat_input.txt`
# 2. Run the script: `python chatbot.py`
# 3. The responses will be saved in `chat_output.txt`

# requirements.txt
# No external dependencies required, built using Python standard libraries
