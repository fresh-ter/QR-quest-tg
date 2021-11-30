from utils import TasksDB


def main():
	tasksDB = TasksDB()
	tasksDB.start()
	tasksDB.createAndAddNewTask("What is it?", "Linux", 1000)

	a = tasksDB.getTaskById(2)
	print(a.dumpToDict())

	print()
	b = a.processAnswer('Linux')
	print(b)
	b = a.processAnswer('linux')
	print(b)
	b = a.processAnswer('  lInUx  ')
	print(b)
	b = a.processAnswer('not linux')
	print(b)

	print()

	print(a.dumpToDict())



if __name__ == '__main__':
	main()
