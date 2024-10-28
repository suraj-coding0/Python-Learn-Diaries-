import os

# os.rename("clutteredFolder/file.txt","clutteredFolder/self.txt")

files = os.listdir("clutteredFolder")       #print all files
i = 1
for file in files:
    if file.endswith(".png"):       #find png files
        print(file)
        os.rename(f"clutteredFolder/{file}",f"clutteredFolder/{i}.png")         #rename png files
        i = i+1