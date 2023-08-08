import os
import telebot
import requests
import json
import csv
from csv import DictWriter

# TODO: 1.1 Get your environment variables 
bot_id='5721194698:AAGNkeyYbOgy3AX8DBuGCIGyEp4owvrGgTY'

bot = telebot.TeleBot(bot_id)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file\n/help for commands.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')



@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    
    a=message.text
    movie= a[7:]
    response = requests.get(f"http://www.omdbapi.com/?apikey=fc88b3a8&t={movie}")
    
    movie_data=response.json()
    y = json.loads(json.dumps(movie_data))
    p = y['Poster']
    q = y['Title']
    w = y['Year']
    e = y['imdbRating']
    f = y['Actors']
    g = y['Plot']
    d= {}
    d.update({'Title':q, 'Year':w, 'IMDb':e, 'Actors':f, 'Plot':g})
    telem= f"TITLE: {q}\nYEAR: {w}\nIMDb: {e}\nACTORS: {f}\nPLOT: {g}"

    bot.send_photo(message.chat.id, p)    
    bot.send_message(message.chat.id, telem)


    # TODO: 2.1 Create a CSV file and dump the movie information in it

    fields=['Title', 'Year', 'IMDb', 'Actors', 'Plot']
    file = 'movie_info.csv'

    with open(file, 'a') as csvfile:
        writer = DictWriter(csvfile, fieldnames=fields)
        writer.writerow(d)

  
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')

    #TODO: 2.2 Send downlodable CSV file to telegram chat
    
    bot.send_document(message.chat.id, document=open('movie_info.csv', 'rb'))


@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()