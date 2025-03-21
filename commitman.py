#!/usr/bin/env python
import sys
import os
try:
    from mistralai import Mistral as Brain
except Exception as e:
    print(str(e))
    print("install required package!")
    sys.exit(-1)

if len(sys.argv) != 2:
    print("the only argument is required. Mistral AI API key.")
    sys.exit(-2)
key = sys.argv[1]

pipe_input = sys.stdin.read()
if not pipe_input.strip():
    print("no `git diff` data provided via pipe. Aborted.")
    sys.exit(-3)


os.environ["MISTRAL_API_KEY"] = key
client = Brain(api_key=os.environ["MISTRAL_API_KEY"])

def ask(prompt:str):
    '''send provided prompt to Mistral AI and returns its request'''
    chat_response = client.chat.complete(
        model= "mistral-large-latest",
        messages = [
            {
                "role": "user",
                "content": prompt,
            },
        ]
    )
    response = chat_response.choices[0].message.content
    return response

response = ask("{} this is result of git diff. Write short commit of changes. Give actual commit in brackets.".format(pipe_input))
print(response.split("\n")[1])
