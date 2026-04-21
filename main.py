import datetime
from crewai import Crew
from agents import code_reviewer
from tasks import code_review_task

def get_user_input():
    print("\n📥 Paste your code below (type 'END' on a new line to finish):\n")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    return "\n".join(lines)


def choose_operation():
    print("\n⚙️ Select operation:")
    print("1. Code Review")

    choice = input("Enter choice (1): ").strip()

    if choice == "1":
        return "review"
    else:
        print("❌ Invalid choice. Defaulting to Code Review.")
        return "review"


def save_output(content, operation):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outputs/{operation}_{timestamp}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(content))

    print(f"\n✅ Output saved to: {filename}")


def main():
    print("\n🚀 AI Code Review Agent\n")

    code_input = get_user_input()
    operation = choose_operation()

    crew = Crew(
        agents=[code_reviewer],
        tasks=[code_review_task]
    )

    print("\n🔄 Processing...\n")

    result = crew.kickoff(inputs={"code": code_input})

    print("\n📊 RESULT:\n")
    print(result)

    save_output(result, operation)


if __name__ == "__main__":
    main()