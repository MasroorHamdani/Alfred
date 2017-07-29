import os
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

def manage_keystrokes(key):
	"""
	"""
	if key=="enter":
		press_keystroke(Key.enter)
		return

	elif key=="up":
		press_keystroke(Key.up)
		return

	elif key=="down":
		press_keystroke(Key.down)
		return

	elif key=="left":
		press_keystroke(Key.left)
		return

	elif key=="right":
		press_keystroke(Key.right)
		return

	elif key=="space":
		press_keystroke(Key.space)
		return

	elif key=="backspace":
		press_keystroke(Key.backspace)
		return

	elif key=="tab":
		press_keystroke(Key.tab)
		return

def press_keystroke(keystroke):
	"""
	"""
	time.sleep(1)
	os.system('wmctrl -a gedit')
	keyboard.press(keystroke)
	time.sleep(0.500)
	keyboard.release(keystroke)
	return

def add_text(text):
	"""
	"""
	os.system('wmctrl -a gedit')
	time.sleep(1)
	if text:
		if "nl" in text:
			keyboard.type(text.split("nl")[0])
			manage_keystrokes("enter")
			manage_keystrokes("tab")
			keyboard.type(text.split("tab")[1])
		else:
			keyboard.type(text)
		manage_keystrokes("enter")

	with keyboard.pressed(Key.ctrl):
		keyboard.press('s')
		keyboard.release('s')


