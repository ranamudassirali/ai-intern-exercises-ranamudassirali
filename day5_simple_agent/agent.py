import os
import time
from dotenv import load_dotenv
from groq import Groq
from tools import calculator, get_weather

load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("XAI_API_KEY"))

# Standard Groq model for 2026
MODEL_ID = "llama-3.1-8b-instant"


def run_agent(user_query):
    """Processes a query and returns tool usage and the final answer."""
    # --- STEP 1: REASONING ---
    prompt = """
    You are an AI Agent. Tools available:
    1. calculator(expression): Math problems.
    2. get_weather(city): Weather lookups.

    Respond in this format:
    THOUGHT: <reasoning>
    TOOL: <calculator, get_weather, or none>
    INPUT: <input string>
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_query}
        ],
        model=MODEL_ID,
    )

    response_text = chat_completion.choices[0].message.content

    # Parsing logic
    tool_name = "none"
    tool_input = ""
    for line in response_text.split('\n'):
        if "TOOL:" in line:
            tool_name = line.replace("TOOL:", "").strip().lower()
        if "INPUT:" in line:
            tool_input = line.replace("INPUT:", "").strip().replace('"', '')

    # --- STEP 2: ACTION ---
    observation = "No tool needed."
    used_tool = "none"

    if "calculator" in tool_name:
        observation = str(calculator(tool_input))
        used_tool = f"calculator ({tool_input})"
    elif "weather" in tool_name:
        observation = get_weather(tool_input)
        used_tool = f"get_weather ({tool_input})"

    # --- STEP 3: FINAL ANSWER ---
    final_res = client.chat.completions.create(
        messages=[
            {"role": "user", "content": (
                f"Query: {user_query}\n"
                f"Result: {observation}\n"
                "Give a final answer."
            )}
        ],
        model=MODEL_ID,
    )

    final_answer = final_res.choices[0].message.content.strip()

    return used_tool, final_answer


if __name__ == "__main__":
    input_file = "queries.txt"
    output_file = "results.txt"

    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found. Create it with your queries.")
    else:
        with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
            print(f"Reading from {input_file}...")

            for line in f_in:
                query = line.strip()
                if not query:
                    continue

                print(f"Processing: {query}")
                try:
                    # Run agent and get results
                    tool_used, answer = run_agent(query)

                    # Write to results.txt in the required format
                    f_out.write(f"Query: {query}\n")
                    f_out.write(f"Tool used: {tool_used}\n")
                    f_out.write(f"Answer:\n{answer}\n")
                    f_out.write("-" * 20 + "\n")

                    # Respect API limits
                    time.sleep(1)

                except Exception as e:
                    error_msg = f"Query: {query}\nError: {e}\n"
                    f_out.write(error_msg + "-" * 20 + "\n")
                    print(f"Error: {e}")

        print(f"✅ Finished! Check {output_file} for results.")