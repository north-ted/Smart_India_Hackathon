import time

from pygame.time import delay

import gesture as gs
from tkinter import *                          #import statements
# import tasks as task
from pynput.keyboard import Key,Controller
import win32api
from win32con import *
keyboard = Controller()

num=1


def systemsetting():                         #system settings
    prev=0
    finger=gesture1.hands()
    while finger != 5:
        finger = gesture1.hands()
        # prev=finger
        direct = gesture1.direction()
        if finger == 1:                           #1 for volume up and down
            prev = 1
            if direct == 0:
                keyboard.press(Key.media_volume_up)
            elif direct == 1:
                keyboard.press(Key.media_volume_down)
        elif finger == 2:                                  #2 for volume mute and unmute

            if prev != finger:
                prev = 2
                keyboard.press(Key.media_volume_mute)

        elif finger == 3:                        #3 for play/pause

            if prev != finger:
                prev = 3
                keyboard.press(Key.media_play_pause)

        elif finger == 4:  # to fast forward and revert back while playing youtube video
            if direct == 2:
                keyboard.press("l")
            elif direct == 3:
                keyboard.press("j")

        else :
            prev = finger
    prev =5
    return

def photo_viewer():                         #system settings
    prev=0
    finger=gesture1.hands()
    while finger != 5:
        finger = gesture1.hands()
        # prev=finger
        direct = gesture1.direction()
        if finger == 1:                           #1 for volume up and down
            prev = 1
            if direct == 2 :
                keyboard.press(Key.left)
                keyboard.release(Key.left)
            if direct == 3:
                keyboard.press(Key.right)
                keyboard.release(Key.right)
            elif direct == 0:
                keyboard.press(Key.up)
                keyboard.release(Key.up)
            elif direct == 1:
                keyboard.press(Key.down)
                keyboard.release(Key.down)
        elif finger == 2:                                  #2 for volume mute and unmute

            newpos = win32api.GetCursorPos()

            if direct == 4:
                for i in range(0,200):
                    keyboard.press(Key.ctrl)
                    win32api.mouse_event(MOUSEEVENTF_WHEEL,newpos[0],newpos[1], -1, 0)
                    print("gggggggggggggggggggg")
            elif direct ==5:
                for i in range(0,200):
                    keyboard.press(Key.ctrl)
                    win32api.mouse_event(MOUSEEVENTF_WHEEL,newpos[0],newpos[1], 1, 0)
                    print("gggggggggggggggggggg")

                # print(newpos)
            if prev != finger:
                prev = 2



        else :
            prev = finger
            keyboard.release(Key.ctrl)
    prev =5
    return


def mp3player():     #method for mp3 player
    root = Tk()
    player = task.MusicPlayer(root)
    prev = 0
    finger = gesture1.hands()
    num =1

    while finger != 5 :
        delay(2)
        finger = gesture1.hands()
        direct = gesture1.direction()
        root.update()
        if finger == 1:                           #1 for volume up and down based on direction of finger
            prev = 1
            if direct == 0:
                player.volup()
            elif direct == 1:
                player.voldown()


        elif finger == 2:                     #2 for song select
            if direct == 0 and prev != finger:
                prev = 2
                player.nextSong()
            elif direct == 1 and prev != finger:
                prev=2
                player.prevSong()





        elif finger == 3:                         #3 for pause/play
            # print('31')
            if prev != finger and num == 1:
                prev = 3
                player.play()
                num = 0
                # print('play')

            elif prev != finger and num == 0:
                prev = 3
                player.pause()
                num=0
        elif finger==4:                                #4 to stop the mp3 player
            # print('41')
            # player.stop()
            prev=5
            # return
        else:
            prev = finger

    player.stop()
    root.destroy()
    prev =5
    return

def document():
    prev = 0
    finger = gesture1.hands()
    while finger !=5 :
        finger = gesture1.hands()
        direct = gesture1.direction()
        if finger == 1:      # 1 for volume up and down based on direction of finger
            prev = 1
            if direct == 0:
                keyboard.press(Key.page_up)
                keyboard.release(Key.page_up)
            elif direct == 1:
                keyboard.press(Key.page_down)
                keyboard.release(Key.page_down)
        elif finger == 2:
            prev = 2
            keyboard.press(Key.f12)
        elif finger == 3 and prev != finger:
            prev = 3
            keyboard.press(Key.ctrl)
            keyboard.press("p")
            keyboard.release(Key.ctrl)
        elif finger == 4 and prev != finger:
            prev = 4
            keyboard.press(Key.alt)
            keyboard.press(Key.f4)
            keyboard.press(Key.enter)
            keyboard.release(Key.alt)
        else:
            prev = finger







gesture1 = gs.gesture()

while True:                                    #loop for identifying number of fingers and starting the task
    gesture1.hands()
    # print(gs.totalFingers)                    # 1 for system settings
                 # 2 for mp3 player
    # if num_fingers == 0:

    num_fingers=gs.totalFingers
    while num_fingers != 5:
        gesture1.hands()
        num_fingers = gs.totalFingers
        fingers = []
        print(num_fingers)
        if num_fingers == 1:
            systemsetting()
        # if num_fingers == 2:
        #     mp3player()
        if num_fingers == 2:
            photo_viewer()

        if num_fingers == 3:
            document()







