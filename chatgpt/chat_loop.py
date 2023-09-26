import os
import sys
import json
import subprocess
import logging
logger = logging.getLogger(__name__)

import openai

import chatgpt

def is_android():
    return os.uname().machine == 'aarch64'

def input_android():
    sout = subprocess.check_output(["termux-dialog"])
    try:
        sout = json.loads(sout)
    except json.decoder.JSONDecodeError:
        return ""
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
                    deployment_id=chatgpt.deployment_id,  # This defines model in Azure
                    model="gpt-4",  # Not used in Azure
                    messages=message_log,
                    stream=True)

                # Receive response
                response = ""
                for result in events:
                    try:
                        if not result.choices:
                            continue
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
