from crewai import Task
from agents import code_reviewer

code_review_task = Task(
    description=(
        "Review the following code:\n\n"
        "{code}\n\n"
        "Analyze for:\n"
        "1. Code quality and best practices\n"
        "2. Bugs or logical errors\n"
        "3. Performance improvements\n"
        "4. Readability and maintainability\n"
        "5. Security issues\n"
    ),
    expected_output="Detailed structured code review with suggestions",
    agent=code_reviewer,
)