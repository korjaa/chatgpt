from .chat_loop import loop

def main():
    message_log = [{
        "role": "system",
        "content":
            "You are Vietnamese language translator. "
    }]

    try:
        loop(message_log)
    except KeyboardInterrupt:
        print()
        pass
