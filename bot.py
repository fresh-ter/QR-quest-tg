import json
import telebot

import config as tS


bot = telebot.TeleBot(tS.token)


def send_invitation_to_qr(chat_id):
	text = 'Найдите и отсканируйте QR-код задачки...'
	bot.send_message(chat_id, text)


@bot.message_handler(regexp='^\/start t\w*$')
def start_command_with_task(message):
	bot.reply_to(message, "task")
	print(message.text)


@bot.message_handler(commands=['start'])
def start_command(message):
	bot.reply_to(message, "Simple start")
	print(message.text)

	send_invitation_to_qr(message.chat.id)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)


def print_tasks_for_check():
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
		print()


def main():
	# bot.infinity_polling(interval=5)
	print_tasks_for_check()


if __name__ == '__main__':
	main()
