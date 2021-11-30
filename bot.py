from Penger.penger import Penger, Accordance
import tgbotSettings as tS

from time import sleep

from utils.task import Task
from utils import UserStatuses, interlocutor

# parcipantList = ["some_id"]

p = Penger(token = tS.token)
usersDB = None
taskDB = None


def isParcipant(tg_id):
	user = usersDB.getUserByTgId(tg_id)

	if user is None:
		return False
	else:
		return True


def getUser(tg_id):
	return usersDB.getUserByTgId(tg_id)


def isRegistrationEnabled():
	return True


def registerNewUser(tg_id):
	p.sendMessage(tg_id, interlocutor.registration['hello'][0])
	sleep(0.1)

	p.sendMessage(tg_id, "Registration...")
	sleep(0.1)
	user = usersDB.createAndAddNewUser(tg_id)

	print(user.dumpToDict())

	p.sendMessage(tg_id, interlocutor.registration['enter_name'][0])
	sleep(0.1)
	user.changeStatus(UserStatuses.SENDS_NAME)
	usersDB.updateUser(user)

	# p.senderWhitelist.append(tg_id)


def registrationClosed(tg_id):
	p.sendMessage(tg_id, "Hello!")


def start_for_parcipant(tg_id):
	user = usersDB.getUserByTgId(tg_id)
	p.sendMessage(user.tg_id, "Hello, "+user.getName()+"!")


def start_command(self):
	tg_id = self.data["sender_id"]
	user = getUser(tg_id)
	print(self.data)

	command_arr = self.data['text'].split()

	if len(command_arr) == 1:
		tg_id = self.data["sender_id"]

		if user is None:
			if isRegistrationEnabled():
				registerNewUser(tg_id)
			else:
				registrationClosed(tg_id)
		else:
			start_for_parcipant(tg_id)
	else:
		if command_arr[1][:4] == "task" and user is not None:
			p.sendMessage(tg_id, 'This is task')
			Task.getTaskNumberFromStart(start_message_argument=command_arr[1])
		else:
			p.sendMessage(tg_id, 'I do not understand...')


def help_for_parcipant(user):
	p.sendMessage(user.tg_id, interlocutor.help_text[0])


def help_command(self):
	tg_id = self.data["sender_id"]
	user = usersDB.getUserByTgId(tg_id)

	if user is not None:
		help_for_parcipant(user)
	else:
		p.sendMessageToChat(self.data, "This is help")


def score_for_parcipant(user):
	p.sendMessage(user.tg_id, "This is score")


def score_command(self):
	tg_id = self.data["sender_id"]
	user = usersDB.getUserByTgId(tg_id)

	if user is not None:
		score_for_parcipant(user)
	else:
		p.sendMessageToChat(self.data, 'I do not understand...')


def empty_for_parcipant(user, message):
	print(message)
	userStatus = user.getStatus()

	answer = "Status error.\nWrite to tech support - it's interesting."

	if userStatus == UserStatuses.READY:
		answer = interlocutor.others["ready"][0]
	elif userStatus == UserStatuses.SENDS_NAME:
		user.changeName(interlocutor.get_validated_name(message))
		user.changeStatus(UserStatuses.READY)
		usersDB.updateUser(user)
		answer = interlocutor.others["sends_name"][0]

	p.sendMessage(user.tg_id, answer)
		


def empty(self):
	tg_id = self.data["sender_id"]
	user = usersDB.getUserByTgId(tg_id)

	if user is not None:
		empty_for_parcipant(user, self.data["text"])
	else:
		p.sendMessageToChat(self.data, 'I do not understand...')


p.accordance = [
	Accordance('/start', start_command, 'all:all', enableArgument=True),
	Accordance('/help', help_command, 'all:all', enableArgument=True),
	Accordance('/score', score_command, 'all:all', enableArgument=True)
]
p.emptyAccordance = Accordance('', empty, 'all:all', enableArgument=True)


def main(u):
	global usersDB
	usersDB = u

	while True:
		p.updateAndRespond()
		sleep(10)


# if __name__ == '__main__':
# 	main()
