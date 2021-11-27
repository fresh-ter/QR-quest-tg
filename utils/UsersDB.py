import sqlite3

class UsersDB:
	"""docstring for Users"""
	def __init__(self, dbFile="Users.sqlite3"):
		self.mainTableName = 'users'

		self.dbFile = dbFile
		self.conn = None
		self.lastID = 0

		self.maxLengthOfName = 16

	def commit(self):
		self.conn.commit()

	def connect(self):
		self.conn = sqlite3.connect(self.dbFile)

	def createTable(self):
		request = 'CREATE TABLE IF NOT EXISTS ' + self.mainTableName + '(' + \
					'id INT NOT NULL PRIMARY KEY,' + \
					'tg_id TEXT UNIQUE,' + \
					'tg_name TEXT,' + \
					'tg_nickname TEXT,' + \
					'fname TEXT,' + \
					'lname TEXT,' + \
					'name TEXT,' + \
					'score INT NOT NULL,' + \
					'second_score INT NOT NULL,' + \
					'status INT NOT NULL,' + \
					'taskid_in_progress INT' + \
					')'

		cursor = self.conn.cursor()
		cursor.execute(request)
		self.commit()

	def getLastID(self):
		request = 'SELECT max(id) FROM ' + self.mainTableName

		cursor = self.conn.cursor()
		cursor.execute(request)
		lastID = cursor.fetchone()[0]

		if lastID is None:
			lastID = 0

		return lastID

	def start(self):
		self.connect()
		self.createTable()

	def addNewUser(self, tg_id, tg_name=None, tg_nickname=None):
		tg_id = str(tg_id)
		name = str(name)
		tg_name = str(tg_name)
		tg_nickname = str(tg_nickname)

		ID = self.getLastID() + 1

		data = (ID, tg_id, tg_name, tg_nickname, 0, 0, 10)


		request = 'INSERT INTO ' +  self.mainTableName + \
					'(id, tg_id, tg_name, tg_nickname, score, second_score, status)' + \
					'VALUES(?, ?, ?, ?, ?, ?, ?)'

		cursor = self.conn.cursor()
		cursor.execute(request, data)
		self.commit()

	def isIdExists(self, ID):
		pass

