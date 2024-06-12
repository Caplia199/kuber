import math

def safe_eval(expression):
    allowed_names = {
        k: v for k, v in math.__dict__.items() if not k.startswith("__")
    }
    allowed_names.update({
        'abs': abs,
        'round': round,
    })

    code = compile(expression, "<string>", "eval")

    for name in code.co_names:
        if name not in allowed_names:
            raise NameError(f"Use of '{name}' is not allowed")

    return eval(code, {"__builtins__": {}}, allowed_names)
