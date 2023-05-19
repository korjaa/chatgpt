import os
import sys
import json

import openai

fapi_keys = os.path.join(os.path.expanduser("~"), ".bash_aliases.d", "api_keys.json")
with open(fapi_keys, "r") as fid:
    my_key = json.load(fid)["chatgpt"]
    openai.api_key = my_key

def list_engines():
    engines = [e["id"] for e in openai.Engine.list()["data"]]
    engines.sort()
    return engines
#print("\n".join(list_engines()))

message_log = [
    {
        "role": "system",
        "content": "You are a helpful assistant. You don't split code examples in multiple pieces."
    }]

try:
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
except KeyboardInterrupt:
    print()
    pass
