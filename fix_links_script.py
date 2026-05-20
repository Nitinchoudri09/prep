import os, glob
files = glob.glob('Prep2Hire/**/*.html', recursive=True)
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if '/resume-analyzer/score-checker/' in content or '/resumes/score-checker/' in content:
        content = content.replace('/resume-analyzer/score-checker/', '/resume-analyzer/').replace('/resumes/score-checker/', '/resume-analyzer/')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
