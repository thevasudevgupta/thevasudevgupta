from transformers import pipeline
model = pipeline("question-answering")
answer = model("What's your name?", "My name is Vasudev Gupta. I do ML at Unbox AI. I love learning new things and read more. I don't get sleep at nights :(")
print(answer)

import subprocess
# stdout = subprocess.run("source $HOME/.bashrc".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(stdout)
 
stdout = subprocess.run("ovhai notebook ls".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(stdout)
