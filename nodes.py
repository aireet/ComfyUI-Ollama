from ollama import Client


supported_models = ["llama3", "llava"]

class CO_CLIENT:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "endpoint": ("STRING", {"default": "http://127.0.0.1:11434"}),
            }
        }

    FUNCTION = "load_client"

    RETURN_TYPES = ("Client", )

    def load_client(self, endpoint):
        return (Client(host=endpoint), )

class CO_CHAT:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                        "question": ("STRING", {"forceInput": True}),
                        "system": ("STRING", {"forceInput": True}),
                        "client": ("Client",),
                        "model": (supported_models, ),
            }
        }
    FUNCTION = "chat"

    RETURN_TYPES = ("STRING",)

    def chat(self, question, system, client, model):
        print(question, system)

        message = []
        if system:
            message.append({
                'role': 'system',
                'content': system,
            })

        message.append(
            {
                'role': 'user',
                'content': question
            },
        )
        response = client.chat(model=model, messages=message)
        print(response)
        return (response["message"]["content"], )

class CO_QUESION:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
            }
        }

    FUNCTION = "q"
    RETURN_TYPES = ("STRING",)
    def q(self, text):
        return (text,)