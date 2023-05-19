from .chat_loop import loop

def main():
    message_log = [{
        "role": "system",
        "content": "You are a helpful assistant. You don't split code examples in multiple pieces."
    }]

    try:
        loop(message_log)
    except KeyboardInterrupt:
        print()
        pass
