from pygame import mixer

# wyswietlenie listy komend

komendy = open('komendy.txt', 'r')
print(komendy.read())
komendy.close()
print("\n")

# wyswietlenie listy dostepnych utworow
lista = open('lista.txt', 'r')
print(lista.read())
lista.close()


mixer.init()

# wybor utworu
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
        current_song = command+'.mp3'
        mixer.music.load(current_song)
        mixer.music.set_volume(volume_lvl)
        mixer.music.play()
        print("p/u/e/v")
        # operacja na utworze, wstrzymanie wznowienie zakonczenie zmiana glosnosci
        while True:

            order = input("  ")

            if order == 'p':

                # Pausing the music
                mixer.music.pause()
            elif order == 'u':

                # Resuming the music
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
