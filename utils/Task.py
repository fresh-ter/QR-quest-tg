import re


class Task:
	def getTaskNumberFromStart(start_message_argument):
		message = start_message_argument
		print("Parsing start message: ", message)

		if re.match("^task_\\d{,3}$", message):
			task_number = message[5:]
			if task_number.isdigit():
				task_number = int(task_number)
				print("Task number: ", task_number)
