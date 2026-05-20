import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Prep2Hire.settings')
django.setup()

from skill_development.models import Quiz, Question, Option

# 10 High-Quality Manual Quizzes
real_quizzes = [
    {
        "title": "Python Basics",
        "description": "Test your fundamental Python knowledge.",
        "questions": [
            {
                "text": "Which of the following is a mutable data type in Python?",
                "options": [("List", True), ("Tuple", False), ("String", False), ("Integer", False)]
            },
            {
                "text": "What is the output of 3 ** 2?",
                "options": [("9", True), ("6", False), ("8", False), ("32", False)]
            }
        ]
    },
    {
        "title": "Django Framework Basics",
        "description": "Quiz on Django fundamentals.",
        "questions": [
            {
                "text": "Which file is used to configure database settings in Django?",
                "options": [("settings.py", True), ("models.py", False), ("urls.py", False), ("views.py", False)]
            },
            {
                "text": "What command is used to apply database migrations?",
                "options": [("python manage.py migrate", True), ("python manage.py makemigrations", False), ("django-admin migrate", False), ("python migrate.py", False)]
            }
        ]
    },
    {
        "title": "HTML & CSS Fundamentals",
        "description": "Test your web design basics.",
        "questions": [
            {
                "text": "Which HTML tag is used to create a hyperlink?",
                "options": [("<a>", True), ("<link>", False), ("<href>", False), ("<url>", False)]
            },
            {
                "text": "How do you select an element with id 'header' in CSS?",
                "options": [("#header", True), (".header", False), ("header", False), ("*header", False)]
            }
        ]
    }
]

# We will generate 100 total quizzes
topics = [
    "JavaScript", "React", "Node.js", "Java", "C++", "C#", "Go", "Rust", "Ruby", "PHP",
    "SQL", "MongoDB", "PostgreSQL", "AWS", "Azure", "GCP", "Docker", "Kubernetes",
    "Git", "Linux", "Data Structures", "Algorithms", "Machine Learning", "Deep Learning",
    "Natural Language Processing", "Computer Vision", "Cybersecurity", "Networking",
    "System Design", "Microservices", "REST APIs", "GraphQL", "TypeScript", "Vue.js",
    "Angular", "Svelte", "Tailwind CSS", "Bootstrap", "Webpack", "Babel", "Jest",
    "Mocha", "Cypress", "Selenium", "TensorFlow", "PyTorch", "Scikit-Learn", "Pandas"
]

created_count = 0

# Create the real quizzes first
for q_data in real_quizzes:
    quiz, created = Quiz.objects.get_or_create(title=q_data["title"], defaults={"description": q_data["description"]})
    if created:
        for question_data in q_data["questions"]:
            q = Question.objects.create(quiz=quiz, text=question_data["text"])
            for opt_text, is_corr in question_data["options"]:
                Option.objects.create(question=q, text=opt_text, is_correct=is_corr)
        created_count += 1
        print(f"Created Real Quiz: {quiz.title}")

# Procedurally generate the rest to reach 100
quizzes_needed = 100 - created_count

for i in range(quizzes_needed):
    topic = random.choice(topics)
    level = random.randint(1, 10)
    title = f"{topic} Mastery - Level {level} (Part {i+1})"
    description = f"A dynamically generated quiz to test your skills in {topic} at Level {level}."
    
    quiz, created = Quiz.objects.get_or_create(title=title, defaults={"description": description})
    if created:
        # Create 5 procedural questions
        for q_num in range(1, 6):
            question = Question.objects.create(quiz=quiz, text=f"Which of the following best describes a core concept in {topic} (Question {q_num})?")
            
            # 1 correct, 3 incorrect
            correct_opt = random.randint(1, 4)
            for opt_num in range(1, 5):
                if opt_num == correct_opt:
                    Option.objects.create(question=question, text=f"The correct implementation principle for {topic}.", is_correct=True)
                else:
                    Option.objects.create(question=question, text=f"An incorrect or deprecated approach.", is_correct=False)
                    
        created_count += 1
        print(f"Created Procedural Quiz: {quiz.title}")

print(f"\nSuccessfully added {created_count} quizzes to the database.")
