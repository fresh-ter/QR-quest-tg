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

	def dumpToDict(self):
		d = {}

		d['id'] = self.ID

		d['tg_id'] = self.tg_id
		d['tg_name'] = self.tg_name
		d['tg_nicknamen'] = self.tg_nickname

		d['fname'] = self.fname
		d['lname'] = self.lname
		d['name'] = self.name

		d['score'] = self.score
		d['second_score'] = self.second_score

		d['status'] = self.status

		d['taskid_in_progress'] = self.taskid_in_progress

		return d

