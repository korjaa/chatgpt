import os
import json
import openai

model = None
deployment_id = None

fapi_keys = os.path.join(os.path.expanduser("~"), ".bash_aliases.d", "api_keys.json")
with open(fapi_keys, "r") as fid:
    bash_keys = json.load(fid)
    if "chatgpt_api_type" in bash_keys:
        openai.api_type = bash_keys["chatgpt_api_type"]

    if "chatgpt_api_base" in bash_keys:
        openai.api_base = bash_keys["chatgpt_api_base"]

    if "chatgpt_api_version" in bash_keys:
        openai.api_version = bash_keys["chatgpt_api_version"]

    if "chatgpt_deployment_id" in bash_keys:
        deployment_id = bash_keys["chatgpt_deployment_id"]

    if "chatgpt_model" in bash_keys:
        model = bash_keys["chatgpt_model"]
    else:
        model = "gpt-4"

    openai.api_key = bash_keys["chatgpt"]

def list_engines():
    engines = [e["id"] for e in openai.Engine.list()["data"]]
    engines.sort()
    return engines
