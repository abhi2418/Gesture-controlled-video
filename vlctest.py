import vlc
import time
import os
tracks = []

path = r"/home/katniss/Downloads/Movies/test"
songs = os.listdir(path)
#print(songs)
        
for s in songs:
    if '.mp4' in s:
        des = path + '/' + s
        print(des)

p = "/home/katniss/Downloads/Movies/test/Shutter.Island.mp4"
#os.system("cvlc"+" /home/katniss/Downloads/Movies/test/Shutter.Island.mp4")

os.system(f"vlc-ctrl play -p {p}")

os.system("vlc-ctrl volume +10%")
os.system("vlc-ctrl volume +20%")
os.system("vlc-ctrl volume -5%")
print("DONE")


# start playing video
