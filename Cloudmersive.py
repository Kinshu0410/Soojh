from pyrogram import Client
from pyrogram.handlers import MessageHandler, PollHandler
from pyrogram import filters
from pyrogram.types import Message, ReplyKeyboardRemove, Poll
import  json
import time
import re as reaaa

app = Client("my_account",
#bot_token=ClientText["bot_token"],
api_id="13682659",
api_hash="b984d240c5258407ea911f042c9d75f6")

@app.on_message(filters.text & filters.chat("POLLQZ") )#& filters.incoming)
async def forword(client:Client,message:Message):
    if message.reply_markup:
        await app.send_message("quizbot", message.reply_markup["inline_keyboard"][0][0].url)
    
@app.on_message(filters.all & ~ filters.poll & filters.chat("quizbot") )#& filters.incoming)
async def forword(client:Client,message:Message):
	#await app.send_message("me", str(message.reply_markup["inline_keyboard"][0][0].callback_data))
	if message.reply_markup:
	    if message.reply_markup["inline_keyboard"][0][0].callback_data=='{"a":"user_ready"}':
	        await client.request_callback_answer(chat_id=message.chat.id,message_id=message.message_id,callback_data=message.reply_markup["inline_keyboard"][0][0].callback_data)

@app.on_message(filters.poll & filters.chat("quizbot") )#& filters.incoming)
async def forword(client:Client,message:Message):
	chatid=["POLLQZ"]
	
	#print(message.message_id)
	try:
		
	    mess=(await client.vote_poll(chat_id=message.chat.id, message_id=message.message_id,options=1))
	except:
	    mess=message.poll
	#print(mess)
	    #print(mess)
	await app.delete_messages(chat_id="POLLQZ", message_ids=message.message_id)
	question=mess.question
	question=reaaa.sub("\n","       ",question)
	question=reaaa.sub(r"(@|#)\w*?(\s|)", "", question)
	question=reaaa.sub(r"^((Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|)(\d{1,}\. |\d{1,}\.|)(\[\d{1,}\/\d{1,}\] ){1,}|)(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|)(\d{1,}\. |\d{1,}\.|)|( |\n)(\@)(.*?)( |\n)", "", question)
	#
	options=[o.text for o in mess.options]
	correct_option_id = 0
	for i in range(len(mess.options)):
	       if mess.options[i]['correct']:
	           correct_option_id = i
	           break
	#correct_option_id
	#print(message)
	#time.sleep(100)
	for x in chatid:
	    mess=(await app.send_poll(chat_id=x,question=question,options=options,correct_option_id =correct_option_id,is_anonymous=False,type="quiz"))
	    #print(mess)
	    await app.stop_poll(chat_id=x,message_id=mess.message_id)

@app.on_message(filters.poll & filters.chat("Neha55bot") & ~filters.chat("Soojhboojh_01bot"))
async def start_(client:Client,message:Message):
	chatid=["Polls_Quiz","haryanaspecialquiz"]
	try:
	    mess=(await client.vote_poll(chat_id=message.chat.id, message_id=message.message_id,options=1))
	except:
	    mess=message.poll
	await app.delete_messages(chat_id="Neha55bot", message_ids=message.message_id)
	question=mess.question
	question=reaaa.sub("\n","       ",question)
	question=reaaa.sub(r"(@|#)\w*?(\s|)", "", question)
	question=reaaa.sub(r"^((Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|)(\d{1,}\. |\d{1,}\.|)(\[\d{1,}\/\d{1,}\] ){1,}|)(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|)(\d{1,}\. |\d{1,}\.|)|( |\n)(\@)(.*?)( |\n)", "", question)
	options=[o.text for o in mess.options]
	correct_option_id = 0
	for i in range(len(mess.options)):
	       if mess.options[i]['correct']:
	           correct_option_id = i
	           break
	for x in chatid:
	    mess=(await app.send_poll(chat_id=x,question=question,options=options,correct_option_id =correct_option_id,is_anonymous=True,type="quiz"))
	    #print(mess)
	    #await app.stop_poll(chat_id=x,message_id=mess.message_id)
	
@app.on_message(filters.poll & filters.chat("SOOJH_BOOJH_BOT_discussion_grouo"))
async def start_command(client:Client,message:Message):
	#print(message)
	chatid=["Soojhboojh_01bot"]
	
	#print(message.message_id)
	try:
	    mess=(await client.vote_poll(chat_id=message.chat.id, message_id=message.message_id,options=1))
	except:
	    mess=message.poll
	#print(mess)
	    #print(mess)
	await app.delete_messages(chat_id="SOOJH_BOOJH_BOT_discussion_grouo", message_ids=message.message_id)
	question=mess.question
	options=[o.text for o in mess.options]
	correct_option_id = 0
	for i in range(len(mess.options)):
	       if mess.options[i]['correct']:
	           correct_option_id = i
	           break
	#correct_option_id
	#print(message)
	#time.sleep(100)
	for x in chatid:
	    await app.send_poll(chat_id=x,question=question,options=options,correct_option_id =correct_option_id,is_anonymous=False,type="quiz")#reply_markup=ReplyKeyboardRemove())

@app.on_message(filters.poll & filters.chat("SOOJH_BOOJH_BOT_discussion_grouo"))
async def start_command(client:Client,message:Message):
	#print(message)
	chatid=["Soojhboojh_01bot"]
	
	#print(message.message_id)
	try:
	    mess=(await client.vote_poll(chat_id=message.chat.id, message_id=message.message_id,options=1))
	except:
	    mess=message.poll
	#print(mess)
	    #print(mess)
	await app.delete_messages(chat_id="SOOJH_BOOJH_BOT_discussion_grouo", message_ids=message.message_id)
	question=mess.question
	options=[o.text for o in mess.options]
	correct_option_id = 0
	for i in range(len(mess.options)):
	       if mess.options[i]['correct']:
	           correct_option_id = i
	           break
	#correct_option_id
	#print(message)
	#time.sleep(100)
	for x in chatid:
	    await app.send_poll(chat_id=x,question=question,options=options,correct_option_id =correct_option_id,is_anonymous=False,type="quiz")#reply_markup=ReplyKeyboardRemove())

@app.on_message(filters.poll & filters.chat("POLLQZ") & ~filters.chat("Soojhboojh_01bot"))
async def start_command(client:Client,message:Message):
	#print(message)
	chatid=["POLLQZ"]
	
	#print(message.message_id)
	try:
		
	    mess=(await client.vote_poll(chat_id=message.chat.id, message_id=message.message_id,options=1))
	except:
	    mess=message.poll
	#print(mess)
	    #print(mess)
	await app.delete_messages(chat_id="POLLQZ", message_ids=message.message_id)
	question=mess.question
	question=reaaa.sub("\n","       ",question)
	question=reaaa.sub(r"(@|#|http|t\.me|tg:)\w*+(\s|)", "", question)
	question=reaaa.sub(r"^((Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|)(\d{1,}\. |\d{1,}\.|)(\[\d{1,}\/\d{1,}\] ){1,}|)(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|)(\d{1,}\. |\d{1,}\.|)|( |\n)(\@)(.*?)( |\n)", "", question)
	#
	options=[o.text for o in mess.options]
	correct_option_id = 0
	for i in range(len(mess.options)):
	       if mess.options[i]['correct']:
	           correct_option_id = i
	           break
	#correct_option_id
	#print(message)
	#time.sleep(100)
	for x in chatid:
	    mess=(await app.send_poll(chat_id=x,question=question,options=options,correct_option_id =correct_option_id,is_anonymous=False,type="quiz"))
	    #print(mess)
	    await app.stop_poll(chat_id=x,message_id=mess.message_id)


@app.on_message(filters.text & filters.chat("KINBIN247_bot") & filters.incoming)
def forword(client:Client,message:Message):
    #if message.forward_from_chat:
#        forward=message.forward_from_chat
#    else:
#        forward=message.forward_from
#    
#    mess=(await app.get_history(forward.id, limit=1))
#    
#    #print()
#    if mess:
#        for mid in range(mess[0].message_id-message.forward_from_message_id):
            
            client.forward_messages(chat_id="KINBIN247_bot",from_chat_id=message.chat.id,message_ids=message.message_id)
            app.delete_messages(chat_id="KINBIN247_bot",message_ids=message.message_id)
#    

@app.on_message(filters.poll & filters.chat("KINBIN247_bot") & filters.incoming)
def forword(client:Client,message:Message):
    
    client.forward_messages(chat_id="Soojhboojh_01bot",from_chat_id=message.chat.id,message_ids=message.message_id)
    app.delete_messages(chat_id="KINBIN247_bot",message_ids=message.message_id)


@app.on_message(filters.regex("https://t.me/.*?/\d{1,}/\d{1,}") & filters.chat("jsjdkdkkd") & filters.outgoing )
def forword(client:Client,message:Message):
    chatid=message.text
    chatid=reaaa.sub("https://t.me/","",chatid)
    chatid=reaaa.split("/",chatid)
    print(chatid)
    for x in range(int(chatid[2])):
       app.forward_messages(chat_id="KINBIN247_bot",from_chat_id=chatid[0],message_ids=int(chatid[1])+x)


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
import re


from telegram.ext.dispatcher import run_async
import logging
import os
import json
from functools import wraps
#using cloudmersive api
import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException

def send_typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)
        return func(update, context,  *args, **kwargs)

    return command_func

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

@run_async
@send_typing_action
def start(update, context):
  update.message.reply_text("Bot                    :                  @soojhboojh \nWeb                  :                 Soojhboojh.xyz \nBot                    :         @Soojhboojh_02bot\nMain Bot          :   @Soojhboojhbot ( @ANKITAdidi )")

@run_async
@send_typing_action
def channels(update, context):
  update.message.reply_text( 'Welcome to Channels\nMath Channel   https://t.me/Math_quiz_ans' )
  update.message.reply_text( 'Math Group   https://t.me/Royalworldmathdoubt' )
  update.message.reply_text('Math Channel  https://t.me/Maths_Quiz_Notes')
  update.message.reply_text( 'Math Group   https://t.me/learnwithaditya' )
  update.message.reply_text('All SUBQUIZ   https://t.me/makefuturebright')
  update.message.reply_text('Math Question Bot   https://t.me/soojhboojh')

@run_async
@send_typing_action
def owner(update, context):
  update.message.reply_text("send your suggestions\n    1. @kinbin247 \n  2. @ANKITAdidi \n 3. comming soon \ud83d\ude1c")

LIST_OF_ADMINS = ["711296045", "555919730"]

def restricted(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        userName = str(update.message.from_user.id)
        if userName not in LIST_OF_ADMINS:
            print("start")#update.message.reply_text(f"Unauthorized access denied for {update.effective_user.mention_html()}.", parse_mode=ParseMode.HTML)
            return
        return func(update, context, *args, **kwargs)
    return wrapped

import asyncio
from text_to_poll import texttopoll


@restricted
@run_async
@send_typing_action
def poll(update, context):
    """Sends a predefined poll"""
    questions = ["Math_quiz_ans", "Royalworldmathdoubt", "Maths_Quiz_Notes", "learnwithaditya", " makefuturebright", "soojhboojh"]
    #que = update.message.text()
    quest=(update.message.text)
    asyncio.run(texttopoll(quest,update,context))
    if update.effective_chat.id<=0:
            time.sleep(5)
   
   

@restricted
@run_async
@send_typing_action
def receive_poll_answer(update, context):
    """Summarize a users poll vote"""
    answer = update.poll_answer
    poll_id = answer.poll_id
    try:
        questions = context.bot_data[poll_id]["questions"]
    # this means this poll answer update is from an old poll, we can't do our answering then
    except KeyError:
        return
    selected_options = answer.option_ids
    answer_string = ""
    for question_id in selected_options:
        if question_id != selected_options[-1]:
            answer_string += questions[question_id] + " and "
        else:
            answer_string += questions[question_id]
    context.bot.send_message(
        context.bot_data[poll_id]["chat_id"],
        "{} feels {}!".format(update.effective_user.mention_html(), answer_string),
        parse_mode=ParseMode.HTML,
    )
    context.bot_data[poll_id]["answers"] += 1
    # Close poll after three participants voted
    if context.bot_data[poll_id]["answers"] == 100:
        context.bot.stop_poll(
            context.bot_data[poll_id]["chat_id"], context.bot_data[poll_id]["message_id"]
        )

@restricted
@run_async
@send_typing_action
def quiz(update, context):
    """Send a predefined poll"""
    questions = ["1", "2", "4", "20"]
    message = update.effective_message.reply_poll(
        "How many eggs do you need for a cake?", questions, type=Poll.QUIZ, correct_option_id=2
    )
    # Save some info about the poll the bot_data for later use in receive_quiz_answer
    payload = {
        message.poll.id: {"chat_id": update.effective_chat.id, "message_id": message.message_id}
    }
    context.bot_data.update(payload)

@restricted
@run_async
@send_typing_action
def receive_quiz_answer(update, context):
    """Close quiz after three participants took it"""
    # the bot can receive closed poll updates we don't care about
    if update.poll.is_closed:
        return
    if update.poll.total_voter_count == 10:
        try:
            quiz_data = context.bot_data[update.poll.id]
        # this means this poll answer update is from an old poll, we can't stop it then
        except KeyError: 
            return
        context.bot.stop_poll(quiz_data["chat_id"], quiz_data["message_id"])
i=0
ind=0
indt=1000000
apino=1000000
x=["dab10e83"]
x=list(dict.fromkeys(x))
@run_async
@send_typing_action
def convert_image(update,context):
    global filename
    global chat_id
    chat_id=update.message.chat_id
    global ind
    global i
    
    #i=0
    #ind=0
    i=i+1
    
    if(ind == len(x)):
        ind=0
    if indt!=1000000:
        ind=indt
            
   
    filename="testing.jpg"
    #context.bot.send_message(chat_id=chat_id , text="number of images are = ")
    #context.bot.send_message(chat_id=chat_id , text = "Photo no. {}".format(i))
    #context.bot.send_message(chat_id=chat_id , text = "Api no. {}".format(ind+1))

    global file_id
    file_id = update.message.photo[-1].file_id
    newFile=context.bot.get_file(file_id)
    newFile.download(filename)
    #Till now we downloaded the image file
    #global chat_id
    #chat_id=update.message.chat_id
    context.bot.send_message(chat_id=chat_id , text="Yeah!,I got your image let me process it")

    # Now we are using inline keyboard for getting the language input from user
    keyboard = [[InlineKeyboardButton("English ", callback_data='ENG'),InlineKeyboardButton("Hindi", callback_data='HIN'), InlineKeyboardButton("Russian", callback_data='RUS'),InlineKeyboardButton("Czech", callback_data='CES')],
                [InlineKeyboardButton("Chinese simplified", callback_data='ZHO'), InlineKeyboardButton("Chinese Traditional", callback_data='ZHO-HANT'),InlineKeyboardButton("Japanese", callback_data='JPA'),InlineKeyboardButton("Indonesian", callback_data='IND')] ,
                [InlineKeyboardButton("Arabic", callback_data='ARA'),InlineKeyboardButton("Afrikans", callback_data='AFR'), InlineKeyboardButton("German", callback_data='DEU'),InlineKeyboardButton("French", callback_data='FRA')],
                [InlineKeyboardButton("Italian", callback_data='ITA'), InlineKeyboardButton("Urdu", callback_data='URD'),InlineKeyboardButton("Malayalam", callback_data='MAL'),InlineKeyboardButton("Tamil", callback_data='TAM')],
                [InlineKeyboardButton("Hebrew", callback_data='HEB'), InlineKeyboardButton ("Bengali" , callback_data='BEN'), InlineKeyboardButton ("Spanish", callback_data='SPA'), InlineKeyboardButton ("Persian",callback_data='FAS')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Select Language : ', reply_markup=reply_markup)
    return convert_image

@run_async
def button(update, context):
    global query
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Selected Language is: {}".format(query.data))



    configuration = cloudmersive_ocr_api_client.Configuration()
    #Enter Your cloudmersive api key in place of  os.environ.get(...........)
    configuration.api_key['Apikey'] = x[ind]


    api_instance = cloudmersive_ocr_api_client.ImageOcrApi(cloudmersive_ocr_api_client.ApiClient(configuration))
    print(api_instance)
    try:
        lang=query.data
        api_response = api_instance.image_ocr_post(filename,language=lang)
        #confidence=api_response.mean_confidence_level
        #context.bot.send_message(chat_id=chat_id , text="Confidence : "+str(confidence*100)+"% \nExtracted text:\n")
        context.bot.send_message(chat_id=chat_id , text="{}\n{}/{}".format(i,ind+1,len(x)+1))
        context.bot.send_message(chat_id=chat_id , text=api_response.text_result)
    except ApiException as e:
        global indt
        
        indt=ind
        
        
        #context.bot.send_message(chat_id=chat_id , text="teasting 01")
        #convert_image(update,context)
        #context.bot.send_message(chat_id=chat_id , text="changing Api I\'d No. = {}".format(ind+2))
        
        context.bot.send_message(chat_id=chat_id , text="Waiting...")
        my_fun(indt)
        indt=apino
        print("finish")
        context.bot.send_message(chat_id=chat_id , text="{}\n{}/{}".format(i,indt+1,len(x)+1))
        context.bot.send_message(chat_id=chat_id , text="{}".format(imgtext))
        print("start")
        #context.bot.send_message(chat_id=chat_id , text="Exception when calling ImageOcrApi->image_ocr_photo_to_text: %s\n" % e)
        try:
            os.remove('testing.jpg')
        except Exception:
            pass
    return button

@restricted
def my_fun(indz):
    if indz==len(x):
        indz=0
    else:
      indz+=1
    print(indz)
    configuration = cloudmersive_ocr_api_client.Configuration()
    #Enter Your cloudmersive api key in place of  os.environ.get(...........)
    configuration.api_key['Apikey'] = x[indz]
    
    api_instance = cloudmersive_ocr_api_client.ImageOcrApi(cloudmersive_ocr_api_client.ApiClient(configuration))
    print(query.data)
    print(api_instance)
    try:
        lang=query.data
        print("start")
        api_response = api_instance.image_ocr_post(filename,language=lang)
        #confidence=api_response.mean_confidence_level
        #context.bot.send_message(chat_id=chat_id , text="Confidence : "+str(confidence*100)+"% \nExtracted text:\n")
        global imgtext
        imgtext=api_response.text_result
        global apino
        apino=indz
        print("good")
        #print(api_response.text_result)
        
        #update.message.reply_text(api_response.text_result)
        print("finish")
    except ApiException as e:
        my_fun(indz)
        print("yo kya huaa")
        

def donate(update,context):
    update.message.reply_text("Thanks for tap.\nThanks you bro chennal Channel = @botsbyamit \nIf someone really want to donate follow Channel = @botsbyamit",parse_mode=ParseMode.MARKDOWN)
    return donate 

@run_async
@send_typing_action
def preview(update, context):
    """Ask user to create a poll and display a preview of it"""
    # using this without a type lets the user chooses what he wants (quiz or poll)
    button = [[KeyboardButton("Press me!", request_poll=KeyboardButtonPollType())]]
    message = "Press the button to let the bot generate a preview for your poll"
    # using one_time_keyboard to hide the keyboard
    update.effective_message.reply_text(
        message, reply_markup=ReplyKeyboardMarkup(button, one_time_keyboard=True)
    )


#@run_async
@restricted
@send_typing_action
def receive_poll(update, context):
    """On receiving polls, reply to it by a closed poll copying the received poll"""
    actual_poll = update.effective_message.poll
    # Only need to set the question and options, since all other parameters don't matter for
    # a closed poll
    #update.message.reply_text(str(actual_poll))
    #ex="@Soojhboojhbot/n"
    ex =actual_poll.explanation
    #update.message.reply_text("1")
    if ex is None:
        ex=""
        #ex="👇👇👇 Ask your Doubts here 👇👇👇\n👇👇👇        Only for Math        👇👇👇\nhttps://soojhboojh.xyz/ask-question/"
    else:
        ex=reaaa.sub(r"\@.*?\s", "", ex)
        ex=reaaa.sub(r"\@\w.*", "", ex)
    
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
        #update.message.reply_text("<pre>"+q+"</pre>",parse_mode=telegram.ParseMode.HTML)
        #for r in options:
        	#update.message.reply_text("<pre>"+r+"</pre>",parse_mode=telegram.ParseMode.HTML)
        options="\n".join(options)
        T=q+"\n"+options+"\n"+cor
        update.message.reply_text("<pre>"+T+"</pre>",parse_mode=telegram.ParseMode.HTML)
    
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







@restricted
@run_async
@send_typing_action
def help_handler(update, context):
    """Display a help message"""
    update.message.reply_text("Use /quiz, /poll or /preview to test this " "bot." )
    update.message.reply_text("created by Mohit Sharma" )
    update.message.reply_text("send me a POLL" )
    update.message.reply_text(" I CAN CREATE.\n\n30 voting poll. \n             &\n OCR thing compcompletely shut down." )




SUBQUIZ, POLLSUB , POLLREPLACE , POLLEXPS= range(4)

def sub(update: Update, _: CallbackContext) -> int:
    if i==0:
    	update.message.reply_text(
        "Send me TEXT that you want me to Regrx.\n\nyou can study Regrx here\n\nhttps://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285"
		)
    elif i>0:
    	update.message.reply_text("After "+Textstr2[i-1]+ " what you want me to replace you. You can text me only.")

    return SUBQUIZ

tsr=""
i=0

Textstr2=[]
@restricted
#@run_async
@send_typing_action
def sub_quiz(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    global Textstr2
    
    Textstr2.append(update.message.text)
    if i==0:
    	update.message.reply_text("Send me Text \"NEW REPLACE TEXT\"\nfor empty use /nil\nfor cancel use /cancel")
    
    return POLLREPLACE

Textstr3=[]
#@run_async
@send_typing_action
@restricted
def poll_replace(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    global Textstr3
    global i
    global tsr
    Textstr3.append(update.message.text)
    update.message.reply_text("List what you can do.\n1. Text(Replace)\n2. Poll (in poll for adding explanation use /add_explanation )\n3. /cancel")
    
    if True:
    	tsr=tsr+"\n"+Textstr2[i]+" ➢ ➣ ➤ "+Textstr3[i]
    	update.message.reply_text("Replace sequence\n\n"+tsr+ "\n\nLooking Good!")
    if Textstr3[i]=="/nil":
    	Textstr3[i]=""
    i+=1

    return POLLSUB

@restricted
@send_typing_action
def poll_sub(update: Update, _: CallbackContext) -> int:
    #update.message.reply_text("yoo")
    user = update.message.from_user
    userText=update.message.poll
    global q
    global options
    global corr
    q=userText.question
    q=reaaa.sub("(\[\d{1,}/\d{1,}\] ){1,}((Q|)(\d{1,}|)(_|)(\d{1,}|)(\.|)( |)){1,}","",q)
    options=[o.text for o in userText.options]
    corr=userText.correct_option_id
    for z in range(len(Textstr2)):
	    print(Textstr2[z])
	    print(Textstr3[z])
	    q=reaaa.sub(Textstr2[z],Textstr3[z], q)
	    for op in range(len(options)):
	    	options[op]=reaaa.sub(Textstr2[z], Textstr3[z], options[op])
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
    #update.message.reply_text("send me more polls or /cancel")
    return POLLSUB

#@run_async
@restricted
@send_typing_action
def poll_exp(update: Update, _: CallbackContext) -> int:
    update.message.reply_text("Send me your explanation.")
    return POLLEXPS

exp=""
@send_typing_action
@restricted
def poll_exps(update: Update, _: CallbackContext) -> int:
    #update.message.reply_text("yoo")
    exp = update.message.text
    update.effective_message.reply_poll(
            question= q,
            options=options,
            # with is_closed true, the poll/quiz is immediately closed
            type=Poll.QUIZ,
            correct_option_id =corr,
            explanation=exp,
            #is_closed=True,
            is_anonymous=True,
            reply_markup=ReplyKeyboardRemove()
    )
    #update.message.reply_text("send me more polls or /cancel")
    return POLLSUB



@restricted
def cancel(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    global tsr , Textstr2, Textstr3, i
    tsr=""
    i=0
    Textstr2=[]
    Textstr3=[]
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END



def main():
    bot_token=os.environ.get("BOT_TOKEN_1", "")
    #bot_token='1355592440:AAEG7NPTJrJXAj40NYVltjGTTpKUBgze4lc'
    updater = Updater(bot_token,use_context=True)
    conv_handler02 = ConversationHandler(
        entry_points=[CommandHandler('sub', sub)],
        states={
            SUBQUIZ: [MessageHandler(Filters.regex('^.*$'), sub_quiz)],
            POLLSUB: [MessageHandler(Filters.poll, poll_sub), MessageHandler(Filters.regex('^.*$') & ~Filters.command, sub_quiz), CommandHandler('add_explanation', poll_exp)],
            POLLREPLACE: [MessageHandler(Filters.regex('^.*$'), poll_replace)],
            POLLEXPS: [MessageHandler(Filters.text, poll_exps)]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    
    
    dp = updater.dispatcher
    dp.add_handler(conv_handler02)
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('channels', channels))
    dp.add_handler(CommandHandler('owner', owner))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, poll))
    dp.add_handler(PollAnswerHandler(receive_poll_answer))
    dp.add_handler(CommandHandler('quiz', quiz))
    dp.add_handler(PollHandler(receive_quiz_answer))
    dp.add_handler(CommandHandler('preview', preview))
    
    dp.add_handler(MessageHandler(Filters.poll, receive_poll))
    dp.add_handler(CommandHandler('help', help_handler))
    dp.add_handler(MessageHandler(Filters.photo, convert_image))
    dp.add_handler(CommandHandler('donate', donate))
    
    #dp.add_handler(MessageHandler(Filters.photo, convert_image))
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    app.run()
    updater.idle()
    
if __name__ == '__main__':
    main()