import pytest
from questions import get_questions
from project import run_quiz

def test_get_questions_valid_category():
    categories = ["Biology", "Chemistry", "Physics", "Earth Science"]
    for category in categories:
        questions = get_questions(category)
        assert isinstance(questions, list)
        assert len(questions) > 0
        for q in questions:
            assert "question" in q
            assert "choices" in q
            assert "answer" in q
            assert isinstance(q["choices"], list)
            assert len(q["choices"]) == 4

def test_get_questions_invalid_category():
    questions = get_questions("Magic")  # A non-existent category
    assert questions == []


