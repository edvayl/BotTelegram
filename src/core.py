from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
import random
import string





def start(bot, update):
    response_message = "Oi"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def http_cats(bot, update, args):
    bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo="https://www.freebunker.com/img/500"
    )

def rd(bot, update):
    letters = string.ascii_lowercase
    a =random.choice(letters)
    b =random.choice(letters)
    r =  random.randint(1000, 9999)
    c= str(r)
    link ='https://imgmak.com/a' + b + a + b

    bot.send_message(
        chat_id=update.message.chat_id,
         text= link
    )

def sx(bot, update):
    
    link ='https://www.freebunker.com/img/500'

    bot.send_message(
        chat_id=update.message.chat_id,
         text=link
    )





def unknown(bot, update):
    r =  random.randint(1000, 9999)
    c= str(r)
    link ='https://www.freebunker.com/img/' + c
    bot.send_message(
        chat_id=update.message.chat_id,
         text=link
    )


def main():
    updater = Updater(token="830193229:AAFoDBIWv2Yx9qN2RDIQpCD2PkzUjK5etsA")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )
    dispatcher.add_handler(
        CommandHandler('oi', http_cats, pass_args=True)
    )

    dispatcher.add_handler(
        CommandHandler('r', rd)
    )
    
    dispatcher.add_handler(
        CommandHandler('x', sx)
    )
    

    dispatcher.add_handler(
        MessageHandler(Filters.command,unknown)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.all,unknown)
    )
    
    


    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()
