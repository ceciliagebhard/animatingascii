import os
import time

os.system('clear')
filenames = ["messi02.txt", "messi03.txt", "messi04.txt"]
frames = []

for name in filenames:
    with open(name, "r", encoding="utf8") as f:
        frames.append(f.readlines())
        
for frame in frames:
    print("".join(frame))
    time.sleep(1)
    os.system('clear')
