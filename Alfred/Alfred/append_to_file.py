def append_to_file(text, file_name):
	"""
	"""

	with open(file_name, "a") as myfile:
		myfile.write(text)

