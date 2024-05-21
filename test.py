
from ollama import Client

client = Client(host="http://127.0.0.1:11434")
response = client.chat(model="llama3", messages=[
            {
                'role': 'system',
                'content': "You are an SD prompt maker, you create high quality coherent stablediffusion prompts base on the input. limit your respond to no more than 50 words, Use the user input to construct your response, always include all the words from the user input within your response, be non verbose, non superflous, Since you are describing images make sure to describe the framing of the shot, lighting and composition, pose or action, location subject. use keywords that are choherent for the request, do not include explanations or additional information about meaning or artist intentions",
            },
            {
                'role': 'user',
                'content': "a girl with blue hair"
            },
        ])
print(response["message"]["content"])