import ftplib
import re

# Скрипт исполльзовался для поиска данных через ftp, а также вывод данных в файл с последующим поиском нужных данных в файле

ftp = ftplib.FTP("host", "user", "pass")
ftp.cwd('/')


def ftp_walk(ftp):
    print('Path:', ftp.pwd())
    dirs = ftp.nlst()
    retrLines = []
    ftp.retrlines('LIST -a', retrLines.append)
    listOfFiles = []
    for entry in retrLines:
        entrySplit = entry.split(' ')[-1]
        if entrySplit not in ['.', '..']:
            data = entry.split(' ')
            result = []
            for el in data:
                if el:
                    result.append(el)
            if result[5] == "Jun" and result[6] == "23":
                listOfFiles.append(result[8])
    print(listOfFiles) if len(listOfFiles) else print('------------------')
    if len(listOfFiles):
        with open('result_search.txt', 'a', encoding='utf-8') as f:
            f.write(f'{ftp.pwd()}\n')
            f.write(f'{listOfFiles}\n')
    for item in (path for path in dirs if not re.search("\w+\.\w+", path)):
        try:
            ftp.cwd(item)
            print('Changed to', ftp.pwd())
            ftp_walk(ftp)
            ftp.cwd('..')
        except Exception as e:
            print(item, e)


ftp_walk(ftp)
ftp.quit()
