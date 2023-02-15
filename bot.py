from storage import Storage
from tg_token import TOKEN, GROUP_ID
import telebot
import time

bot = None

for i in range(0, 5):
    try:
        # connect
        bot = telebot.TeleBot(TOKEN)
        connection_error = None
    except Exception as e:
        connection_error = str(e)
    if connection_error:
        print('Failed starting Telegram bot...')
        time.sleep(4)
    else:
        break


def send(msg, chat_id):
    print(f'Sending message:\n{msg}')
    for i in range(0, 5):
        try:
            bot.send_message(chat_id=chat_id, text=msg)
            send_error = None
        except Exception as e:
            send_error = str(e)

        if send_error:
            print('Error sending message to group chat')
            time.sleep(4)
        else:
            break

send('Bot started', GROUP_ID)

while 1:
    # infinite loop where we check every 10 minutes whether there is enough space
    strg = Storage()
    if strg.is_enough_gib():
        print('There is enough space on PC')
    else:
        send(f'‼️**AT SERVER**‼️\nLow amount of space on PC\nDetails:\n{str(strg)}', GROUP_ID)
        print('There is not enough space on PC')
    wait_hours = 24
    print(f'Waiting {wait_hours} hours')
    time.sleep(wait_hours * (60*60))
