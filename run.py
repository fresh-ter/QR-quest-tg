from utils import UsersDB
import bot


def run_bot(usersDB):
	bot.main(usersDB)


def create_test_users(usersDB):
	usersDB.createAndAddNewUser('123', 'qwerty')
	usersDB.createAndAddNewUser('124')
	usersDB.createAndAddNewUser('125', 'test')
	usersDB.createAndAddNewUser('126', 'Steve')


def main():
	usersDB = UsersDB()
	usersDB.start()

	# create_test_users(usersDB)

	a = usersDB.getLastID()
	print(a)

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

	run_bot(usersDB)


if __name__ == '__main__':
	main()
