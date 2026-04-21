import os
from crewai import Agent
from crewai.llm import LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="openai/gpt-4o-mini",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

code_reviewer = Agent(
    role="Senior Code Reviewer",
    goal="Review code for best practices, bugs, and improvements",
    backstory=(
        "You are a senior software engineer with 10+ years of experience. "
        "You review code for quality, performance, security, and maintainability."
    ),
    llm=llm,
    verbose=True
)