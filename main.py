import os
from playsound3 import playsound


print('Welcome to pusic player')
print('Version 0.2')



def search_music():
    music_name = input('enter music name: ')
    if not music_name.lower().endswith('.mp3'):
        music_name += '.mp3'
    home = os.path.expanduser('~')
    result = []

    for root, dirs, files in os.walk(home):
        for file in files:
            if file.lower() == music_name.lower():
                path = os.path.join(root, file)
                result.append(path)
                print(f'Found: {path}')

    if not result:
        print('Music not found')
        return None

    for number, path in enumerate(result, start=1):
        print(f'{number}. {path}')

    try:
        choice = int(input('Choose music: '))
    except ValueError:
        print('enter valid number')
    else:
        if choice < 1 or choice > len(result):
            print('invalid choice')
        else:
            return result[choice - 1]


def play_music(path):
    sound = playsound(path, block=False)
    return sound


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
                confirm = input('Are you sure you want to delete this file? (y/n): ')

                if confirm.lower() == 'y':
                    os.remove(path)
                    print(f'Deleted: {path}')
                else:
                    print('deletation cancelled')
                    return
                print('music not found')


while True:
    i = input('enter 1.play music 2.search music 3.delete music 4.exit: ')
        
    if i == "1":
        path = search_music()
        if path is None:
            print('music not found')
        else:
            sound = play_music(path)

            while True:
                control = input('1. Stop 2. Back: ')

                if control == "1":
                    sound.stop()
                    print('Music stopped')
                    break
                elif control == "2":
                    break
                else:
                    print('invalid choice')

    if i == "2":
        search_music()

    if i == "3":
        delete_music()

    if i == "4":
        print('Goodbye!')
        break