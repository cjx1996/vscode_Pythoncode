import os
import json
print(os.path.abspath('.'))
filename = 'vscode_Pythoncode/Python from start to practice/Chapters/Chapter12_Aliens/high_score.json'
with open (filename,'r') as f:
    a = json.load(f)
print(a)