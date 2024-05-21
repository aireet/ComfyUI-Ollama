

class CO_MODEL:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
                        "model": ("MODEL",),
                     },
                }
    FUNCTION = "echo"
    RETURN_TYPES = ("VALUE")
    def echo(s, input, echo):
        return 0