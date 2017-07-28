import os
import subprocess
import pyttsx

class Executioner(object):
	def __init__(self, text=None, file_name=None):
		self.text = text
		self.file_name = file_name

	def speak(self):
		engine = pyttsx.init()
		rate = engine.getProperty('rate')
		engine.setProperty('rate', rate-50)
		engine.say('Less chit-chat and more demo')
		engine.runAndWait()

	def printText(self):
		print (self.text)


	def run_my_code(self):
		"""
		"""
		try:
			return execfile(self.file_name)
		except Exception as ex:
			print("caught exception")
			return str(ex)
			





