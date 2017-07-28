import pyttsx

class Executioner(object):
	def __init__(self, text):
		self.text = text

	def speak(self):
		engine = pyttsx.init()
		rate = engine.getProperty('rate')
		engine.setProperty('rate', rate-50)
		engine.say('Less chit-chat and more demo')
		engine.runAndWait()

	def printText(self):
		print (self.text)

