import random
from questions import get_questions


def main():
    print("Welcome to the Science Literacy Quiz App!")
    print("Test your knowledge across different branches of science.\n")

    categories = ["Biology", "Chemistry", "Physics", "Earth Science"]
    print("Available Categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    choice = input("Choose a category by number: ")
    try:
        category = categories[int(choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice. Exiting.")
        return

    questions = get_questions(category)
    if not questions:
        print("No questions found in this category.")
        return

    random.shuffle(questions)
    run_quiz(questions)

def run_quiz(questions):
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for j, choice in enumerate(q['choices'], 1):
            print(f"{j}. {choice}")
        answer = input("Your answer (1-4): ")
        try:
            # Check if the answer is valid
            if int(answer) < 1 or int(answer) > 4:
                print("❌ Invalid input. Choose a number between 1 and 4.")
                continue
            # Check if the selected option matches the correct answer
            selected_option = q['choices'][int(answer) - 1].lower()  # User's selected option
            correct_answer = q['answer'].lower()  # Correct answer from the question
            if selected_option == correct_answer:
            #if q['choices'][int(answer) - 1].lower() == q['answer'].lower():
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect! Correct answer was: {q['answer']}")
        except (IndexError, ValueError):
            print(f"❌ Invalid input. Correct answer was: {q['answer']}")

    print(f"\nYou scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    main()



