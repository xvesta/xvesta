import telebot
import random
from xuylist import xuyanswers_list, pizdaanswers_list, kuanswers_list, kurequests_list, stickerrequest_list,\
    stickeranswer_list, lubovreques_list, anekanswer_list, anekrequest_list, questionrequestlist, xuyrequest_list,\
    pizdarequests_list, memes_list

bot = telebot.TeleBot("5778875150:AAFIsTxbIh1g35y7JbmLshUWfsisIxd3dSM")
@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "ку")
@bot.message_handler(commands = ['help'])
def help(message):
    bot.send_message(message.chat.id, "тебе уже ничего не поможет")

@bot.message_handler(commands = ['meme'])
def memes(message):
    choiceofniggers = ["1", "2"]
    rNum = random.choice(choiceofniggers)
    photo = open(memes_list + rNum + ".jpg", "rb")
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(content_types=['photo'])
def userphoto(message):
    bot.send_message(message.chat.id, "мне не интересны твои подачки. либо нюдсы либо ничего!")

@bot.message_handler(content_types=['text'])
def xuy(message):
    if message.text in xuyrequest_list:
        bot.send_message(message.from_user.id, random.choice(xuyanswers_list))
    elif message.text in pizdarequests_list:
        bot.send_message(message.from_user.id, random.choice(pizdaanswers_list))
    elif message.text == "да":
        bot.send_message(message.chat.id, "пизда")
    elif message.text == "нет":
        bot.send_message(message.chat.id, "скажи да")
    elif message.text in kurequests_list:
        bot.send_message(message.chat.id, random.choice(kuanswers_list))
    elif message.text == "пока":
        bot.send_message(message.chat.id, "прощай..")
    elif message.text in stickerrequest_list:
        bot.send_sticker(message.chat.id, random.choice(stickeranswer_list))
    elif message.text in lubovreques_list:
        bot.send_message(message.chat.id, "мы")
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEFxYdjF4EWyh4rrGmY5Hhkx1jyiQgnJQAC5AADpiVjKmQomC9NbiWSKQQ")
    elif message.text in anekrequest_list :
        bot.send_message(message.chat.id, random.choice(anekanswer_list))
    elif message.text in questionrequestlist:
        bot.send_message(message.chat.id, "долбаёбище ты тупое блять вопросы свои себе в очко засунь")
    elif message.text == "хорош":
        bot.send_message(message.chat.id, "да - да, я")
    elif message.text == "имба":
        bot.send_message(message.chat.id, "соглы")
    elif message.text == "ладно":
        bot.send_message(message.chat.id, "прохладно")
    else:
        bot.send_message(message.chat.id, "чел, у меня iq ниже 12, я тебя абсолютно не понимаю")
bot.polling (none_stop = True, interval=0)
