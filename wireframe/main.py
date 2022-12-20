from pygame import mixer

# commands list
komendy = open('commands.txt', 'r')
print(komendy.read())
komendy.close()
print("\n")

# track list
import os
songs = []
i = 1
for x in os.listdir():
    if x.endswith(".mp3"):
        song_name = x.split('.mp3')
        print(i, song_name[0])
        songs.append(x)
        i+=1

mixer.init()
# track operations
while True:
    volume_lvl = float(0.5)

    command = str(input())
    if command == 'v':
        volume_lvl = input()
    if command == 'c':
        break
    elif command == '':
        continue
    else:
        current_song = songs[int(command)-1]
        mixer.music.load(current_song)
        mixer.music.set_volume(volume_lvl)
        mixer.music.play()
        print("p/u/e/v")
        # pause, unpause, close, change volume
        while True:

            order = input("  ")

            if order == 'p':

                # Pausing the music
                mixer.music.pause()
            elif order == 'u':

                # Unpause the music
                mixer.music.unpause()
            elif order == 'e':

                # Stop the mixer
                mixer.music.stop()
                break
            elif order == 'v':
                volume_lvl = float(input())
                mixer.music.set_volume(volume_lvl)
            else:
                continue
