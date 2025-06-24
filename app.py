import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.0-flash')

# === PROMPT SETS ===
prompt_variants = {
    "question": [
        "What is the capital of France?",
        "Can you briefly explain Newton’s law of motion?",
        "Tell me 3 interesting facts about the Moon."
    ],
    "summarize": [
        "Summarize the following paragraph: The internet has revolutionized...",
        "Can you give a short summary of this article?",
        "Extract the main points from this text: ..."
    ],
    "creative": [
        "Write a short story about a robot and a lost child.",
        "Create a poem on the theme of hope and rain.",
        "Generate an idea for a science fiction novel set in 3024."
    ],
    "advice": [
        "What are some tips for staying productive while studying?",
        "How can I reduce stress before an exam?",
        "Give me advice on managing time in college."
    ]
}

# === ASK GEMINI ===
def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# === FEEDBACK LOGGER ===
def log_interaction(category, user_prompt, ai_response, feedback):
    with open("feedback_log.txt", "a", encoding="utf-8") as file:
        file.write("=== New Interaction ===\n")
        file.write(f"Category     : {category}\n")
        file.write(f"User Prompt  : {user_prompt}\n")
        file.write(f"AI Response  : {ai_response}\n")
        if feedback:
            file.write(f"Feedback     : {feedback}\n")
        file.write("\n")

# === MENU INTERFACE ===
def main():
    while True:
        print("\n=== Gemini AI Assistant ===")
        print("1. Answer Factual Question")
        print("2. Summarize Text")
        print("3. Generate Creative Content")
        print("4. Get Advice")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == '5':
            print("Thank you for using the Gemini AI Assistant. Goodbye!")
            break

        elif choice in ['1', '2', '3', '4']:
            category_map = {
                '1': 'question',
                '2': 'summarize',
                '3': 'creative',
                '4': 'advice'
            }
            category = category_map[choice]

            print(f"\nChoose a prompt example or enter your own:")
            for idx, prompt in enumerate(prompt_variants[category], 1):
                print(f"{idx}. {prompt}")
            print(f"{len(prompt_variants[category])+1}. Enter my own prompt")

            sub_choice = input(f"Select (1-{len(prompt_variants[category])+1}): ")
            if sub_choice.isdigit():
                sub_choice = int(sub_choice)
                if 1 <= sub_choice <= len(prompt_variants[category]):
                    user_prompt = prompt_variants[category][sub_choice - 1]
                elif sub_choice == len(prompt_variants[category]) + 1:
                    user_prompt = input("Type your custom prompt: ")
                else:
                    print("Invalid choice. Returning to main menu.")
                    continue
            else:
                print("Invalid input. Returning to main menu.")
                continue

            ai_response = ask_gemini(user_prompt)
            print("\n=== AI Response ===")
            print(ai_response)

            feedback = input("Was this response helpful? (yes/no): ").strip()
            log_interaction(category, user_prompt, ai_response, feedback)

        else:
            print("Invalid option. Please select a number from 1 to 5.")

if __name__ == "__main__":
    main()
