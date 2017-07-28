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
	os.system('wmctrl -a pycharm')
	keyboard.press(keystroke)
	time.sleep(0.690)
	keyboard.release(keystroke)
	return

def add_text(text):
	"""
	"""
	os.system('wmctrl -a pycharm')
	keyboard.type(text)

if __name__ == "__main__":
	manage_keystrokes("enter")