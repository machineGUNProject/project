# -*- coding: utf-8 -*-
import os

def file_read():
    path = 'C:/Users/Ai/Desktop/final_cut/'

    #파일의 경로를 읽습니다.
    folders = os.listdir(path)
    folders
    #반복문으로 전체 폴더를 읽어내어 files에 추가합니다.
    files = []
    for folder in folders:
        full_filename = os.path.join(path, folder)
        files.append(os.listdir(full_filename))
    final_answer = []
    #files는 [[첫번째 폴더안의 파일들],[두번째 폴더안의 파일들],...] 구조를 가지게 됩니다.
    for i in range(len(files)):
        for c in range(0, len(files[0])):
            final_answer.append(path + str(files[0][c]))

    return len(final_answer)

print(file_read())
