import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
        bot.send_message(message.chat.id, pokemon.ability_1())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['attack'])
def attack(message):
    if message.reply_to_message:
        p1 = Pokemon.pokemons[message.reply_to_message.from_user.username]
        p2 = Pokemon.pokemons[message.from_user.username]
        if p1.pokemon_trainer == p2.pokemon_trainer:
            bot.send_message(message.chat.id, 'нельзя себе уубить')
        else:

            r = p2.attack(p1)
            bot.send_message(message.chat.id, r)

@bot.message_handler(commands=['feed'])
def Feed(message):
    if message.reply_to_message:
        p1 = Pokemon.pokemons[message.reply_to_message.from_user.username]
        bot.send_message(message.chat.id, p1.feed())



bot.infinity_polling(none_stop=True)

