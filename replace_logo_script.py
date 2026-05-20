import os, glob
files = glob.glob('Prep2Hire/**/*.html', recursive=True)
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if '<h1>⚡ HirePilot</h1>' in content:
        content = content.replace('<h1>⚡ HirePilot</h1>', '<h1><img src="{% static \'assets/images/hirepilot_logo.png\' %}" style="width:50px;height:50px;vertical-align:middle;margin-right:10px;" alt="Logo">HirePilot</h1>')
        if '{% load static %}' not in content:
            content = '{% load static %}\n' + content
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
