import os
import time

os.system('clear')
# PUT INTO THIS LIST THE TXT FILES THAT CONTAINS THE FRAMES TO BE USED FOR THE ANIMATION
filenames = ["messi01.txt", "messi02.txt", "messi03.txt"]
frames = []

for name in filenames:
    with open(name, "r", encoding="utf8") as f:
        frames.append(f.readlines())

        
while frames: # I have added this while loop to keep the frames in a loop. 
              # You can STOP the ejecution of the animation by closing the TERMINAL or deleting the terminal in VSCode
              # It doesn't consume any memory from the computer, since the frames are made of txt. 

    
    for frame in frames:
        print("".join(frame))
        time.sleep(1)
        os.system('clear')        

"""for frame in frames:
    print("".join(frame))
    time.sleep(1)
    os.system('clear')"""
