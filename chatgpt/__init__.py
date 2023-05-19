import os
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
