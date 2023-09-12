from .chat_loop import loop

def main():
    message_log = [{
        "role": "system",
        "content":
            "You are a helpful assistant that provides Python snippets to a Python programmer. "
            "You prioritize minimal examples over error checking. "
            "You don't instruct how to install Python packages. "
    }]

    try:
        loop(message_log)
    except KeyboardInterrupt:
        print()
