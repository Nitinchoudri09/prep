import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Prep2Hire.settings')
django.setup()

from Home.models import Question, Option, CareerSuggestion

def populate_career():
    print("Clearing old career data...")
    Question.objects.all().delete()
    CareerSuggestion.objects.all().delete()

    print("Creating career suggestions...")
    careers = [
        CareerSuggestion(career="Software Engineer", description="Design, develop, and maintain software applications.", skills_required="Python, Java, C++, Problem Solving"),
        CareerSuggestion(career="Data Scientist", description="Analyze and interpret complex data to help organizations make decisions.", skills_required="Python, R, Statistics, Machine Learning"),
        CareerSuggestion(career="Product Manager", description="Guide the success of a product and lead the cross-functional team that is responsible for improving it.", skills_required="Leadership, Communication, Agile, Strategy"),
        CareerSuggestion(career="UX/UI Designer", description="Design the user interfaces and user experiences for digital products.", skills_required="Figma, Wireframing, User Research, Prototyping"),
    ]
    CareerSuggestion.objects.bulk_create(careers)

    print("Creating questions and options...")
    questions_data = [
        {
            "text": "When faced with a complex problem, what is your preferred approach?",
            "options": [
                {"text": "Write a script or code to solve it.", "scores": {"Software Engineer": 10, "Data Scientist": 5}},
                {"text": "Analyze the data and find patterns.", "scores": {"Data Scientist": 10, "Software Engineer": 2}},
                {"text": "Organize a team meeting to discuss solutions.", "scores": {"Product Manager": 10, "UX/UI Designer": 2}},
                {"text": "Sketch out possible visual solutions and user flows.", "scores": {"UX/UI Designer": 10, "Product Manager": 2}},
            ]
        },
        {
            "text": "What type of environment do you thrive in?",
            "options": [
                {"text": "Working independently with focused coding time.", "scores": {"Software Engineer": 10, "Data Scientist": 2}},
                {"text": "Working with data, numbers, and statistics.", "scores": {"Data Scientist": 10, "Software Engineer": 2}},
                {"text": "Leading a team and making strategic decisions.", "scores": {"Product Manager": 10, "Software Engineer": 2}},
                {"text": "Collaborating with users to understand their needs.", "scores": {"UX/UI Designer": 10, "Product Manager": 5}},
            ]
        },
        {
            "text": "Which tool do you find most interesting to learn?",
            "options": [
                {"text": "A new programming language or framework.", "scores": {"Software Engineer": 10}},
                {"text": "A new statistical model or machine learning algorithm.", "scores": {"Data Scientist": 10}},
                {"text": "A new project management or roadmapping software.", "scores": {"Product Manager": 10}},
                {"text": "A new design tool or prototyping software.", "scores": {"UX/UI Designer": 10}},
            ]
        }
    ]

    for q_data in questions_data:
        question = Question.objects.create(text=q_data["text"])
        for opt_data in q_data["options"]:
            Option.objects.create(
                question=question,
                text=opt_data["text"],
                score_map=opt_data["scores"]
            )
            
    print("Career data populated successfully!")

if __name__ == '__main__':
    populate_career()
