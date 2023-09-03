import json
from utils import TasksDB, SolutionsDB, UsersDB

tasksDB = TasksDB()
tasksDB.start()


def create_task(task, answer):
    print('----------------------------')
    print()
    print(task)
    print()
    print('--------')
    print(answer)

    print('----------------------------')
    tasksDB.createAndAddNewTask(task, answer, 5000, min_coast=500)


def create_tasks():
    with open("quest/project.json", "r") as f:
        data = json.load(f)

    for x in data['tasks']:
        print('==========================')
        print()
        print("ID: ", x['id'])
        print("Hash: ", x['hash'])
        print()
        print(x['text'])
        print("Answer: ", x['answer'])
        print()
        print()

        create_task(x['text'], x['answer'])



def main():
    create_tasks()


if __name__ == '__main__':
    main()