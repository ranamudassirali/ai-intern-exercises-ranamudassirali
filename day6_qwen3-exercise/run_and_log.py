import ollama
import os
from datetime import datetime

# Configuration
MODEL_NAME = "qwen3.5:0.8b"
LOG_FILE = "prompts_and_responses.md"

def log_to_markdown(category, prompt, response, notes):
    """Appends the evaluation to the markdown file in a table-like format."""
    file_exists = os.path.isfile(LOG_FILE)
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        # Add header if the file is new
        if not file_exists:
            f.write("# Model Evaluation Log\n\n")
            f.write("| Category | Prompt | Model Response | Notes |\n")
            f.write("| :--- | :--- | :--- | :--- |\n")
        
        # Clean up strings for markdown table (remove newlines from cell)
        clean_response = response.replace("\n", "<br>")
        clean_prompt = prompt.replace("\n", " ")
        
        # Append the row
        f.write(f"| {category} | {clean_prompt} | {clean_response} | {notes} |\n")

def run_exercise():
    print(f"--- Qwen3.5-0.8B Local Logger ---")
    
    # 1. Get User Inputs
    category = input("Enter Prompt Category (e.g., Coding, Reasoning): ")
    user_prompt = input("Enter your Prompt: ")
    
    print("\nGenerating response...")
    
    # 2. Run Model
    try:
        response = ollama.generate(model=MODEL_NAME, prompt=user_prompt)
        model_output = response['response']
        
        print("-" * 30)
        print(f"MODEL RESPONSE:\n{model_output}")
        print("-" * 30)
        
        # 3. Manual Debugging/Observations
        print("\nAnalyze the response for:")
        print("- Correctness\n- Hallucinations\n- Incomplete reasoning\n- Interesting behavior")
        obs_notes = input("\nEnter your observation notes: ")
        
        # 4. Save to MD
        log_to_markdown(category, user_prompt, model_output, obs_notes)
        print(f"\n✅ Successfully saved to {LOG_FILE}")
        
    except Exception as e:
        print(f"❌ Error: {e}. Is Ollama running?")

if __name__ == "__main__":
    while True:
        run_exercise()
        cont = input("\nRun another prompt? (y/n): ")
        if cont.lower() != 'y':
            break