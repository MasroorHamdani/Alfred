def append_to_file(text):
	"""
	"""

	with open("im_code.txt", "a") as myfile:
		myfile.write(text)
