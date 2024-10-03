import os
# print(os.getcwd()) # current working directory 현재 작업 공간
# # os.chdir("rpa_basic") # rpa_basic 으로 작업 공간 이동
# print(os.getcwd())
# os.chdir("..") # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir("../..") # 조부모 폴더로 이동
# print(os.getcwd())

# 파일 경로만들기 
file_path = os.path.join(os.getcwd(), "my_file.txt") # 절대 경로 생성
# print(os.path.join(os.getcwd(), ""))

