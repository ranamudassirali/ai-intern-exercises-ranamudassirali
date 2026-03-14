# 🤖 Day 5: Simple ReAct AI Agent

This project implements a **ReAct (Reason + Act)** AI Agent using Python and the Groq Cloud API. Unlike standard chatbots, this agent can "think" about a query and decide whether it needs to execute an external tool to find the correct answer.

---

## 🌟 Key Features
* **ReAct Logic**: Uses a chain-of-thought process: `Thought` -> `Action` -> `Observation` -> `Final Answer`.
* **External Tools**: Equipped with a safe Math Calculator and a Mock Weather Service.
* **Automated Batch Processing**: Reads multiple queries from a text file and generates a structured log of results.
* **PEP 8 Compliant**: The code follows strict Python style guidelines (checked with Flake8).



---

## 📁 Project Structure
| File | Description |
| :--- | :--- |
| **`agent.py`** | The main engine that handles reasoning, parsing, and execution. |
| **`tools.py`** | Contains the Python functions the agent can call (Calculator, Weather). |
| **`queries.txt`** | Input file containing the list of questions for the agent. |
| **`results.txt`** | Generated output file containing the agent's full interaction logs. |
| **`.gitignore`** | Ensures sensitive files like `.env` are not uploaded to GitHub. |

---

## 🛠️ Setup Instructions

### 1. Requirements
* Python 3.8+
* Groq Cloud API Key

### 2. Installation
Clone the repository and install the necessary library:
```bash
pip install groq python-dotenv

3. Environment Variables
Create a .env file in the project root and add your API key:
XAI_API_KEY=your_groq_api_key_here

4. Running the Agent
Ensure you have a queries.txt file in the folder, then run:
python agent.py