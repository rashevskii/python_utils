import ftplib
import json
import os
import re

# Загрузка файлов на сервер из набора папок. Скрипт проходит по всем папкам и загружает конкретные файлы на конкрентные сайты

broken = []
path_json = 'ftps.json'  # json с путями, тут менять
image_dirs = [item for item in os.listdir() if not re.search("\.", item)]  # список папок с картинками
path_on_server = 'images/__user__/pharmacies/'  # путь назначения, тут менять

with open(path_json, "r", encoding="utf-8") as f:
    access_dict = json.load(f)

for image_dir in image_dirs:
    images = os.listdir(image_dir)
    os.chdir(image_dir)

    for key, val in access_dict.items():
        if image_dir in key:
            try:
                ftp = ftplib.FTP(val["host"], val["username"], val["password"])
                print(f'-----------Подключился к {key}------------')
                ftp.cwd(path_on_server)
                print(f'-----------Перешел в {path_on_server}-----------------')
                for idx, el in enumerate(images):
                    file = open(f'{el}', 'r+b')
                    ftpResponseMessage = ftp.storbinary(f'STOR {el}', file)
                    print(f"{idx} - {key} - {ftpResponseMessage}")
                    file.close()
                ftp.quit()
            except Exception as e:
                print(f"{key} - {e}")
                broken.append({key: e})
            print(f'File upload on {val["host"]}')
    print(f"Script is over with {broken=}")
    os.chdir('../')
