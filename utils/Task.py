from .interlocutor import task_presentation

class Task:
	"""docstring for Task"""
	def __init__(self, task, answer, coast, ID=None, current_coast=None,
			features=None, max_coast=None, min_coast=None):
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

	def isCorrectAnswer(self, _answer):
		_answer = str(_answer)

		response = False

		if self.features == "plain":
			if _answer.replace(" ", '').lower() == self.answer.replace(" ", '').lower():
				response = True

		return response

	def getTaskAsMessage(self, lang=0):
		message = task_presentation['start'][lang]
		message += str(self.ID) + task_presentation['start_1'][lang]

		message += '> '
		message += self.task
		message += '\n\n'

		# if "plain" in self.features:
		# 	message += task_presentation["answer_plain_abc"][lang]

		message += task_presentation["answer_stop"][lang]

		return message

	def processAnswer(self, _answer):
		isCorrectAnswer = self.isCorrectAnswer(_answer)

		points = self.getCurrentCoast


		print("Answer: ", _answer, "  Correct: ", isCorrectAnswer)

		return isCorrectAnswer, points

