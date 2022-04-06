import sqlite3
from .User import User


def createUserFromResponse(response):
	user = User(response[1])
	user.ID = response[0]

	user.tg_name = response[2]
	user.tg_nickname = response[3]

	user.fname = response[4]
	user.lname = response[5]
	user.name = response[6]

	user.score = response[7]
	user.second_score = response[8]

	user.status = response[9]

	user.taskid_in_progress = response[10]

	return user


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

	def isExistsID(self, ID):
		request = 'SELECT id FROM ' + self.mainTableName + ' WHERE id = ?'

		cursor = self.conn.cursor()
		cursor.execute(request, (ID,))
		response = cursor.fetchone()

		if response is None:
			return False
		elif response[0] == ID:
			return True

	def getUsersBy(self, request, value):
		cursor = self.conn.cursor()
		cursor.execute(request, value)
		response = cursor.fetchall()

		# print(response)

		if len(response) == 0:
			return [None]
		else:
			users = []
			for userTuple in response:
				users.append(createUserFromResponse(userTuple))

			return users

	def getUserById(self, ID):
		request = 'SELECT * FROM ' + self.mainTableName + ' WHERE id = ?'

		return self.getUsersBy(request, (ID,))[0]

	def getUserByTgId(self, tg_id):
		request = 'SELECT * FROM ' + self.mainTableName + ' WHERE tg_id = ?'

		return self.getUsersBy(request, (tg_id,))[0]

	def start(self):
		self.connect()
		self.createTable()

	def createAndAddNewUser(self, tg_id, tg_name=None, tg_nickname=None):
		tg_id = str(tg_id)
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

		user = self.getUserById(ID)
		return user

	def _updateValue(self, ID, _valueName, newValue):
		request = 'UPDATE ' + self.mainTableName + ' SET ' + _valueName + ' = ?' + \
					' WHERE id = ?'

		cursor = self.conn.cursor()
		cursor.execute(request, (newValue, ID))
		self.commit()

	def updateUser(self, user):
		userID = user.getID()
		existingUser = self.getUserById(userID)

		if existingUser is None:
			return False

		if existingUser.tg_name != user.tg_name:
			self._updateValue(userID, 'tg_name', user.tg_name)

		if existingUser.tg_nickname != user.tg_nickname:
			self._updateValue(userID, 'tg_nickname', user.tg_nickname)

		if existingUser.fname != user.fname:
			self._updateValue(userID, 'fname', user.fname)

		if existingUser.lname != user.lname:
			self._updateValue(userID, 'lname', user.lname)

		if existingUser.name != user.name:
			self._updateValue(userID, 'name', user.name)

		if existingUser.score != user.score:
			self._updateValue(userID, 'score', user.score)

		if existingUser.second_score != user.second_score:
			self._updateValue(userID, 'second_score', user.second_score)

		if existingUser.status != user.status:
			self._updateValue(userID, 'status', user.status)

		if existingUser.taskid_in_progress != user.taskid_in_progress:
			self._updateValue(userID, 'taskid_in_progress', user.taskid_in_progress)

	def updateUserStatus(self, user):
		userID = user.getID()
		existingUser = self.getUserById(userID)

		if existingUser is None:
			return False

		if existingUser.status != user.status:
			self._updateValue(userID, 'status', user.status)

	def top10byScoreDict(self):
		request = 'SELECT id, score FROM ' + self.mainTableName + ' ORDER BY score DESC LIMIT 5'

		cursor = self.conn.cursor()
		cursor.execute(request)
		response = cursor.fetchall()

		print(response)

		if len(response) == 0:
			return None
		else:
			d = {}

			# id: score
			for x in response:
				d[x[0]] = x[1]

			return d
