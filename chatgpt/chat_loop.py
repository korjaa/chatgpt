import sys
import openai

def loop(message_log):
    while True:
        # Query user
        message = input("➑  ")
        message_log.append({"role": "user", "content": message})

        # Connect GPT
        events = openai.ChatCompletion.create(
            model = "gpt-4",
            messages = message_log,
            stream=True)

        # Receive response
        response = ""
        for result in events:
            try:
                partial_response = result.choices[0].delta.content
                response += partial_response
                print(partial_response, end="")
                sys.stdout.flush()
            except AttributeError:
                pass
        print()

        # Append response to log
        message_log.append({"role": "assistant", "content": response})
