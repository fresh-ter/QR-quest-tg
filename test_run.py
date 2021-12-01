from utils import TasksDB, SolutionsDB


def main():
	tasksDB = TasksDB()
	tasksDB.start()
	tasksDB.createAndAddNewTask("What is it?", "Linux", 1000)

	solutionsDB = SolutionsDB()
	solutionsDB.start()
	solutionsDB.createAndAddNewSolution(1, 4, 1, True)

	a = tasksDB.getTaskById(2)
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

	# print()

	# print(a.dumpToDict())



if __name__ == '__main__':
	main()
