import sqlite3

class UsersDB:
	"""docstring for Users"""
	def __init__(self, dbFile="Users.sqlite3"):
		self.dbFile = dbFile

		self.conn = None

	def createAndConnect(self):
		self.conn = sqlite3.connect(self.dbFile)

		request = 'CREATE TABLE IF NOT EXISTS ' + 'users' + '(' + \
					'id INT PRIMARY KEY,' + \
					'tg_id TEXT,' + \
					'tg_name TEXT,' + \
					'tg_nickname TEXT,' + \
					'fname TEXT,' + \
					'lname TEXT,' + \
					'name TEXT,' + \
					'score INT,' + \
					'second_score INT,' + \
					'taskid_in_progress INT' + \
					')'

		cursor = self.conn.cursor()
		cursor.execute(request)
