import json
import os

def read_json(file_path):
    try:
        with open(file_path) as json_file:
            data = json.load(json_file)
            return data
    except Exception as ex:
        print(ex)

def write_json(formatted_key_value_pairs, path):
    name = os.path.splitext(path)[0]

    json_output = json.dumps(dict(formatted_key_value_pairs))
    with open(f'output\{name}.json', 'w') as outfile:
        outfile.write(json_output)