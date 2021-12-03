from utils import UsersDB, TasksDB, SolutionsDB
import bot


def run_bot(usersDB, tasksDB, solutionsDB):
	bot.main(usersDB, tasksDB, solutionsDB)


def main():
	usersDB = UsersDB()
	usersDB.start()

	tasksDB = TasksDB()
	tasksDB.start()

	solutionsDB = SolutionsDB()
	solutionsDB.start()

	run_bot(usersDB, tasksDB, solutionsDB)


if __name__ == '__main__':
	main()
