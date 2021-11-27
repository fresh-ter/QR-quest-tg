from Penger.penger import Penger, Accordance
import tgbotSettings as tS
from time import sleep

from utils.task import Task
from utils import UsersDB, User, interlocutor


p = Penger(token = tS.token)
usersDB = None
taskDB = None


def registerNewUser(tg_id):
	p.sendMessage(tg_id, interlocutor.registration['hello'][0])
	sleep(0.1)

	p.sendMessage(tg_id, "Registration...")
	sleep(0.1)
	user = usersDB.createAndAddNewUser(tg_id)

	print(user.dumpToDict())

	p.sendMessage(tg_id, interlocutor.registration['enter_name'][0])
	sleep(0.1)
	


def start_command(self):
	print(self.data)

	if self.data['text'] == "/start":
		tg_id = self.data["sender_id"]
		user = usersDB.getUserByTgId(tg_id)

		if user is None:
			registerNewUser(tg_id)
		else:
			p.sendMessage(tg_id, "Hello")
		
	else:
		command_args = self.data['text'].split()
		if len(command_args) > 1:
			arg = str(command_args[1])

			if arg[:4] == "task":
				Task.getTaskNumberFromStart(start_message_argument=arg)


def empty(data):
	p.sendMessageToChat(data, 'I do not understand...')


p.accordance = [
	Accordance('/start', start_command, 'all:all', enableArgument=True),
]
p.emptyAccordance = empty


def main(u):
	global usersDB
	usersDB = u

	while True:
		p.updateAndRespond()
		sleep(10)


# if __name__ == '__main__':
# 	main()
