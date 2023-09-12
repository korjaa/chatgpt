from .chat_loop import loop

def main():
    message_log = [{
        "role": "system",
        "content":
            "You are a helpful assistant. "
            "In math and sciences, you work in metric and SI units. "
            "You don't repeat the question when answering. "
            "You don't respond with Ah and Oh. "
            "You don't split programming code examples in multiple pieces."
    }]

    try:
        loop(message_log)
    except KeyboardInterrupt:
        print()
