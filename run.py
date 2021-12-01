from utils import UsersDB, TasksDB, SolutionsDB
import bot


def run_bot(usersDB, tasksDB, solutionsDB):
	bot.main(usersDB, tasksDB, solutionsDB)


def create_test_users(usersDB):
	usersDB.createAndAddNewUser('123', 'qwerty')
	usersDB.createAndAddNewUser('124')
	usersDB.createAndAddNewUser('125', 'test')
	usersDB.createAndAddNewUser('126', 'Steve')

def create_test_tasks(tasksDB):
	tasksDB.createAndAddNewTask("What is it?", "Linux", 1000)
	tasksDB.createAndAddNewTask("Who is it?", "Tux", 700)
	tasksDB.createAndAddNewTask("Where is it?", "Antarctica", 750)
	tasksDB.createAndAddNewTask("When is it?", "Now", 5000)


def main():
	usersDB = UsersDB()
	usersDB.start()

	tasksDB = TasksDB()
	tasksDB.start()

	solutionsDB = SolutionsDB()
	solutionsDB.start()

	# create_test_users(usersDB)
	# create_test_tasks(tasksDB)

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

	run_bot(usersDB, tasksDB, solutionsDB)


if __name__ == '__main__':
	main()
