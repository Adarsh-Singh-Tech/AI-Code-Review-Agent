from crewai import Crew
from agents import code_reviewer
from tasks import code_review_task

crew = Crew(
    agents=[code_reviewer],
    tasks=[code_review_task]
)

code_input = """
def add(a,b):
 return a+b
"""

result = crew.kickoff(inputs={"code": code_input})

print("\nREVIEW OUTPUT:\n")
print(result)