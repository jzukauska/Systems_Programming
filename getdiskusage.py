import argparse
from os import listdir
from os.path import isfile, join, getsize, isdir
import json


def is_good_path(path):
    if not isdir(path):
        raise ValueError("BadDir")
    return True


def output_json_string_from_path(argpath):
    data = []
    obj = {}

    is_good_path(argpath)

    for item in listdir(argpath):
        fullpath = join(argpath, item)

        if isfile(fullpath):
            size = getsize(fullpath)
            data.append({"path": fullpath, "bytes": size})

    obj["files"] = data

    return json.dumps(obj, indent=2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find file sizes and output json from path')
    parser.add_argument('path', type=str, help='Path of directory to get files')
    path = parser.parse_args().path

    try:
        output = output_json_string_from_path(path)
    except ValueError as e:

        if str(e) == "BadDir":
            print("Path argument is not a valid directory")
        else:
            print("Unknown Error")
    else:
        print(output)
