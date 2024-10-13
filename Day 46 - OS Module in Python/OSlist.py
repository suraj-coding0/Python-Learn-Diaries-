import os

folders = os.listdir("data")

print(folders)              #check how many folder in data folder
# print(os.getcwd())        #check file directory
# os.chdir("/Users")        #change file diractory
# print(os.getcwd())

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))