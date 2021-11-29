from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import logging
from .config import BOT_TOKEN
from .commands.start import start
from .commands.help import help
from .commands.invalid_command import invalid_command
from .handlers.callbackquery_handler import button_click
from .handlers.extract_image import extract_image


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def main(): 
    updater = Updater(BOT_TOKEN,use_context=True)
    updater.bot.set_my_commands([("start","start the bot"),("help","Get list of commands")])
    dp=updater.dispatcher
    conv_handler01PDF= ConversationHandler(
        entry_points=[CommandHandler('pdf', pdf)],
        states={
        #POLLN: [MessageHandler(Filters.regex('^.*$') & ~Filters.command, pollfsend),],
            PDF: [MessageHandler(Filters.text& ~Filters.command, pdfc),],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    
    conv_handler01F= ConversationHandler(
        entry_points=[CommandHandler('start', pollf)],
        states={
        #POLLN: [MessageHandler(Filters.regex('^.*$') & ~Filters.command, pollfsend),],
            POLLF: [MessageHandler(Filters.regex('^.*$') & ~Filters.command, pollfname),],
        },
        fallbacks=[CommandHandler('start', pollf)],
    )
    
    
    conv_handler012 = ConversationHandler(
        entry_points=[CommandHandler('copyc', copyc)],
        states={
            COPY: [MessageHandler(Filters.regex('^.*$') & ~Filters.command, copy), 
            MessageHandler(Filters.poll, polls),
            ],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    
    
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
            TIME: [MessageHandler(Filters.regex('^\d{1,}$'), time0)],
            Re:[CommandHandler('result', res)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    
    
    
    conv_handler0C = ConversationHandler(
        entry_points=[CommandHandler('playingroup', playinc)],
        states={
            CHN: [MessageHandler(Filters.regex('^.*$'), chn)],
            QUIZ: [MessageHandler(Filters.regex('^.*$'), quizc)],
            TIME: [MessageHandler(Filters.regex('^\d{1,}$'), time0c)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    conv_handler1C = ConversationHandler(
        entry_points=[CommandHandler('massingroup', playing)],
        states={
            GHN: [MessageHandler(Filters.text & ~Filters.command & ~Filters.regex(r'^((https|http).*|@.*)$') & ~Filters.regex(r'^-\d{1,}$'), ghn), MessageHandler(Filters.regex(r'^((https|http).*|@.*|-\d{1,})$'), time1c)],
            GHN2:[MessageHandler(Filters.poll,  ghn2),MessageHandler(Filters.text & ~Filters.command & ~Filters.regex(r'^((https|http).*|@.*)$') & ~Filters.regex(r'^-\d{1,}$'), ghn)],
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
    
    
    conv_handler0u = ConversationHandler(
        entry_points=[CommandHandler('uploadfile', uploadfile)],
        states={
            UPLOAD: [MessageHandler(Filters.document, upload)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    conv_handler01R= ConversationHandler(
        entry_points=[CommandHandler('quizresult', quizresult)],
        states={
            RESULT: [MessageHandler(Filters.text,result)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    conv_handler01R1= ConversationHandler(
        entry_points=[CommandHandler('create', upload1)],
        states={
            #CALL: [],
            CALL: [MessageHandler(Filters.text& ~Filters.command, call1),MessageHandler(Filters.photo& ~Filters.command,call2),MessageHandler(Filters.poll& ~Filters.command,call6)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    conv_handler01R2= ConversationHandler(
        entry_points=[CommandHandler('adde', upload2)],
        states={
            #CALL: [],
            CALL1: [MessageHandler(Filters.text& ~Filters.command, call4),MessageHandler(Filters.photo& ~Filters.command,call5)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    updater.dp.add_handler(conv_handler01R1)
    updater.dp.add_handler(conv_handler01R2)
    updater.dp.add_handler(CommandHandler('add', call4))
    updater.dp.add_handler(CommandHandler('startquiz', call3))
    #updater.dp.add_handler(CommandHandler('start', start))
    updater.dp.add_handler(MessageHandler(Filters.photo, photos))
    updater.dp.add_handler(CallbackQueryHandler(button))
    updater.dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(conv_handler01PDF)
    dp.add_handler(conv_handler01R)
    dp.add_handler(PollAnswerHandler(receive_poll_answer))
    
    dp.add_handler(conv_handler)
    
    dp.add_handler(conv_handler01F)
    dp.add_handler(conv_handler01)
    dp.add_handler(conv_handler0C)
    dp.add_handler(conv_handler1C)
    dp.add_handler(conv_handler02)
    dp.add_handler(conv_handler012)
    dp.add_handler(conv_handler0u)
    dp.add_handler(CommandHandler('quizlist', quizlist))
    dp.add_handler(CommandHandler('downloadfile',downloadfile))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, poll))
    dp.add_handler(MessageHandler(Filters.poll, ghppp1))

    updater.start_polling(drop_pending_updates=True)
    print("Bot is running")
    updater.idle()
    
