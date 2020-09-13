from collections import defaultdict

from . import db

welcomed = []
msg_count = defaultdict(int)


def process(bot, user, message):
    update_records(bot, user)
    if user['id'] not in welcomed:
        welcome(bot, user)
    elif 'leaving' in message or 'got to go' in message or 'gtg' in message or 'need to leave' in message:
        say_goodbye(bot, user)

    # if user['id'] != 'self id'
    check_activity(bot, user)


def update_records(bot, user):
    db.execute("INSERT OR IGNORE INTO users (UserID) VALUES (?)", user['id'])
    db.execute("UPDATE users SET MessagesSent = MessagesSent + 1 WHERE  UserID = ?", user['id'])


def welcome(bot, user):
    message = f"Welcome to the stream @{user['name']} !!! Hope you are doing alright today..."
    bot.send_message(message)
    welcomed.append(user['id'])


def say_goodbye(bot, user):
    bot.send_message(f"See you @{user['name']}!!! You will be missed!!!")
    welcomed.remove(user['id'])


def check_activity(bot, user):
    msg_count[user['id']] += 1
    if msg_count[user['id']] % 5 == 0:
        message = f"Thank for keeping the chat alive @{user['name']}!!!"
        bot.send_message(message + f" Count: {msg_count[user['id']]}")
