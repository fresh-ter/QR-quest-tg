class UserStatuses:
	READY = 10
	SENDS = 20
	SENDS_NAME = 21
	SENDS_FNAME = 22
	SENDS_LNAME = 23
	SENDS_ANSWER = 24


class User:
	"""docstring for User"""
	def __init__(self, tg_id, ID=None, status=10, taskid_in_progress=None):
		self.ID = ID

		self.tg_id = tg_id
		self.tg_name = None
		self.tg_nickname = None

		self.fname = None
		self.lname = None
		self.name = None

		self.score = 0
		self.second_score = 0

		self.status = status

		self.taskid_in_progress = taskid_in_progress

	def getID(self):
		return self.ID

	def dumpToDict(self):
		d = {}

		d['id'] = self.ID

		d['tg_id'] = self.tg_id
		d['tg_name'] = self.tg_name
		d['tg_nickname'] = self.tg_nickname

		d['fname'] = self.fname
		d['lname'] = self.lname
		d['name'] = self.name

		d['score'] = self.score
		d['second_score'] = self.second_score

		d['status'] = self.status

		d['taskid_in_progress'] = self.taskid_in_progress

		return d

	def addPoints(self, points, toMain=True):
		# if str(points).isdigit():
		# 	points = int(points)
		# else:
		# 	return

		if toMain:
			self.score += points
		else:
			self.second_score += points

	def getName(self):
		return str(self.name)

	def changeName(self, name):
		self.name = str(name)

	def getStatus(self):
		return self.status
	
	def changeStatus(self, status):
		self.status = status

	def getTaskID(self):
		return self.taskid_in_progress

	def changeTaskID(self, task_id):
		self.taskid_in_progress = int(task_id)
