import time
import os
import ollama


# --- Configuration ---
MODEL_NAME = "qwen3.5:0.8b"
LOG_FILE = "prompts_and_responses.md"
# OPTIMIZATION: Set this to your CPU's physical core count (e.g., 4, 6, or 8)
CPU_THREADS = 4


def log_to_markdown(category, prompt, response, user_notes, dur):
    """Saves results with generation duration and user observations."""
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        if not file_exists:
            f.write("# Qwen3.5-0.8B Exercise Results\n\n")

        f.write(f"## 📌 Category: {category}\n")
        f.write(f"**Prompt:** {prompt}\n\n")
        f.write(f"**⏱️ Response Time:** {dur:.2f} seconds\n\n")
        f.write(f"### 🤖 Model Response:\n{response}\n\n")
        f.write("### 🔍 Your Observations:\n")
        f.write(f"{user_notes}\n")
        f.write("\n---\n\n")


def run_task(category):
    """Executes evaluation with optimized CPU threading."""
    print(f"\n{'='*40}\nACTIVE TASK: {category}\n{'='*40}")
    user_prompt = input("Enter your prompt: ")

    if not user_prompt:
        print("Empty prompt, skipping.")
        return

    print("\n🚀 Generating (Optimized for CPU)...")
    try:
        # Start high-precision timer
        start_time = time.perf_counter()

        # Generation with performance options
        response_data = ollama.generate(
            model=MODEL_NAME,
            prompt=user_prompt,
            options={
                "num_thread": CPU_THREADS,
                "temperature": 0.7
            }
        )

        model_output = response_data['response']
        duration = time.perf_counter() - start_time

        print(f"\nMODEL OUTPUT:\n{model_output}\n")
        print(f"⏱️ Speed: {duration:.2f} seconds")
        print("-" * 20)

        # Manual Observations
        print("Analyze for: Correctness, Hallucinations, Reasoning.")
        user_notes = input("Your observations: ")

        # Save results
        log_to_markdown(category, user_prompt, model_output, user_notes, duration)
        print(f"\n✅ Results appended to {LOG_FILE}")

    except Exception as e:
        print(f"❌ Error: {e}. Ensure Ollama is running.")


def main():
    """Main selection menu."""
    tasks = {
        "1": "1️⃣ Coding",
        "2": "2️⃣ General Knowledge / QA",
        "3": "3️⃣ Reasoning",
        "4": "4️⃣ Visual Question Answering"
    }

    while True:
        print("\n--- Qwen 3.5 Local Evaluation Menu ---")
        for key, value in tasks.items():
            print(f"{key}. {value}")
        print("5. Exit")

        choice = input("\nSelect (1-5): ")

        if choice == "5":
            print("Session ended. Happy documenting!")
            break
        elif choice in tasks:
            run_task(tasks[choice])
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()