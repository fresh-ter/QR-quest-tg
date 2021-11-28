from utils import UsersDB
import bot


def run_bot(usersDB):
	bot.main(usersDB)


def main():
	usersDB = UsersDB()
	usersDB.start()

	a = usersDB.getLastID()
	print(a)

	#usersDB.addNewUser('12345', 'qwerty')

	a = usersDB.getUserByTgId("123")

	a.addPoints(50)
	a.fname = 'Eliot'
	a.changeName('eliot')
	a.changeStatus(21)
	usersDB.updateUser(a)

	# if a is not None:
	# 	print(a.dumpToDict())
	# else:
	# 	print(a)

	# a = usersDB.isExistsID(5)
	# print(a)

	# usersDB._updateValue(4, 'score', '50')

	# run_bot(usersDB)


if __name__ == '__main__':
	main()
