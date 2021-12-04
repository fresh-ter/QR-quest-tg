from utils import TasksDB, SolutionsDB, UsersDB


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
	tasksDB = TasksDB()
	tasksDB.start()
	# tasksDB.createAndAddNewTask("What is it?", "Linux", 1000)

	solutionsDB = SolutionsDB()
	solutionsDB.start()
	# solutionsDB.createAndAddNewSolution(1, 4, 1, True)

	usersDB = UsersDB()
	usersDB.start()

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

	# a = tasksDB.getTaskById(4)
	# u = usersDB.getUserById(6)
	# print(a.dumpToDict())

	# print()
	# b = a.processAnswer('Linux')
	# print(b)
	# b = a.processAnswer('linux')
	# print(b)
	# b = a.processAnswer('  lInUx  ')
	# print(b)
	# b = a.processAnswer('not linux')
	# b = a.getTaskAsMessage()
	# print(b)
	# print("---------------")

	# a = solutionsDB.didUserAnswer(u, a)

	# print(a)

	# print(a.dumpToDict())

	t = tasksDB.getTaskById(4)
	print(t.getCurrentCoast())
	t.min_coast = 960
	t.updateCurrentCoast()
	t.updateCurrentCoast()
	t.updateCurrentCoast()
	t.updateCurrentCoast()
	t.updateCurrentCoast()
	t.updateCurrentCoast()
	t.updateCurrentCoast()
	print(t.getCurrentCoast())
	# tasksDB.updateCurrentCoastForTask(t)



if __name__ == '__main__':
	main()
