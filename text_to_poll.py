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

async def texttopoll(quest,update, context):
    quest=reaaa.sub(" "," ",quest)
    if 1==1:
        q=quest[0:-1]
        q=reaaa.sub("(\n| )(\(a\) ){10,}|(\n| |)Sandeep Choudhary(\n| |)|(\n| |)🤗.*?🤗(\n| |)|Poll to Text Bot\:\n|Soojh Boojh Bot - 02\:\n|NaN| Q.*\.|^\. |^\.|🅰︎\n🅱︎\n🅲︎\n🅳︎\n", "\n", q)
        q=reaaa.sub("(\n|\ )( |)(\(|\[|)(A|B|C|D|a|b|c|d|अ|ब|स|द|1|2|3|4|ए|ऐ|बी|सी|डी)(\)|\]|\.)(\.|\ |)", "\n", q)
        #q=reaaa.sub("(A|B|C|D)", "\n", q)
        q=reaaa.sub("\n{2,}", "\n", q)
        q=reaaa.sub("^\n", "", q)

    
        q=reaaa.split("[\n]", q)
        #update.message.reply_text(q)
        ques=q[0]
        que=""+ ques
        #que=que+"\n\n  ■_𝗜𝗺𝗽𝗼𝗿𝘁𝗮𝗻𝘁_𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻_■"
        option1="(A) "+q[1]
        option2="(B) "+q[2]
        option3="(C) "+q[3]
        option4="(D) "+q[4]
        options=[option1, option2, option3, option4]
        corr=quest[-1]
        result = reaaa.match("[-+]?\d+$", corr)
        options5=q[5::1]
        options5="\n".join(options5)
        options5=reaaa.sub(r"@\w*", "@kinbin247", options5)
        if options5 == "":
            options5=""#options5="👇👇👇 Ask your Doubts here 👇👇👇\n👇👇👇        Only for Math        👇👇👇\nhttps://soojhboojh.xyz/ask-question/"
        else:
            options5=options5
            print(options5)
        #options5=reaaa.sub(r"\@\w.*", "", options5)
        #update.message.reply_text(options)

        if result is None:
          message = context.bot.send_poll(
            update.effective_chat.id,
            que,
            options,
            is_anonymous=False,
            allows_multiple_answers=False,
        )
        elif options5 !="":
          co=int(corr)-1
          message = context.bot.send_poll(
            update.effective_chat.id,
            que,
            options,
            type=Poll.QUIZ,
            correct_option_id=co,
            explanation=options5,
            is_closed=True,
            is_anonymous=False,
            allows_multiple_answers=False,
        )
        elif options5 =="":
          co=int(corr)-1
          message = context.bot.send_poll(
            update.effective_chat.id,
            que,
            options,
            type=Poll.QUIZ,
            correct_option_id=co,#explanation=options5,
            is_closed=True,
            is_anonymous=False,
            allows_multiple_answers=False,
        )
        # Save some info about the poll the bot_data for later use in receive_poll_answer
        payload = {
            message.poll.id: {
                "questions": questions,
                "message_id": message.message_id,
                "chat_id": update.effective_chat.id,
                "answers": 0,
                "explanation": ["join"],
            }
        }
        context.bot_data.update(payload)
