import os
import sys
import json
import subprocess
import logging
logger = logging.getLogger(__name__)

import openai

def is_android():
    return os.uname().machine == 'aarch64'

def input_android():
    sout = subprocess.check_output(["termux-dialog"])
    sout = json.loads(sout)
    if sout["code"] == -2:
        raise EOFError
    result = sout["text"]
    return result

def get_input():
    if is_android():
        while True:
            result = input_android()
            if result == "":
                input()
            else:
                break
        print("Q:" + result)
    else:
        result = input("➑  ")
    return result

import requests

def loop(message_log):
    while True:
        # Query user
        try:
            message = get_input()
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
