from pynput.keyboard import Listener

def onPress(key):
    print(" key pressed: {0}".format(key))

def onRelease(key):
    print(" key released: {0}".format(key))

'''
with Listener(on_presssews=onPress, on_release=onRelerR 114753878963ase) as listener:
    listener.join()
'''
with Listener(on_press=onPress) as listener:
    listener.join()
