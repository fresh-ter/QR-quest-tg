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
