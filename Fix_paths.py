from typing import *
import os


def __getFilesList(files_path: str) -> List:
    files_list = []
    for root, dirs, files in os.walk(files_path):
        for name in files:
            ext = name.split(".")[-1]
            if ext == "hds":
                files_list.append(os.path.join(root, name))
    return files_list


def fixPaths(files_path: str) -> None:
    pattern = r"$TO_BE_REPLACED$"
    files_list = __getFilesList(files_path)
    for file in files_list:
        with open(file, "r+", encoding='utf8') as f:
            data = f.read()
            path = os.path.abspath(files_path) + "\\"
            new_data = data.replace(pattern, path)
            f.seek(0)
            f.write(new_data)


if __name__ == "__main__":
    fixPaths("Files")
