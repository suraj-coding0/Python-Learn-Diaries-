import os

class ClearTheCulture:
    def create(self):
         if (not os.path.exists("Folder")):
            os.mkdir("Folder")
            for i in range(0,5):
                os.mkdir(f"Folder/nfejnifuqiu {i+1}")

    def rename(self):
        for i in range(0,5):
            os.rename(f"Folder/nfejnifuqiu {i+1}", f"Folder/{i+1}.png")

obj = ClearTheCulture()
obj.create()
obj.rename()