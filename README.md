# 🧠 AI Code Review Agent

An AI-powered code analysis tool built using CrewAI and OpenRouter.  
This project simulates a senior software engineer reviewing code for quality, bugs, performance, and maintainability.

---

## 🚀 Overview

The AI Code Review Agent helps developers by:

- Identifying bugs and logical issues
- Suggesting performance improvements
- Enforcing best coding practices
- Improving readability and maintainability
- Highlighting potential security risks

---

## ✨ Features

- 🤖 Autonomous Code Review Agent
- 🔍 Multi-dimensional code analysis
- ⚡ Fast and cost-efficient (OpenRouter - GPT-4o-mini)
- 🧩 Built using CrewAI agent architecture
- 📄 Structured and detailed feedback output

---

## 🛠 Tech Stack

- Python 3.11
- CrewAI
- OpenRouter API
- dotenv

---

## 📂 Project Structure
ai-code-review-agent/
│
├── app/                          # Core application logic
│   ├── main.py                  # Entry point (runs the agent)
│   │
│   ├── agents/                  # All agent definitions
│   │   └── code_reviewer.py     # Code reviewer agent
│   │
│   ├── tasks/                   # Task definitions
│   │   └── review_task.py       # Code review task
│
├── inputs/                      # Sample inputs for testing
│   └── sample_code.py           # Example code for review
│
├── outputs/                     # Generated outputs
│   └── review_*.md              # Saved review reports
│
├── config/                      # Configuration files (optional future use)
│   └── settings.py              # Model, params, etc.
│
├── .env                         # API keys (ignored in Git)
├── .gitignore                   # Ignore rules
├── requirements.txt             # Dependencies
├── README.md                    # Project documentation
└── mainbk.py                    # Backup (optional)-

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-code-review-agent.git
cd ai-code-review-agentd