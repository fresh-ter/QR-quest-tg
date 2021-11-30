import re


def getTaskNumberFromStart(start_message_argument):
		message = start_message_argument
		print("Parsing start message: ", message)

		if re.match("^task_\\d{,3}$", message):
			task_number = message[5:]
			if task_number.isdigit():
				task_number = int(task_number)
				print("Task number: ", task_number)


class Task:
	"""docstring for Task"""
	def __init__(self, task, answer, coast, ID=None, current_coast=None,
			features=None, max_coast=None, min_coast=None, id_solved=None,
			id_unsolved=None):
		self.ID = ID

		self.task = task
		self.answer = answer
		self.coast = coast

		if current_coast is None:
			current_coast = coast
		else:
			current_coast = int(current_coast)

		if features is None:
			features = "plain"
		else:
			features = str(features)

		if max_coast is None:
			max_coast = coast
		else:
			max_coast = int(max_coast)

		if min_coast is None:
			min_coast = coast
		else:
			min_coast = int(min_coast)

		if id_solved is None:
			id_solved = []

		if id_unsolved is None:
			id_unsolved = []

	def dumpToDict(self):
		d = {}

		d['id'] = self.ID

		d['task'] = self.task
		d['answer'] = self.answer
		d['coast'] = self.coast

		d['current_coast'] = self.current_coast

		d['features'] = self.features

		d['max_coast'] = self.max_coast
		d['min_coast'] = self.min_coast

		d['id_solved'] = self.id_solved
		d['id_unsolved'] = self.id_unsolved

		return d

	def getID(self):
		return self.ID

	def getCurrentCoast(self):
		return self.current_coast

	def addIDSolved(self, ID):
		self.id_solved.append(ID)

	def addIDUnsolved(self, ID):
		self.id_unsolved.append(ID)

	def isCorrectAnswer(self, _answer):
		_answer = str(_answer)

		response = False

		if self.features == "plain":
			if _answer.replace(" ", '').lower() == self.answer.replace(" ", '').lower():
				response = True

		return response


	def processAnswer(self, answer):
		isCorrectAnswer = self.isCorrectAnswer(answer)

		print("Answer: ", answer, "  Correct: ", isCorrectAnswer)

		return isCorrectAnswer

