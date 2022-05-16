import os
import re

# Скрипт на основании списка наименований файлов выдает 2 файла - с путями на сервере, в каждый путь подставляется название файла, и со списком наименований файлов. 
# Скрипт использовался для удобства работы при сборе данных на основании исходных данных

IMAGE_PATH: str = '/images/__user__/pharmacies/'

dirs = [item for item in os.listdir() if not re.search("\.", item)]


def parse_names(path):
    names_files = os.listdir(path)
    data = [f'{IMAGE_PATH}{name}' for name in names_files]
    return data


def parse_codes(path):
    codes = os.listdir(path)
    data = [f'{name.split(".")[0]}' for name in codes]
    return data


if __name__ == '__main__':
    for path in dirs:
        paths_list = parse_names(path)
        code_list = parse_codes(path)

        with open(f"{path}_paths.txt", "w", encoding="utf-8") as f:
            for i, string in enumerate(paths_list):
                if i != len(paths_list) - 1:
                    f.write(f'{string},')
                else:
                    f.write(f'{string}')
        with open(f"{path}_codes.txt", "w", encoding="utf-8") as f:
            for i, code in enumerate(code_list):
                if i != len(code_list) - 1:
                    f.write(f'{code},')
                else:
                    f.write(f'{code}')
