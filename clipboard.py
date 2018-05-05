from pyhooked import Hook, KeyboardEvent, MouseEvent
import pyperclip, pyautogui

clipper = {}

def ctrlC():
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')

def ctrlV():
    pyautogui.keyDown('ctrl')
    pyautogui.tap('v')
    pyautogui.keyUp('ctrl')

def handle_events(args):
    if isinstance(args, KeyboardEvent):
        print(args.key_code)
        if args.current_key == 'Q' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
            print('Quitting.')
            raise SystemExit
        if args.current_key == 'C' and args.event_type == 'key down' and 'Lshift' in args.pressed_key:
            if 'F1' in args.pressed_key:
                print("shift C F1")
                ctrlC()
                clipper['1'] = pyperclip.paste()
            elif 'F2' in args.pressed_key:
                print("shift C F2")
                ctrlC()
                clipper['2'] = pyperclip.paste()
            elif 'F3' in args.pressed_key:
                print("shift C F3")
                ctrlC()
                clipper['3'] = pyperclip.paste()
            elif 'F4' in args.pressed_key:
                print("shift C F4")
                ctrlC()
                clipper['4'] = pyperclip.paste()
            elif 'F5' in args.pressed_key:
                print("shift C F5")
                ctrlC()
                clipper['5'] = pyperclip.paste()

        if args.current_key == 'V' and args.event_type == 'key down' and 'Lshift' in args.pressed_key:
            if 'F1' in args.pressed_key:
                print("shift V F1")
                pyperclip.copy(clipper["1"])
                ctrlV()
            elif 'F2' in args.pressed_key:
                print("shift V F2")
                pyperclip.copy(clipper["2"])
                ctrlV()
            elif 'F3' in args.pressed_key:
                print("shift V F3")
                pyperclip.copy(clipper["3"])
                ctrlV()
            elif 'F4' in args.pressed_key:
                print("shift V F4")
                pyperclip.copy(clipper["4"])
                ctrlV()
            elif 'F5' in args.pressed_key:
                print("shift V F5")
                pyperclip.copy(clipper["5"])
                ctrlV()

hk = Hook()  # make a new instance of PyHooked
hk.handler = handle_events  # add a new shortcut ctrl+a, or triggered on mouseover of (300,400)
hk.hook()  # hook into the events, and listen to the presses