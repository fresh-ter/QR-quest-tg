from utils import TasksDB, SolutionsDB, UsersDB


def main():
	tasksDB = TasksDB()
	tasksDB.start()
	# tasksDB.createAndAddNewTask("What is it?", "Linux", 1000)

	solutionsDB = SolutionsDB()
	solutionsDB.start()
	# solutionsDB.createAndAddNewSolution(1, 4, 1, True)

	usersDB = UsersDB()
	usersDB.start()

	a = tasksDB.getTaskById(4)
	u = usersDB.getUserById(6)
	# print(a.dumpToDict())

	# print()
	# b = a.processAnswer('Linux')
	# print(b)
	# b = a.processAnswer('linux')
	# print(b)
	# b = a.processAnswer('  lInUx  ')
	# print(b)
	# b = a.processAnswer('not linux')
	b = a.getTaskAsMessage()
	print(b)
	print("---------------")

	a = solutionsDB.didUserAnswer(u, a)

	print(a)

	# print(a.dumpToDict())



if __name__ == '__main__':
	main()
