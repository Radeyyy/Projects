# Science Literacy Quiz App
#### Video Demo: https://youtu.be/4hZCUdPLQVc
#### Description:

This project is a command-line based quiz app that helps users test their knowledge of science across four categories: Biology, Chemistry, Physics, and Earth Science.

Upon launching, users are welcomed and prompted to select a category. The app then displays a randomized set of questions with multiple-choice options. Users enter the number corresponding to their chosen answer. The app immediately tells the user whether they are correct or not and tracks their score.

### Features:
- Four science categories to choose from
- Randomized questions using the `random` module
- Instant feedback for each answer
- Score summary at the end

### Files:
- `project.py`: This is the main file. It contains the logic for displaying questions, taking input, checking answers, and showing the score.
- `questions.py`: A separate module that stores and returns questions based on category.
- `test_project.py`: Contains test functions to validate that `get_questions` works correctly and the question structure is consistent.

### Design Choices:
I kept the project simple and terminal-based to focus on logic and user experience. I chose not to use external libraries to avoid confusion and show what could be done with just Python's built-in capabilities. I also separated the questions into a different file for better structure and scalability.

This project helped me practice working with functions, lists, dictionaries, input/output handling, and basic testing with pytest.

### How to Run:
1. Make sure you have Python installed.
2. Run the project from terminal:
```bash
python project.py

