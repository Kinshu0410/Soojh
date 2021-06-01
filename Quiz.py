#!/usr/bin/env python
# pylint: disable=C0116
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import time
import re
import json
import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, Poll, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    PollAnswerHandler,
    PollHandler,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

GENDER, PHOTO, LOCATION, BIO, QUIZ, DELETE = range(6)


def createquiz(update: Update, _: CallbackContext) -> int:
    

    update.message.reply_text(
        "Hello Quizers \n\n Send me a name of your quiz..."
	)

    return GENDER

Textstr=""
def gender(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("Gender of %s: %s", user.first_name, update.message.text)
    global Textstr
    userText=update.message.text
    Textstr=userText
    update.message.reply_text(
        "Greate! this is a good name.\n\n Send me poll or you can skip using /skip do you want to quit ", reply_markup=ReplyKeyboardRemove(),
    )

    return PHOTO



db = {}
we=1
Que=""
#question=""
#options=""
#correct_option_id=""
def photo(update: Update, _: CallbackContext) -> int:
    user = update.effective_message.poll
    '''photo_file = update.message.photo[-1].get_file()
    photo_file.download('user_photo.jpg')
    logger.info("Photo of %s: %s", user.first_name, 'user_photo.jpg')'''
    global db
    global we
    with open('/storage/emulated/0/ADM/file.text') as json_file:
    	db = json.load(json_file)
    	new=[{'que':str(we)+". "+user.question, 'op':[o.text for o in user.options], 'cor':user.correct_option_id}]
    	if Textstr not in list(db.keys()):
    		print("123")
    		db[Textstr]=new
    		'''db[Textstr]=[]
    		db[Textstr].append({'que':str(we)+". "+user.question, 'op':[o.text for o in user.options], 'cor':user.correct_option_id})'''
    		we+=1
    		with open('/storage/emulated/0/ADM/file.text', 'w') as outfile:
    			json.dump(db, outfile)
    	else:
    		db[Textstr].append(new)
    		we+=1
    		with open('/storage/emulated/0/ADM/file.text', 'w') as outfile:
    			json.dump(db, outfile)



    #update.message.reply_text(Que)
    update.message.reply_text("Send me more polls or quiz using /skip")
    return PHOTO


def skip_photo(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s did not send a poll.", user.first_name)
    with open('/storage/emulated/0/ADM/file.text', 'w') as outfile:
    	json.dump(db, outfile)
    
    #update.message.reply_text(db[Textstr][0]['que'])
    #update.message.reply_text(db[Textstr]['op'])
    #update.message.reply_text(db[Textstr]['cor'])

    return LOCATION

i=0
def location(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    user_location = update.message.text
    '''logger.info(
        "Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude
    )'''
    
    
    if Textstr==user_location:
    	print(Textstr)
    	
    	
    else:
    	update.message.reply_text("sorry")
    
    for p in db[Textstr]:
         message = context.bot.send_poll(
            update.effective_chat.id,
            question=p[question],
            options=p[options],
            type=Poll.QUIZ,
            correct_option_id=p[cor],
            #explanation=options5,,
            is_anonymous=False,
            allows_multiple_answers=False,
        )
	
    return BIO


def skip_location(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    update.message.reply_text(
        'You seem a bit paranoid! At last, tell me something about yourself.'
    )

    return BIO


def bio(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Thank you! I hope we can talk again some day.')

    return ConversationHandler.END


def cancel(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def playquiz(update: Update, _: CallbackContext) -> int:
    

    update.message.reply_text(
        "Send me Quiz Name"
	)

    return QUIZ

Textstr0=""
def quiz(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
   
    global Textstr0
    userText=update.message.text
    Textstr0=userText
    with open('/storage/emulated/0/ADM/file.text') as json_file:
    	db = json.load(json_file)
    	try:
    		update.message.reply_text("Quiz Play", reply_markup=ReplyKeyboardRemove(),)
    		for X in range(len(db[Textstr0])):
    			X=int(len(db[Textstr0]))-X-1
    			if X==0:
		    		for q in db[Textstr0]:
		    			update.effective_message.reply_poll(
		    			question=q['que'],
		    			options=q['op'],
		    			# with is_closed true, the poll/quiz is immediately closed
		    			type=Poll.QUIZ,
		    			correct_option_id =q['cor'],
		    			#explanation=Ex,
		    			is_closed=False,
		    			is_anonymous=False,
		    			reply_markup=ReplyKeyboardRemove()
		    			)
		    	else:
		    		for p in db[Textstr0][X]:
		    			update.effective_message.reply_poll(
		    			question=p['que'],
		    			options=p['op'],
		    			# with is_closed true, the poll/quiz is immediately closed
		    			type=Poll.QUIZ,
		    			correct_option_id =p['cor'],
		    			#explanation=Ex,
		    			is_closed=False,
		    			is_anonymous=False,
		    			reply_markup=ReplyKeyboardRemove()
		    			)
	    			time.sleep(5)
    	except:
    		update.message.reply_text("Name not exist Or Quiz finish.", reply_markup=ReplyKeyboardRemove(),)

    return ConversationHandler.END

def deletequiz(update: Update, _: CallbackContext) -> int:
    

    update.message.reply_text(
        "Hello Quizers \n\n Send me a name of your quiz you want to DELETE."
	)

    return DELETE

Textstr1=""
def delete(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
   
    global Textstr1
    userText=update.message.text
    Textstr1=userText
    with open('/storage/emulated/0/ADM/file.text') as json_file:
    	db = json.load(json_file)
    	try:
    		db.pop(Textstr1)
    		with open('/storage/emulated/0/ADM/file.text', 'w') as outfile:
    			json.dump(db, outfile)
    		update.message.reply_text("Quiz "+Textstr1+" deleted", reply_markup=ReplyKeyboardRemove(),)
    		
    	except:
    		update.message.reply_text("Name not exist", reply_markup=ReplyKeyboardRemove(),)

    return ConversationHandler.END




def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("1355592440:AAFrVCpDWYj43y85fIjC5MFJqnqfHqEOsgk")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('createquiz', createquiz)],
        states={
            GENDER: [MessageHandler(Filters.regex('^.*$'), gender)],
            PHOTO: [MessageHandler(Filters.poll, photo), CommandHandler('skip', skip_photo)],
            LOCATION: [
                MessageHandler(Filters.text& ~Filters.command, location),
                CommandHandler('skip', skip_location),
            ],
            BIO: [MessageHandler(Filters.text & ~Filters.command, bio)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    
    conv_handler01 = ConversationHandler(
        entry_points=[CommandHandler('playquiz', playquiz)],
        states={
            QUIZ: [MessageHandler(Filters.regex('^.*$'), quiz)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    conv_handler02 = ConversationHandler(
        entry_points=[CommandHandler('deletequiz', deletequiz)],
        states={
            DELETE: [MessageHandler(Filters.regex('^.*$'), delete)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(conv_handler01)
    dispatcher.add_handler(conv_handler02)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
