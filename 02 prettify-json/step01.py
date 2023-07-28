import glob
from pathlib import Path
import json
import re
import os


dir_ls = ["Yara/coleta01-prettified"]


def logError(file_path, text):
    err_file_s = str(Path(file_path).parent.parent) + '/errs.txt'
    with open(err_file_s, 'a') as f:
        f.write(text)

def prettifyJSON(file_path,text):
    try:
        text_dict = json.loads(text)
        pretty_json = json.dumps(
            text_dict,
            indent=2,
            ensure_ascii=False
        )
    except json.JSONDecodeError as e:
        logError(
            file_path,
            f"Err: {file_s}\n{e}\n\n"
        )
        pretty_json = '{}'
    return pretty_json


for dir in dir_ls:

    # A pasta que atravessamos
    path_s = f"../data/{dir}/*.json"

    files_ls = glob.glob(path_s)

    for file_path in files_ls:
        with open(file_path, "r") as file:
            text = file.read()
            pretty_json = prettifyJSON(
                os.path.abspath(file_path),
                text
            )
        with open(file_path, "w") as file:
            file.write(pretty_json)
            print(file_path)
            a=1
