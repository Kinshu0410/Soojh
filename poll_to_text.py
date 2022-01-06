import telegram

from telegram import (
    Poll,
    Update,
    ParseMode,
    KeyboardButton,
    KeyboardButtonPollType,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ChatAction,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    Updater,
    CommandHandler,
    PollAnswerHandler,
    PollHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    ConversationHandler,
    CallbackQueryHandler
)

#1
import re as reaaa
from telegram.ext.dispatcher import run_async
async def polltotext(actual_poll,update, context):
    ex =actual_poll.explanation
    
    if ex is None:
        ex=""
    else:
        ex=reaaa.sub(r"\@.*+\s", "", ex)
        ex=reaaa.sub(r"(http|ftp|https|t\.me|tg):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", "", ex)
    
    Ex=str(ex)        #ex=ex
    #update.message.reply_text(ex)
    #ex=reaaa.sub(r"\@.*?\s", "", ex)
    #ex=reaaa.sub(r"\@\w.*", "", ex)
    question= actual_poll.question
    #update.message.reply_text("1")
    #question=reaaa.sub("\@\w*", "", question)
    question=reaaa.sub("𝗤. ", "", question)
    #question=reaaa.sub(" ■_𝗜𝗺𝗽𝗼𝗿𝘁𝗮𝗻𝘁_𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻_■", "", question)
    q=reaaa.sub("^((\[\d{1,}\/\d{1,}\] ){1,}|)(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|)(\d{1,}\. |\d{1,}\.|)|( |\n)(\@)(.*?)( |\n)", "", question)
    q=reaaa.sub("\n{1,}|\ {1,}", " ", q)
    
        
    #q=q+"\n\n  ■_𝗜𝗺𝗽𝗼𝗿𝘁𝗮𝗻𝘁_𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻_■"
    options=[o.text for o in actual_poll.options]
    #update.message.reply_text("1")
    corr = actual_poll.correct_option_id
    #update.message.reply_text("1")
    print(corr)
    #print(cor)
    #update.message.reply_text("1")
    try:
        cor=str(int(str(corr))+1)
    except:
        cor="(a) (a) (a) (a) (a) (a) (a) (a) (a) (a) (a) (a) (a) (a) (a) (a) (a) (a) (a) (a)" #update.message.reply_text("1")
    #print("12")
    
    #print("123")
    #update.message.reply_text("1")    #print(actual_poll)
    #update.message.reply_text("<pre>"+question+"</pre>",parse_mode=telegram.ParseMode.HTML)
    
    #update.message.reply_text("1")
    try:
        #print("12")
        Qqq=cor+" "+options[corr]
        
        Qqq=reaaa.sub("(\(|\[)(A|B|C|D|a|b|c|d|अ|ब|स|द)(\)|\])(|\ )", "",Qqq)
        #print("1234")
        abc=reaaa.match("^(1|2|3|4) (A|B|C|D|a|b|c|d|अ|ब|स|द)$", Qqq)
        a1=reaaa.match("^(1|2|3|4) (A|a|अ)$", Qqq)
        a2=reaaa.match("^(1|2|3|4) (B|b|ब|)$", Qqq)
        a3=reaaa.match("^(1|2|3|4) (C|c|स)$", Qqq)
        a4=reaaa.match("^(1|2|3|4) (D|d|द)$", Qqq)
        #print("2")
        if abc:
        	#print("3")
        	if a1:
        		Qqq="1"
        	elif a2:
        		Qqq="2"
        	elif a3:
        		Qqq="3"
        	elif a4:
        		Qqq="4"
        else:
        	Qqq=0
        	#print(Qqq)
        update.message.reply_text("<pre>"+q+Qqq+"</pre>",parse_mode=telegram.ParseMode.HTML)
    except:
        options="\n".join(options)
        T=q+"\n"+options+"\n"+cor
        
        #update.message.reply_text("<pre>"+T+"</pre>",parse_mode=telegram.ParseMode.HTML)
    
        q=q+"\n"+options+"\n"+Ex+"\n"+cor
        update.message.reply_text("<pre>"+q+"</pre>",parse_mode=telegram.ParseMode.HTML)
    #update.message.reply_text("<pre>"+options[3]+"</pre>",parse_mode=telegram.ParseMode.HTML)
    #update.message.reply_text("<pre>"+options[4]+"</pre>",parse_mode=telegram.ParseMode.HTML)
    #update.message.reply_text("<pre>"+options[5]+"</pre>",parse_mode=telegram.ParseMode.HTML)
    #update.message.reply_text("<pre>"+options[6]+"</pre>",parse_mode=telegram.ParseMode.HTML)
    #update.message.reply_text("<pre>"+options[7]+"</pre>",parse_mode=telegram.ParseMode.HTML)
    #update.message.reply_text("<pre>"+options[8]+"</pre>",parse_mode=telegram.ParseMode.HTML)
    #update.message.reply_text("<pre>"+options[9]+"</pre>",parse_mode=telegram.ParseMode.HTML)
    #update.message.reply_text("<pre>"+cor+"</pre>",parse_mode=telegram.ParseMode.HTML)
    '''
    if ex == "":
        update.effective_message.reply_poll(
            question= q,
            options=options,
            # with is_closed true, the poll/quiz is immediately closed
            type=Poll.QUIZ,
            correct_option_id =corr,
            #explanation=Ex,
            is_closed=True,
            is_anonymous=False,
            reply_markup=ReplyKeyboardRemove()
    )
    else:
        update.message.reply_text("<pre>"+Ex+"</pre>",parse_mode=telegram.ParseMode.HTML)
        update.effective_message.reply_poll(
            question= q,
            options=options,
            # with is_closed true, the poll/quiz is immediately closed
            type=Poll.QUIZ,
            correct_option_id =corr,
            explanation=Ex,
            is_closed=True,
            is_anonymous=False,
            reply_markup=ReplyKeyboardRemove()
    )'''
    #update.message.reply_text("<pre>"+ex+"</pre>",parse_mode=telegram.ParseMode.HTML)

