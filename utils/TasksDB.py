import sqlite3
from .Task import Task

from json import dumps, loads


def createTaskFromResponse(response):
	task = Task(response[1], response[2], response[3])

	task.ID = response[0]

	task.current_coast = response[4]
	task.features = response[5]
	task.max_coast = response[6]
	task.min_coast = response[7]

	return task


class TasksDB:
	"""docstring for TasksDB"""
	def __init__(self, dbFile="Tasks.sqlite3"):
		self.mainTableName = 'tasks'

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
			'task TEXT NOT NULL,' + \
			'answer TEXT NOT NULL,' + \
			'coast INT NOT NULL,' + \
			'current_coast INT NOT NULL,' + \
			'features TEXT NOT NULL,' + \
			'max_coast INT NOT NULL,' + \
			'min_coast INT NOT NULL' + \
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

	def getTaskById(self, ID):
		request = 'SELECT * FROM ' + self.mainTableName + ' WHERE id = ?'

		cursor = self.conn.cursor()
		cursor.execute(request, (ID,))
		response = cursor.fetchall()

		print(response)

		if len(response) == 0:
			return None
		else:
			tasks = []
			for taskTuple in response:
				tasks.append(createTaskFromResponse(taskTuple))
			return tasks[0]

	def createAndAddNewTask(self, task, answer, coast,
			current_coast=None, features=None, max_coast=None, min_coast=None):
		task = str(task)
		answer = str(answer)
		coast = int(coast)

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

		ID = self.getLastID() + 1

		data = (ID, task, answer, coast, current_coast, features, max_coast,
			min_coast)


		request = 'INSERT INTO ' +  self.mainTableName + \
					'(id, task, answer, coast, current_coast, features,' + \
					'max_coast, min_coast)' + \
					'VALUES(?, ?, ?, ?, ?, ?, ?, ?)'

		cursor = self.conn.cursor()
		cursor.execute(request, data)
		self.commit()

		task = self.getTaskById(ID)
		return task

	def getNumberOfAll(self):
		request = 'SELECT count(*) FROM ' + self.mainTableName

		cursor = self.conn.cursor()
		cursor.execute(request)
		response = cursor.fetchone()

		return response[0]

	def updateCurrentCoastForTask(self, task):
		request = 'UPDATE ' + self.mainTableName + ' SET current_coast = ?' + \
					' WHERE id = ?'

		cursor = self.conn.cursor()
		cursor.execute(request, (task.getCurrentCoast(), task.getID()))
		self.commit()

