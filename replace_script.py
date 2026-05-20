import os, glob
files = glob.glob('Prep2Hire/**/*.html', recursive=True)
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if 'Prep2Hire' in content or 'prep2hire' in content:
        content = content.replace('Prep2Hire', 'HirePilot').replace('prep2hire.com', 'hirepilot.com').replace('prep2hire', 'hirepilot')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
