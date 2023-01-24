import os
import time

os.system('clear')
# PUT INTO THIS LIST THE TXT FILES THAT CONTAINS THE FRAMES TO BE USED FOR THE ANIMATION
filenames = ["messi01.txt", "messi02.txt", "messi03.txt"]
frames = []

for name in filenames:
    with open(name, "r", encoding="utf8") as f:
        frames.append(f.readlines())
        
for frame in frames:
    print("".join(frame))
    time.sleep(1)
    os.system('clear')
