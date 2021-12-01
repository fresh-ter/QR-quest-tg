from Penger.penger import Penger, Accordance
import tgbotSettings as tS

from time import sleep

from utils import UserStatuses, interlocutor


# parcipantList = ["some_id"]

p = Penger(token = tS.token)
usersDB = None
tasksDB = None
solutionsDB = None


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


def getUserStatusAsMessage(user):
	userStatus = user.getStatus()
	message = ""

	message += interlocutor.me_command['status'][0]

	if userStatus == UserStatuses.READY:
		message += interlocutor.status['ready'][0]
	elif userStatus == UserStatuses.SENDS_NAME:
		message += interlocutor.status['sends_name'][0]
	elif userStatus == UserStatuses.SENDS_ANSWER:
		message += interlocutor.status['sends_answer'][0]
		message += str(user.getTaskID())
	elif userStatus == UserStatuses.SENDS_TASKID:
		message += interlocutor.status['sends_taskid'][0]
	else:
		message += "Status not defined"

	return message


def printTask(task, user):
	message = task.getTaskAsMessage()

	user.changeStatus(UserStatuses.SENDS_ANSWER)
	user.changeTaskID(task.getID())
	usersDB.updateUser(user)

	return message


def answer_stop(user):
	message = interlocutor.others['answer_stop'][0]

	user.changeStatus(UserStatuses.READY)
	usersDB.updateUser(user)
	
	return message


def processUserAnswer(vAnswer, user):
	message = ''

	task = tasksDB.getTaskById(user.getTaskID())

	if task is None:
		message = "This task no longer exists :-("
	else:
		isCorrect, points = task.processAnswer(vAnswer)

		user.addPoints(points)
		user.changeStatus(UserStatuses.READY)
		usersDB.updateUser(user)

		solutionsDB.createAndAddNewSolution(user.getID(), task.getID(),
			points, isCorrect)

		message += interlocutor.task_answer['start'][0]
		message += str(task.getID()) + "\n\n"


		if isCorrect:
			message += interlocutor.task_answer['ok'][0]
		else:
			message += interlocutor.task_answer['not_ok'][0]

		message += interlocutor.task_answer['points'][0]
		message += str(points)

	return message


def taskIDEnter(text, user):
	botAnswer = ''

	taskID = interlocutor.getTaskIDFromText(text)

	if taskID is None:
		botAnswer = 'Error: Invalid link or parameter.'
	else:
		task = tasksDB.getTaskById(taskID)
		if task is None:
			botAnswer = 'Ahaha, 404 Error: Task not found.'
		else:
			botAnswer = printTask(task, user)

	return botAnswer


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
			print("Parsing start message: ", command_arr[1])

			taskID = interlocutor.getTaskIDFromStart(command_arr[1])
			if taskID is None:
				p.sendMessage(tg_id, 'Error: Invalid link or parameter.')

			task = tasksDB.getTaskById(taskID)
			if task is None:
				p.sendMessage(tg_id, 'Ahaha, 404 Error: Task not found.')
			else:
				response = printTask(task, user)
				p.sendMessage(tg_id, response)


			# print("Task ID:", taskID)
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
	message = ''

	message += interlocutor.me_command['score'][0]
	message += str(user.getScore())

	return message


def score_command(self):
	tg_id = self.data["sender_id"]
	user = usersDB.getUserByTgId(tg_id)
	botAnswer = ''

	if user is not None:
		botAnswer = score_for_parcipant(user)
	else:
		botAnswer = 'I do not understand...'

	p.sendMessageToChat(self.data, botAnswer)


def mecommand_for_parcipant(user):
	message = ''
	
	message += interlocutor.me_command['start'][0]

	message += interlocutor.me_command['name'][0]
	message += user.getName()

	message += getUserStatusAsMessage(user)

	message += score_for_parcipant(user)

	message += interlocutor.me_command['task'][0]
	message += '-'

	message += interlocutor.me_command['task_2'][0]

	message += interlocutor.me_command['task_ok'][0]
	message += '-'

	message += interlocutor.me_command['task_notok'][0]
	message += '-'

	return message



def me_command(self):
	tg_id = self.data["sender_id"]
	user = usersDB.getUserByTgId(tg_id)
	botAnswer = ''

	if user is not None:
		botAnswer = mecommand_for_parcipant(user)
	else:
		botAnswer = 'I do not understand...'

	p.sendMessageToChat(self.data, botAnswer)


def stats_for_parcipant():
	message = ''

	message += 'Statistics under construction...'

	return message


def stats_command(self):
	tg_id = self.data["sender_id"]
	user = usersDB.getUserByTgId(tg_id)
	botAnswer = ''

	if user is not None:
		botAnswer = stats_for_parcipant()
	else:
		botAnswer = 'I do not understand...'

	p.sendMessageToChat(self.data, botAnswer)


def task_for_parcipant(user):
	message = ''

	message = interlocutor.task_command["enter"][0]

	user.changeStatus(UserStatuses.SENDS_TASKID)
	usersDB.updateUser(user)


	return message


def task_command(self):
	tg_id = self.data["sender_id"]
	user = usersDB.getUserByTgId(tg_id)
	botAnswer = ''

	if user is not None:
		botAnswer = task_for_parcipant(user)
	else:
		botAnswer = 'I do not understand...'

	p.sendMessageToChat(self.data, botAnswer)


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

	elif userStatus == UserStatuses.SENDS_ANSWER:
		if message.replace(" ", '').lower() == interlocutor.stop_word:
			answer = answer_stop(user)
		else:
			message = interlocutor.get_validated_answer(message)
			answer = processUserAnswer(message, user)

	elif userStatus == UserStatuses.SENDS_TASKID:
		answer = taskIDEnter(message, user)

	return answer
		


def empty(self):
	tg_id = self.data["sender_id"]
	user = usersDB.getUserByTgId(tg_id)
	text = self.data['text']
	botAnswer = ''

	if user is not None:
		botAnswer = "This is <empty> for parcipant."

		if len(text) > 0:
			if text[0] != "/":
				botAnswer = empty_for_parcipant(user, text)
	else:
		botAnswer = 'I do not understand...'

	p.sendMessageToChat(self.data, botAnswer)


p.accordance = [
	Accordance('/start', start_command, 'all:all', enableArgument=True),
	Accordance('/help', help_command, 'all:all', enableArgument=True),
	Accordance('/me', me_command, 'all:all', enableArgument=True),
	Accordance('/score', score_command, 'all:all', enableArgument=True),
	Accordance('/stats', stats_command, 'all:all', enableArgument=True),
	Accordance('/task', task_command, 'all:all', enableArgument=True)
]
p.emptyAccordance = Accordance('', empty, 'all:all', enableArgument=True)


def main(u, t, s):
	global usersDB
	global tasksDB
	global solutionsDB
	usersDB = u
	tasksDB = t
	solutionsDB = s

	while True:
		p.updateAndRespond()
		sleep(10)


# if __name__ == '__main__':
# 	main()
