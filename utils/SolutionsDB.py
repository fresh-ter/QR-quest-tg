import sqlite3


def createSolutionFromResponse(response):
	pass


class SolutionsDB:
	"""docstring for SolutionDB"""
	def __init__(self, dbFile='Solutions.sqlite3'):
		self.mainTableName = 'solutions'

		self.dbFile = dbFile
		self.conn = None
		self.lastID = 0

	def commit(self):
		self.conn.commit()

	def connect(self):
		self.conn = sqlite3.connect(self.dbFile)

	def createTable(self):
		request = 'CREATE TABLE IF NOT EXISTS ' + self.mainTableName + '(' + \
			'id INT NOT NULL PRIMARY KEY,' + \
			'user_id INT NOT NULL,' + \
			'task_id TEXT NOT NULL,' + \
			'score INT NOT NULL,' + \
			'is_solved INT NOT NULL' + \
			')'

		cursor = self.conn.cursor()
		cursor.execute(request)
		self.commit()

	def start(self):
		self.connect()
		self.createTable()

	def getLastID(self):
		request = 'SELECT max(id) FROM ' + self.mainTableName

		cursor = self.conn.cursor()
		cursor.execute(request)
		lastID = cursor.fetchone()[0]

		if lastID is None:
			lastID = 0

		return lastID

	def isExistsID(self, ID):
		request = 'SELECT id FROM ' + self.mainTableName + ' WHERE id = ?'

		cursor = self.conn.cursor()
		cursor.execute(request, (ID,))
		response = cursor.fetchone()

		if response is None:
			return False
		elif response[0] == ID:
			return True

	def getSolutionById(self, ID):
		request = 'SELECT * FROM ' + self.mainTableName + ' WHERE id = ?'

		cursor = self.conn.cursor()
		cursor.execute(request, (ID,))
		response = cursor.fetchall()

		print(response)

		if len(response) == 0:
			return None
		else:
			solutions = []
			for solutionTuple in response:
				solutions.append(createSolutionFromResponse(solutionTuple))
			return solutions[0]

	def createAndAddNewSolution(self, user_id, task_id, score=0, is_solved=True):
		user_id = int(user_id)
		task_id = int(task_id)
		score = int(score)

		if is_solved:
			is_solved = 1
		else:
			is_solved = 0

		ID = self.getLastID() + 1

		data = (ID, user_id, task_id, score, is_solved)

		request = 'INSERT INTO ' +  self.mainTableName + \
					'(id, user_id, task_id, score, is_solved)' + \
					'VALUES(?, ?, ?, ?, ?)'

		cursor = self.conn.cursor()
		cursor.execute(request, data)
		self.commit()

		solution = self.getSolutionById(ID)
		return solution

	def didUserAnswer(self, task, user):
		response = False

		

		return response
