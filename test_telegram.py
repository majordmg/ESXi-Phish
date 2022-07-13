import telebot
import json 

msg = "test"
config_data = json.load(open("./config.json", "r"))
api_token = config_data['api_token']
chat_id = config_data['chat_id']
bot = telebot.TeleBot(api_token) # You can set parse_mode by default. HTML or MARKDOWN
bot.send_message(int(chat_id), msg)

