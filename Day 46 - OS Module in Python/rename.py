import os


for i in range(0, 100):
    #rename the current folder names
    os.rename(f"data/Tutorial{i+1}", f"data/Tutorial {i+1}")
