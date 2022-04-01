import base64
import json
import os


def file_to_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def get_all_files():
    return os.listdir(".")


files = get_all_files()

output = {}

for name in files:
    if name != "build.py" or name != "README.md":
        output.update({name: "data:audio/mpeg;base64,"+file_to_base64(name)})

with open("output.json", "w") as f:
    json.dump(output, f)
