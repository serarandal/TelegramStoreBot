# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests
import re
from telegram import InlineQueryResultArticle, InputTextMessageContent ,Bot
from telegram.ext import Updater, CommandHandler ,MessageHandler,Filters,InlineQueryHandler,filters
import logging
import json
import SaveData

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def caps(update,context):
    if (not context.args):
        context.bot.send_message(chat_id=update.effective_chat.id, text="no has puesto nada")
    text_caps=''.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def inline_caps(update,context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id,results)
def Store(update,context):
    text = update.message.text.split()
    link = text[1].split("//",1)
    long=(len(link))
    if(long>1):
        novela = link[1].split("/",1)
    if((text[0] =="/store") & (long >1)):
        if(novela[0]=="tunovelaligera.com"):
            context.bot.send_message(chat_id=update.effective_chat.id,text="libro guardado")
            Bot.delete_message(context.bot,update.effective_chat.id,update.message.message_id)
            SaveData.saveBook(text)

        elif((link[1]!="tunovelaligera.com") & ((link[0]=="http:") or (link[0]=="https:"))):
            context.bot.send_message(chat_id=update.effective_chat.id, text="enlace guardado")
            Bot.delete_message(context.bot, update.effective_chat.id, update.message.message_id)
            SaveData.saveLink(text)
    elif((text[0]=="/store")& len(link) <=1):
        context.bot.send_message(chat_id=update.effective_chat.id, text="texto guardado")
        Bot.delete_message(context.bot, update.effective_chat.id, update.message.message_id)
        SaveData.saveText(text)


def unkown(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

updater = Updater(token='here you need to introduce the token of your bot',use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

start_handler = CommandHandler('start', start)
#echo_handler = MessageHandler(Filters.text & (~Filters.command),echo)
caps_handler = CommandHandler('caps',caps)
inline_caps_handler = InlineQueryHandler(inline_caps)
Store_handler = MessageHandler(Filters.text & (Filters.command),Store)
#unknown_handler = MessageHandler(Filters.command, unkown)
dispatcher.add_handler(start_handler)
#dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(inline_caps_handler)
dispatcher.add_handler(Store_handler)
#dispatcher.add_handler(unknown_handler)
updater.start_polling()
