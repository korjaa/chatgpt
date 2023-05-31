import sys
import openai
import logging
logger = logging.getLogger(__name__)

import requests

def loop(message_log):
    while True:
        # Query user
        try:
            message = input("➑  ")
        except EOFError:
            print()
            break
        message_log.append({"role": "user", "content": message})

        # Retries
        for _ in range(10):
            try:
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
                break
            except requests.exceptions.ChunkedEncodingError:
                logger.warning("requests.exceptions.ChunkedEncodingError")
                continue
            except openai.error.APIConnectionError:
                logger.warning("openai.error.APIConnectionError")
                continue

        # Append response to log
        message_log.append({"role": "assistant", "content": response})
