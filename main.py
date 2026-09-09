import os
from playsound3 import playsound


print('Welcome to pusic player')
print('Version 0.1')

i = input('enter 1.play music 2.search music 3.delete music 4.exit: ')


def search_music():
    music_name = input('enter music name: ')
    home = os.path.expanduser('~')

    for root, dirs, files in os.walk(home):
        for file in files:
            if file.lower() == music_name.lower():
                path = os.path.join(root, file)
                print(f'Found: {path}')
                return path

    print('Music not found')
    return None


def play_music(path):
    playsound(path)


def delete_music():
    music_name = input('enter music name: ')

    if not music_name.lower().endswith('.mp3'):
        print('Only MP3 files are allowed')
        return

    home = os.path.expanduser('~')

    for root, dirs, files in os.walk(home):
        for file in files:
            if file.lower() == music_name.lower():
                path = os.path.join(root, file)
                os.remove(path)
                print(f'Deleted: {path}')
                return

    print('Music not found')


if i == "1":
    j = input('enter music directory: ')
    play_music(j)

if i == "2":
    search_music()

if i == "3":
    delete_music()

if i == "4":
    print('Goodbye!')