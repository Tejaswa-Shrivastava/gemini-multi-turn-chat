#!/usr/bin/env python3
# gemini_chat.py - A console chatbot using Google Gemini API (Gemini 1.5 Flash).

import os
from google import generativeai as genai
import sys

def get_api_key():
    """Securely get the Gemini API key"""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Please set the GEMINI_API_KEY environment variable.")
        print("You can get your API key from the Google Cloud Console after enabling the Generative AI API.")
        sys.exit(1)
    return api_key

def get_model_parameters():
    """Get model parameters from user input"""
    print("\nModel Parameters:")
    
    # Get temperature
    while True:
        try:
            temp_input = input("Enter temperature (0.0 to 1.0, default 0.7): ")
            temperature = float(temp_input) if temp_input else 0.7
            if 0.0 <= temperature <= 1.0:
                break
            print("Please enter a value between 0.0 and 1.0")
        except ValueError:
            print("Please enter a valid number")
    
    # Get top-p
    while True:
        try:
            top_p_input = input("Enter top-p (0.0 to 1.0, default 0.9): ")
            top_p = float(top_p_input) if top_p_input else 0.9
            if 0.0 <= top_p <= 1.0:
                break
            print("Please enter a value between 0.0 and 1.0")
        except ValueError:
            print("Please enter a valid number")
    
    return temperature, top_p

def main():
    try:
        # Initialize client
        api_key = get_api_key()
        genai.configure(api_key=api_key)
        
        # Get model parameters
        temperature, top_p = get_model_parameters()
        
        print("\nStarting Gemini Chat")
        print("Type 'exit' to end the conversation")
        
        # Initialize conversation
        messages = []
        
        while True:
            # Get user input
            user_msg = input("\nYou: ").strip()
            
            if user_msg.lower() == 'exit':
                print("\nGoodbye!")
                break
                
            # Add user message to messages
            messages.append({"author": "user", "content": user_msg})
            
            try:
                # Get Gemini response
                model = genai.GenerativeModel()
                chat = model.start_chat()
                
                # Set model parameters
                chat.temperature = temperature
                chat.top_p = top_p
                
                response = chat.send_message(user_msg)
                
                assistant_msg = response.text
                print(f"\nGemini: {assistant_msg}")
                
                # Add Gemini's response to messages
                messages.append({"author": "model", "content": assistant_msg})
                
            except Exception as e:
                print(f"Error getting Gemini response: {str(e)}")
                sys.exit(1)
                
    except KeyboardInterrupt:
        print("\n\nConversation ended by user")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
