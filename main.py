
import telebot

with open("data/token.txt", "r") as file:
    API_TOKEN = file.readline()

bot = telebot.TeleBot(API_TOKEN)
admins = []

def arguments(message: str):
    return message.split()[1:]


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=["add_admin"])
def add_admin(message):
    if str(message.from_user.id) in admins:
        with open("data/admins.txt", "a") as file:
            print(f"{arguments(message.text)[0]}\n")
            file.write(f"{arguments(message.text)[0]}\n")
            admins.append(arguments(message.text)[0])

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    with open("data/admins.txt", "r") as file:
        admins = [line.rstrip() for line in file]

    bot.infinity_polling()