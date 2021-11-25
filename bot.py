from Penger.penger import Penger, Accordance
import tgbotSettings as tS
import time

from utils.task import Task


p = Penger(token = tS.token)


def start_command(self):
	p.sendMessageToChat(self.data, "Hello:-)")

	print(self.data)

	command_args = self.data['text'].split()
	if len(command_args) > 1:
		arg = str(command_args[1])

		if arg[:4] == "task":
			Task.parse(arg)


def empty(data):
	p.sendMessageToChat(data, 'I do not understand...')


p.accordance = [
	Accordance('/start', start_command, 'all:all', enableArgument=True),
]
p.emptyAccordance = empty


def main():
	while True:
		p.updateAndRespond()
		time.sleep(10)


if __name__ == '__main__':
	main()
