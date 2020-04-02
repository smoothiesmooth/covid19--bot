import telebot
import covid19_data as cd

bot = telebot.TeleBot("916209163:AAHa7SIT04ELKub2Zd9gpf9YABt95szghZs")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, f'<b>Welcome, {message.from_user.username}!</b>\nSend the name of place?', parse_mode='html')

@bot.message_handler(content_types = ['text'])
def main(message):
	try:
		data = cd.dataByName(f'{message.text}')
	except KeyError:
		bot.send_message(message.chat.id, 'Place not found')
	else:
		bot.send_message(message.chat.id, f'<ins><b>{message.text}</b></ins>\ntotal: {data.cases}, deaths: {data.deaths}, recovered: {data.recovered}', parse_mode='html')
bot.polling(none_stop=True)
