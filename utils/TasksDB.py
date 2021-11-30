import sqlite3
from .Task import Task


def createTaskFromResponse(response):
	pass


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
			'min_coast INT NOT NULL,' + \
			'id_solved TEXT NOT NULL,' + \
			'id_unsolved TEXT NOT NULL' + \
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

	def function(self):
		pass

