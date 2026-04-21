#  AI Code Review Agent

An AI-powered code analysis tool built using CrewAI and OpenRouter.  
This project simulates a senior software engineer reviewing code for quality, bugs, performance, and maintainability.

---

##  Overview

The AI Code Review Agent helps developers by:

- Identifying bugs and logical issues
- Suggesting performance improvements
- Enforcing best coding practices
- Improving readability and maintainability
- Highlighting potential security risks

---

##  Features

-  Autonomous Code Review Agent
-  Multi-dimensional code analysis
-  Fast and cost-efficient (OpenRouter - GPT-4o-mini)
-  Built using CrewAI agent architecture
-  Structured and detailed feedback output

---

##  Tech Stack

- Python 3.11
- CrewAI
- OpenRouter API
- dotenv

---

## 📂 Project Structure
<img width="456" height="530" alt="image" src="https://github.com/user-attachments/assets/a768687e-b6f3-4290-897e-f0fa45ed59dd" />

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

bash
git clone https://github.com/YOUR_USERNAME/ai-code-review-agent.git
cd ai-code-review-agentd

### Create virtual environment
python3.11 -m venv .venv
source .venv/bin/activate

### Install dependencies
pip install crewai openai python-dotenv

### Setup environment variables
Create a .env file:
OPENROUTER_API_KEY=your_api_key_here

### Run the project
python main.py

### Example
Input:
def add(a,b):
 return a+b

### Output
Code quality issues
Suggested improvements
Refactored version

### Cost Efficiency
Uses gpt-4o-mini
Approx ₹0.1–₹0.5 per request

### Future Enhancements
Multi-agent pipeline (Reviewer + Fixer)
GitHub PR integration
Web UI (Streamlit / React)
API deployment

### Author
Adarsh Singh Gautam
Building AI-powered developer tools

### TEP 11: Push
bash
git add .
git commit -m "Initial commit - AI Code Review Agent"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-code-review-agent.git
git push -u origin main

### Result
Ab tere paas 2 strong projects honge:
Content Writer Agent
Code Review Agent

