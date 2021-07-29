from pymongo import MongoClient
import dns

'''import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] # this is a google public dns server,  use whatever dns server you like here
# as a test, dns.resolver.query('www.google.com') should return an answer, not an exception'''
client=MongoClient('mongodb+srv://Kinshu04101:Qwert123@cluster0.ckcyx.mongodb.net/test?retryWrites=true&w=majority')

#!/usr/bin/env pyth
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
import re as reaaa
import json
import logging
import os
from functools import wraps
import xlsxwriter
import sqlite3
from telegram.ext.dispatcher import run_async

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, Poll, Update, ChatAction, ParseMode
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

GENDER, PHOTO, LOCATION, BIO, QUIZ, DELETE, RESULT, TIME, Re = range(9)



def send_typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)
        return func(update, context,  *args, **kwargs)

    return command_func


LIST_OF_ADMINS = ["Kinbin247", "Harsh_Avasthi", "TOXIC_MAVI"]

def restricted(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        
        userName = update.message.chat.username
        userName1=update.message.from_user.username
        if userName and userName1 not in LIST_OF_ADMINS:
            #update.message.reply_text(f"Unauthorized access denied for {update.effective_user.mention_html()}.", parse_mode=ParseMode.HTML)
            return
        return func(update, context, *args, **kwargs)
    return wrapped


def restricted1(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        col=client["Quiz_Admin"]["LIST_OF_ADMINS1"]
        x=col.find({})
        LIST_OF_ADMINS1=[]
        for y in x:
            z=y["User_ID"]
            LIST_OF_ADMINS1.append(z)
        #LIST_OF_ADMINS1 = ["Kinbin247", "Harsh_Avasthi", "TOXIC_MAVI", "imKkala", "Om_2611","Gksgj", "ANKITAdidi", "Sharma_jii_ki_betii","yogeshogesh","Unacademy_Quizerrr", "JayBhim00"]

        mid=update.message.message_id
        userName = update.message.chat.username
        #print(userName)
        userName1=update.message.from_user.id
        chatiid=int(update.message.chat.id)
        #print(chatiid)
        chatiid=int(update.message.chat.id)
        	
        
        
        
        if userName1 not in LIST_OF_ADMINS1:
            
            try:
            	if chatiid<=0:
            		
            		try:
            			chatiid="@"+str(update.message.chat.username)#id
            			print("chatid="+str(chatiid))
            			print("message*d"+str(mid))
            		except Exception as e:
            			print(str(e))
            	
            except Exception as e:
            	print(str(e))
            context.bot.delete_message(chat_id=str(chatiid),message_id=mid)
            return
            #update.message.reply_text(f"Unauthorized access denied for {update.effective_user.mention_html()}.", parse_mode=ParseMode.HTML)
            
        return func(update, context, *args, **kwargs)
    return wrapped

def restricted2(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        uid=update.message.from_user.id
        chatiid=int(update.message.chat.id)
        mid=update.message.message_id
        try:
	        y=context.bot.get_chat_administrators(chat_id=chatiid)
	        xid=[]
	        for x in y:
	        	print(x['user']['id'])
	        	xid.append(x['user']['id'])
        except:
        	pass
        if chatiid<=0:
            try:
            	try:
            		 context.bot.delete_message(chat_id=str(chatiid),message_id=mid)
            	except:
            		 pass
            	if uid in xid or uid==711296045:
            		return func(update, context, *args, **kwargs)
            	else:
            		return
            		
            except Exception as e:
            	print(str(e))
            
            
            #update.message.reply_text(f"Unauthorized access denied for {update.effective_user.mention_html()}.", parse_mode=ParseMode.HTML)
        else:
        	return func(update, context, *args, **kwargs)
    return wrapped



LIST_OF_ADMINS_D = ["Kinbin247", "Harsh_Avasthi", "TOXIC_MAVI"]
def restrictedD(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        global Xiii
        if Xiii==1:
            due=10
            chat_id11=711296045
            context.job_queue.run_once(alarm, due, context=chat_id11, name=str(chat_id11))
            Xiii+=1
        else:
            pass
        mid=update.message.message_id
        userName = update.message.chat.username
        #print(userName)
        userName1=update.message.from_user.username
        chatiid=int(update.message.chat.id)
        #print(chatiid)
        chatiid=int(update.message.chat.id)
        if userName and userName1 in LIST_OF_ADMINS_D: # or userName is None:
            try:
            	if chatiid<=0:
            		
            		try:
            			chatiid="@"+str(update.message.chat.username)#id
            			print("chatid="+str(chatiid))
            			print("message*d"+str(mid))
            		except Exception as e:
            			print(str(e))
            	
            except Exception as e:
            	print(str(e))
            context.bot.delete_message(chat_id=str(chatiid),message_id=mid)
            return func(update, context, *args, **kwargs)
            #update.message.reply_text(f"Unauthorized access denied for {update.effective_user.mention_html()}.", parse_mode=ParseMode.HTML)
            
        return 
    return wrapped



@run_async
@send_typing_action
def createquiz(update: Update, _: CallbackContext) -> int:
    

    update.message.reply_text(
        "Hello Quizers \n\n Send me a name of your quiz..."
    )

    return GENDER

Textstr=""
#@run_async
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



i=0
#@run_async
def photo(update: Update, _: CallbackContext) -> int:
    user = update.effective_message.poll
    '''photo_file = update.message.photo[-1].get_file()
    photo_file.download('user_photo.jpg')
    logger.info("Photo of %s: %s", user.first_name, 'user_photo.jpg')'''
    question=user.question
    question= reaaa.sub(r"@\w*", "", question)
    question= reaaa.sub(r"^(\[\d{1,}/\d{1,}\] ){1,}", "", question)
    options=[o.text for o in user.options]
    correct_option_id=user.correct_option_id
    exp=user.explanation
    if exp is not None:
    	exp= reaaa.sub(r"@\w*", "", exp)
    	exp= reaaa.sub(r"(\n| |)join(\n| |)", "", exp)
    
    if exp is None:
    	exp=""
    new={'que':question, 'op':options, 'cor':correct_option_id, 'exp':exp, 'ID':Textstr, 'User_ID':update.message.chat.id}
    col=client["Quiz_Data"][Textstr]
    col.insert_one(new)
    update.message.reply_text("Send me more polls or finish using /skip")
    return PHOTO

#@run_async
def skip_photo(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s did not send a poll.", user.first_name)
    return ConversationHandler.END

i=0
def location(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    user_location = update.message.text
    '''logger.info(
        "Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude
 )'''
    
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

@run_async
def cancel(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


@run_async
@restricted
@send_typing_action
def playquiz(update,context):
    
    global chatid
    chatid=update.message.chat.id
    context.bot.send_message(chat_id=chatid, text="Time in seconds. limit (5-600) .")

    return TIME
Time=30
@run_async
def time0(update,context):
    global Time
    userText=update.message.text
    Time=userText

    context.bot.send_message(chat_id=chatid, text="Send me Quiz Name")

    return QUIZ


Textstr0=""
#@run_async
def quiz(update,context):
    user = update.message.from_user
    global payload
    global Textstr0
    global chatid
    global J
    J=0
    chatid=update.effective_chat.id
    userText=update.message.text
    Textstr0=userText
    col=client["Quiz_Data"][userText]
    coldb=col.find()
    #new={'que':question, 'op':options, 'cor':correct_option_id, 'exp':exp, 'ID':Textstr, 'User_ID':update.message.chat.id}
    if True:
        try:
            
            context.bot.send_message(chat_id=chatid, text="🎲 Get ready for the LIVE TEST \'"+userText+"\'\n\n🖊 "+str(col.count_documents({}))+" questions\n⏱ "+Time+" seconds per question\n📰 Votes are visible to group members only\nevery ✔︎ Question gain ✙4 Marks\nevery ✖︎ Question gain –1 Mark\n\n<b>At least 1 voting for last 3 questions far calculating Results.</b>", parse_mode=ParseMode.HTML)
            mes=context.bot.send_message(chat_id=chatid, text="Quiz is about to start")
            time.sleep(2)
            for xooo in range(6):
                if xooo!=5:
                    context.bot.editMessageText(chat_id=chatid, message_id=mes.message_id, text=str(5-xooo))
                    time.sleep(1)
                if xooo==5:
                    context.bot.editMessageText(chat_id=chatid, message_id=mes.message_id, text="Best Of Luck 👍👍👍")
                    time.sleep(1)
            y=0
            for X in coldb:
                
                Zno=col.count_documents({})-y
                question=str(Zno)+". "+X["que"]
                options=X["op"]
                correct_option_id =X['cor']
                exp=X["exp"]
                message = context.bot.send_poll(
                    update.effective_chat.id,
                    question=question,
                    options=options,
                    # with is_closed true, the poll/quiz is immediately closed
                    type=Poll.QUIZ,
                    correct_option_id =correct_option_id,
                    open_period=int(Time),
                    explanation=exp,
                    is_closed=False,
                    is_anonymous=False,
                    reply_markup=ReplyKeyboardRemove(),
                )
                time.sleep(int(Time))
                try:
                    payload = {
                        message.poll.id: {
                            "cor": question,
                            "options": options,
                            "cor":correct_option_id,
                            "message_id": message.message_id,
                            "chat_id": update.effective_chat.id,

                        }
                    }
                    context.bot_data.update(payload)
                
                except Exception as e:
                    pass
                
            
            
            

            
        except:
            update.message.reply_text("Name not exist.", reply_markup=ReplyKeyboardRemove(),)
    
    #update.message.reply_text("/result")
    try:
        return ConversationHandler.END
    except Exception as e:
        pass
        #print(e)
    



re=""
def res(update: Update, context: CallbackContext) -> None:
    #print("quiz finish")
    global re
    global dbR
    with open('Result.html') as json_file:
        dbR = json.load(json_file)
    #print(str(dbR))
    #print("gghhjj")
    with open('Newfile.text') as json_file:
        db = json.load(json_file)
    try:
        List=list(db[Textstr0]['que'])
        Q=len(List)
        List=list(dbR[Textstr0].keys())
        P=len(List)
        #print(str(List))
        for L in range(P):
                Fname=dbR[Textstr0][List[L]]['fname']
                ##print(Fname)    
                Uname=dbR[Textstr0][List[L]]['uname']
                ##print(Uname)
                Rs=dbR[Textstr0][List[L]]['result'][0]
                ##print(Rs)
                re=re+"\n"+Fname+" gain "+str(Rs)+"/"+str(Q*4)+" Marks"
                #print(re)
        update.message.reply_text("🏁 The quiz \'"+Textstr0+"\' has finished!\n\n"+str(len(db[Textstr0]['que']))+" questions answered\n\n"+re)
        re=""
    except:
        update.message.reply_text("quiz not found")
    return ConversationHandler.END
    

    

@restricted
@run_async
def deletequiz(update: Update, _: CallbackContext) -> int:
    
    #global Uid
    #Uid=update.message.user_id
    update.message.reply_text(
        "Hello Quizers \n\n Send me a name of your quiz you want to DELETE."
    )

    return DELETE

Textstr1=""
@run_async
@send_typing_action
def delete(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    global Textstr1
    userText=update.message.text
    Textstr1=userText
    try:
	    col=client["Quiz_Data"][userText]
	    coldb=col.find({'User_ID':update.message.chat.id})
	    #new={'que':question, 'op':options, 'cor':correct_option_id, 'exp':exp, 'ID':Textstr, 'User_ID':update.message.chat.id}
	    x=int(len(coldb))
	    y=int(col.count_documents({}))
	    if  x==y or update.message.chat.username in LIST_OF_ADMINS:
	        col.drop()
	        update.message.reply_text("Quiz "+userText+" deleted", reply_markup=ReplyKeyboardRemove(),)
	    elif len(coldb)!=0:
	        col.delete_many({'User_ID':update.message.chat.id})
	        update.message.reply_text("In 👉 "+userText+" Quiz deleted only your questions not someone else questions.", reply_markup=ReplyKeyboardRemove(),)
	    else:
	    	update.message.reply_text("👉 "+userText+" Quiz not yours and you are not bot admin so you do not have rights to DELETE it.", reply_markup=ReplyKeyboardRemove(),)
    except:
    	update.message.reply_text("👉 "+userText+" Quiz not found in database.", reply_markup=ReplyKeyboardRemove(),)
    return ConversationHandler.END
    

#@restricted
@run_async
def quizlist(update,context):
    chat__id=int(update.message.chat.id)
    context.bot.delete_message(chat_id=chat__id,message_id=update.message.message_id)
    db=client["Quiz_Data"]
    x=(db.list_collection_names({}))
    for y in x:
    	context.bot.send_message(chat_id=chat__id,text="<pre>"+y+"</pre>", parse_mode=ParseMode.HTML,disable_web_page_preview = True)
    	


RESULT=range(1)
#@run_async
@restricted1
@send_typing_action
def quizresult(update, context):
    global dbR
    global chat__id
    global meid
    global mesho3
    chat__id=int(update.message.chat.id)
    if chat__id<=0:
    	try:
    		chat__id="@"+str(update.message.chat.username)#id
    	except Exception as e:
    		print(str(e))
    else:
    	pass
    me=context.bot.send_message(chat_id=chat__id, text="Send me Quiz name")
    meid=me.message_id
    return RESULT
    
def result(update: Update, context: CallbackContext):
    global COUNTR
    userTex=update.message.text
    userTex1=userTex
    COUNTJ=0
    rnumb=1
    coll=client["Quiz_Data"][userTex]
    cx=coll.find_one()
    colldb=coll.count_documents({})
    #if cx["User_ID"]
    try:
	    col=client["Quiz"][userTex]
	    context.bot.delete_message(chat_id=chat__id,message_id=meid)
    except Exception as e:
	    print("connection fail "+str(e))
    mydoc = col.find().sort("Marks", -1)
    try:
        
        colme=client["Quiz"]["Message"]
        coldoc={"ID":chat__id+"_"+userTex1}
        print("ID==="+chat__id+"_"+userTex1)
        Colm=colme.find_one(coldoc)
        colmessage=Colm["MessID"]
        print(colmessage)
    except Exception as e:
        print("colmessage=="+str(e))
    
    try:
        if True:
            if True:
                try:
                    if True:
                        if True:
                            try:
                                os.remove('Result.xlsx')
                            except:
                                print("removing Result.xlsx File")
                            workbook = xlsxwriter.Workbook('Result.xlsx')
                            worksheet = workbook.add_worksheet()
                            cell_format = workbook.add_format()
                            cell_format1 = workbook.add_format()
                            cell_format10 = workbook.add_format()
                            cell_format.set_align('center')
                            cell_format1.set_align('center')
                            cell_format1.set_font_color('green')
                            cell_format1.set_bold()
                            worksheet.set_column('A:A', 5)
                            worksheet.set_column('C:E', 9)
                            worksheet.set_column('B:B', 37)
                            worksheet.set_column('F:F', 17)
                            worksheet.write('A1', 'Rank', cell_format1)
                            worksheet.write('B1', 'Name', cell_format1)
                            worksheet.write('C1', '︎✔︎ Options', cell_format1)
                            worksheet.write('D1', '︎✖ Options', cell_format1)
                            worksheet.write('E1', 'Marks', cell_format1)
                            worksheet.write('F1', 'User Name', cell_format1)
                            cell_format10.set_align('center')
                            cell_format10.set_num_format('[Green]General;[Red]-General;General')
                            COUNTR=""
                            for x in mydoc:
                                Fname=x["Fname"]
                                Rname=x["✔︎"]
                                Wname=x["︎✖"]
                                Uname=x["User_Name"]
                                Usid=x["User_ID"]
                                Rs=x["Marks"]
                                #print("data loading start")
                                if Uname !="None":
                                	if COUNTJ<=9:
                                		COUNTR=COUNTR+""+str(COUNTJ+1)+". <b>@"+str(Uname)+"</b> 🎰 "+str(Rs)+"\n"
                                		COUNTJ+=1
                                else:
                                	if COUNTJ<=9:
                                		COUNTR=COUNTR+""+str(COUNTJ+1)+". <a href=\"tg://openmessage?user_id="+str(Usid)+"\"><b>"+Fname+"</b></a> 🎰 "+str(Rs)+"\n"
                                		COUNTJ+=1
                                
                                
                                
                                worksheet.write('A'+str(rnumb+1), str(rnumb), cell_format)
                                if False:
                                	worksheet.write_url('B'+str(rnumb+1), "tg://openmessage?user_id="+str(Usid), cell_format=cell_format, string=str(Fname))
                                else:
                                 	worksheet.write_url('B'+str(rnumb+1), "tg://openmessage?user_id="+str(Usid), cell_format=cell_format, string=str(Fname))
                                worksheet.write('C'+str(rnumb+1), str(Rname), cell_format)
                                worksheet.write('D'+str(rnumb+1), str(Wname), cell_format)
                                worksheet.write('E'+str(rnumb+1), int(Rs), cell_format10)
                                if Uname is None:
                                	worksheet.write('F'+str(rnumb+1), 'None', cell_format)
                                else:
                                	worksheet.write('F'+str(rnumb+1), "@"+str(Uname), cell_format)
                                	Uname=None
                                #print(COUNTR)
                                rnumb+=1
                            workbook.close()
                            print("webhook close")
                            
                                    
                            
                except Exception as e:
                    print("e===="+str(e))
                    context.bot.send_document(chat_id=chat__id, text="quiz not found")
        caption1="🏁 The quiz \'"+userTex+"\' has finished!\nQuiz Attempt 👉🏻 "+str(col.count_documents({"User_ID":{ "$type" : "int" }}))+" Persons.\nCurrent Time = "+str(time.ctime(time.time() +19800))+" \n"+str(colldb)+" questions answered\n\n"+COUNTR+"\n🏆 Congratulations to the winners! 🍟"
        #print(caption1)
        try:
        	context.bot.send_document(chat__id, open('Result.xlsx', "rb"),caption=caption1, parse_mode=ParseMode.HTML,reply_to_message_id=colmessage)
        	print(colmessage)
        except Exception as e:
        	print(str(e))
        	context.bot.send_document(chat__id, open('Result.xlsx', "rb"),caption=caption1, parse_mode=ParseMode.HTML)
    except Exception as e:
        context.bot.send_message(chat_id=chat__id, text="no live quiz at now come next time.\n error name = "+str(e))
    return ConversationHandler.END

'''
@restricted
@run_async
@send_typing_action
def downloadfile(update,context):
    #global Uid
    #Uid=update.message.user_id
    f = 'Newfile.text'
    #print("1")
    chat_id=update.effective_chat.id
    #print(chat_id)
    with open(f, "rb") as file:
        context.bot.send_document(chat_id, document=file)
     
        
        try:
            context.bot.send_document(chat_id, document=file)
        except Exception as e:
            #print(e)
'''
#@run_async
@send_typing_action
def downloadfile(update,context):
    f = ['Newfile.text','test.db']
    #print("1")
    chat_id=update.effective_chat.id
    #print(chat_id)
    #with open(f, "rb") as file:
        #context.bot.send_document(chat_id, document=file)
     
        
    try:
        for x in f:
            context.bot.send_document(chat_id, open(x, "rb"))#document=file)
    except Exception as e:
        #pass
        print(e)
    
UPLOAD =range(1)

@restricted
@send_typing_action
def uploadfile(update,context):
    #global Uid
    #Uid=update.message.user_id
    update.message.reply_text("send me file.")
    return UPLOAD

def upload(update,context):
    global filename
    filename="testing.text"
    try:
        os.remove('testing.text')
    except Exception:
        pass
    global file_id
    #print("123345")
    file_id = update.message.document.file_id
    newFile = context.bot.get_file(file_id)
    qwer=newFile.download(filename)
    with open(qwer) as json_file:
        dbq = json.load(json_file)
    
    with open('Newfile.text', 'w') as outfile:
        #json.dump(dbw, outfile)
        json.dump(dbq, outfile)
    
    update.message.reply_text("photo upload")
    return ConversationHandler.END
    

CHN, GHN =range(2)

@run_async
@restricted
@send_typing_action
def playinc(update,context):
    
    global chatid
    chatid=update.message.chat.id
    context.bot.send_message(chat_id=chatid, text="Time in seconds. limit (5-600) .")

    return TIME
Time=30
@run_async
def time0c(update,context):
    global Time
    userText=update.message.text
    Time=userText

    context.bot.send_message(chat_id=chatid, text="Send me group username")
    return CHN

@run_async
def chn(update,context):
    global channelid
    channelid=update.message.text
    channelid=reaaa.sub("(https|http)://t\.me/", "@", channelid)
    print(channelid)
    context.bot.send_message(chat_id=chatid, text="Send me Quiz Name")

    return QUIZ

Cid={}
ZMid={}
Textstr0=""
#@run_async
def quizc(update,context):
    #user = update.message.from_user
    global payload
    global Textstr0
    global J
    global chatid
    global Cid
    global Mid
    global ZMid
    Mid = []
    J=0
    
    userText=update.message.text
    
    Textstr0=userText
    
    coll=client["Quiz_Data"][userText]
    colldb=coll.find()
    if True: 
        try:
            messa=context.bot.send_message(chat_id=channelid, text="🎲 Get ready for the LIVE TEST \'"+userText+"\'\n\n🖊 "+str(coll.count_documents({}))+" questions\n\n⏱ Voting Start "+str(time.ctime(time.time() +19800))+"\n\n⏱ Voting End "+str(time.ctime(time.time() + int(Time) +19800))+" \n\n📰 Votes are visible to group members and shared all polls \nevery ✔︎ Question gain ✙4 Marks\nevery ✖︎ Question gain –1 Mark\n\n<b>Result Comes on "+str(time.ctime(time.time() + int(Time)+19800))+"\n\nPlaying Group "+str(channelid)+"\n\nFor more #Soojh_Boojh</b>", parse_mode=ParseMode.HTML)
            colme=client["Quiz"]["Message"]
            coldoc={"MessID":messa.message_id,"ID":channelid+"_"+userText}
            try:
            	colme.delete_many({"ID":channelid+"_"+userText})
            except Exception as e:
            	print("First time play or not play. "+str(e))
            colme.insert_one(coldoc)
            mes=context.bot.send_message(chat_id=channelid, text="Quiz is about to start")
            time.sleep(2)
            for xooo in range(6):
                if xooo!=5:
                    context.bot.editMessageText(chat_id=channelid, message_id=mes.message_id, text=str(5-xooo))
                    time.sleep(1)
                if xooo==5:
                    context.bot.editMessageText(chat_id=channelid, message_id=mes.message_id, text="Best Of Luck 👍👍👍")
                    time.sleep(1)
                    
                
            cil=client["Quiz"]['Quiz_Polls']
            cil1=client["Quiz"][userText]
            try:
                cil.delete_many({"QuizID":userText})
                cil1.drop()
                print("Quiz_Polls Deleted...")
            except Exception as e:
                print("Quiz_Polls = "+str(e))
            
            y=0
            for X in colldb:
                Zno=coll.count_documents({})-y
                y+=1
                question=str(Zno)+". "+X["que"]
                options=X["op"]
                correct_option_id =X["cor"]
                exp=X["exp"]
                if exp =="":
                    exp=None
                
                try:
                    print("1")
                    message = context.bot.send_poll(
                            chat_id=channelid,
                            question=question,
                            options=options,
                            type=Poll.QUIZ,
                            correct_option_id =correct_option_id,
                            #open_period=int(Time),
                            explanation=exp,
                            is_closed=False,
                            is_anonymous=False,
                            reply_markup=ReplyKeyboardRemove(),    
                        )
                    print("5")
                    Mid.append(message.message_id)
                    time.sleep(5)

                except Exception as e:
                    print("e===="+str(e))
                ZMid[userText]=Mid
                
                try:
                    #print("start")
                    payload = {
                        message.poll.id: {
                            "Que": question,
                            "options": options,
                            "cor":correct_option_id,
                            "exp":exp,
                            "message_id": message.message_id,
                            "chat_id": update.effective_chat.id,
                            "que_no":int(Zno),
                            "quiz_name":userText
                        },"ID":message.poll.id,"QuizID":Textstr0
                    }
                    context.bot_data.update(payload)
                    cil=client["Quiz"]['Quiz_Polls']
                    print("inserting Payload")
                    cil.insert_one(payload)
                    chatid=channelid
                except Exception as e:
                    print("payload not done ="+str(e))
            
                    
            context.bot.send_message(chat_id=channelid, text="<a href=\"https://telegram.me/Soojhboojh_01bot?start\">🌐 Click Sharing ☜ </a>", parse_mode=ParseMode.HTML,disable_web_page_preview = True)

                
    

                
            
            

            
        except Exception as e:
            print("e========"+str(e))
        
            update.message.reply_text("Name not exist.", reply_markup=ReplyKeyboardRemove(),)
        dbn=client["Quiz"]["Quizlist"]
        dbn1=ZMid[userText]
        dbn.delete_many({"Id":userText})
        print("Deleting ...")
        dbn.insert_one({userText:dbn1,"Id":userText,"Channel_Id":channelid})
    #update.message.reply_text("/result")
    try:
        return ConversationHandler.END
    except Exception as e:
        pass
    #print(str(Dbz))
    


Xiii=1
Dbz=[]     
#time.sleep(1)
print("Sleeping for one sec")
#@run_async
def receive_poll_answer(update,context):
    global dbR
    global ree
    global J
    global mess
    global Rmark
    global Wmark
    global mark
    global Xiii
    
    #print("jdjdjdjxj")
    if Xiii==1:
    	due=10
    	chat_id11=711296045
    	context.job_queue.run_once(alarm, due, context=chat_id11, name=str(chat_id11))
    	Xiii+=1
    else:
    	pass
    try:
        answe=update
        answer = update.poll_answer
        print(str(answe))
        usname=answer.user.username
        if usname:
        	pass
        else:
        	usname="None"
        poll_id = answer.poll_id
        print("poll_id="+poll_id)
        ui=str(answer.user.id)
        #print("answer"+str(answer))
        #print("Dbz = "+str(Dbz))
        #print("context="+str(context.bot_data))
        cli=client["Quiz"]['Quiz_Polls']
        yoo=cli.find_one({"ID":poll_id})
        Quizname=yoo[poll_id]["quiz_name"]
        print(Quizname)
        if True:
            print("succ..")
            try:
            	col1=client["Quiz"][Quizname]
            	if col1.find_one({"User_ID":answer.user.id}) is not None:
            		pass
            	else:
            		Lname=answer.user.last_name
            		if Lname is None:
                		Lname=""	
            		dict1={"User_ID":answer.user.id,"Fname":answer.user.first_name+" "+Lname,"✔︎":0,"︎✖":0, "Marks":0,"User_Name":usname}
            		col1.insert_one(dict1)
            		print("---------------------------")
            		print("suss")
            		print("---------------------------")
            	corec = str(yoo[poll_id]["cor"])
            	print(corec)
            	if str(answer.option_ids[0])==corec:
            		x=col1.find_one({"User_ID":answer.user.id})
            		mark=x["Marks"]
            		right=x["✔︎"]
            		print(mark)
            		myquery1 = {"User_ID":answer.user.id}
            		newvalues1 = { "$set": { "Marks":int(mark)+4,"✔︎":str(int(right)+1)} }
            		col1.update_one(myquery1, newvalues1)
            	else:
            		x=col1.find_one({"User_ID":answer.user.id})
            		mark=x["Marks"]
            		wrong=x["︎✖"]
            		print(mark)
            		myquery2 = {"User_ID":answer.user.id}
            		newvalues2 = { "$set": { "Marks":int(mark)-1,"︎✖":str(int(wrong)+1)} }
            		col1.update_one(myquery2, newvalues2)
            	print("--------------updated-------------")
            except Exception as e:
            	print("wrong01 "+str(e))
    except Exception as e:
    	print("wrong02 "+str(e))
                	
                
                
                
                
                
                
            
TIME1=range(1)
@run_async
@restricted
@send_typing_action
def playing(update,context):
    
    global chat0id
    chat0id=update.message.chat.id
    #print(str(update))
    context.bot.send_message(chat_id=chat0id, text="Send me group url.")

    return GHN

@run_async
def time1c(update,context):
    global Time1
    global No
    userText=update.message.text
    Time1=userText
    if reaaa.match(r"^(https|http)://t\.me/.*$",Time1):
        Time1=reaaa.sub("(https|http)://t\.me/", "@", Time1)
    if reaaa.match(r"^-\d{1,}$",Time1):
        Time1=reaaa.sub("-", "-100", Time1)
        Time1=int(Time1)
    col111=client["Schedule"][str(Time1)]
    try:
    	Noo=col111.find_one({"Uid":str(Time1)})
    	No=Noo['No']
    	print('suss======'+No+'======suss')
    except:
    	No="1"

    context.bot.send_message(chat_id=chat0id, text="Send me message.")
    return GHN

@run_async
def ghn(update,context):
    global due1
    userText=update.message.text
    try:
	    global No
	    if reaaa.match(r"^\d{1,}$",userText):
	    	context.bot.delete_message(chat_id=Time1,message_id=int(userText))
	    elif reaaa.match(r"^done$",userText):
	    	due=10
	    	chat_id=update.message.chat.id
	    	context.job_queue.run_once(alarm, due, context=chat_id, name=str(chat_id))
	    elif reaaa.match(r"^!\d{1,}$",userText):
	    	userText=reaaa.sub(r"!","",userText)
	    	due1=int(userText)
	    elif reaaa.match(r"^#\d{1,}$",userText):
	    	userText=reaaa.sub(r"#","",userText)
	    	No=userText
	    else:
	    	userText=reaaa.sub(r"@@","<a href=\"",userText)
	    	userText=reaaa.sub(r"##","\"><b>",userText)
	    	userText=reaaa.sub(r"%%","</b></a>",userText)
	    	context.bot.send_message(chat_id=Time1, text=userText,parse_mode=ParseMode.HTML,disable_web_page_preview = True)
    except Exception as e:
    	context.bot.send_message(chat_id=Time1, text="Error Name = "+str(e))
    return GHN
    
#@run_async
def ghn1(update,context):
    global No
    if reaaa.match(r"^-\d{1,}$",str(Time1)):
        is_anonymous=True
    else:
        is_anonymous=False
    userText=update.message.poll
    que=userText.question
    que=reaaa.sub("^(((\[\d{1,}/\d{1,}\] ){1,}|)(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|)(\d{1,}\. |\d{1,}\.|))","",que)
    que=No+".  "+que
    
    print(que)
    options=[o.text for o in userText.options]
    co=userText.correct_option_id
    explan=userText.explanation
    try:
    	col=client["Schedule"][str(Time1)]
    	c={"chat_id":Time1,"question":que,"options":options,"correct_option_id":co,"explanation":explan}
    	col.insert_one(c)
    	if No == '1':
    		col.insert_one({"Uid":str(Time1),'No':'1'})
    	No=str(int(No)+1)
    	col=client["Schedule"][str(Time1)]
    	print("yoyoyk")
    	myquery1 = {"Uid":str(Time1)}
    	print("yoyoyk")
    	newvalues1 = { "$set": { "No":No} }
    	print("yoyoyk")
    	col.update_one(myquery1, newvalues1)
    	print("yoyoyk")

    	
    	
    	
    	'''context.bot.send_poll(
    		chat_id=Time1,
    		question=que,
    		options=options,
            type=Poll.QUIZ,
            correct_option_id=co,
            explanation=explan,
            is_anonymous=is_anonymous,
            allows_multiple_answers=False,
            parse_mode=ParseMode.HTML #,disable_web_page_preview = True
        )'''
    	context.bot.send_message(chat_id=update.message.user.id, text="Que No. = "+No)
    	#time.sleep(5)
    except Exception as e:
    	print(str(e))
    return GHN

due1=18000
def alarm(context: CallbackContext):
    
    job = context.job
    due=due1
    try:
    	col=client["Schedule"]
    	#yy=col.list_collection_names({})
    	for yyy in range(10):
    		yy=col.list_collection_names({})
    		for y in yy:
	    		coly=col[y]
	    		cou=coly.count_documents({})
	    		z=coly.find_one_and_delete({})
	    		if cou==1:
	    			coly.drop()
	    		chat_id=z["chat_id"]
	    		if reaaa.match(r"^-\d{1,}$",str(chat_id)):
	    			is_anonymous=True
	    		else:
	    			is_anonymous=False
	    		que=z["question"]
	    		options=z["options"]
	    		co=z["correct_option_id"]
	    		explan=z["explanation"]
		    	context.bot.send_poll(
		    		chat_id=chat_id,
		    		question=que,
		    		options=options,
		            type=Poll.QUIZ,
		            correct_option_id=co,
		            explanation=explan,
		            is_anonymous=is_anonymous,
		            allows_multiple_answers=False,
		            parse_mode=ParseMode.HTML #,disable_web_page_preview = True
	    		)
	    	time.sleep(5)
    	context.job_queue.run_once(alarm, due, context=chat_id, name=str(chat_id))
    	#time.sleep(5)
    except Exception as e:
    	context.job_queue.run_once(alarm, due, context=chat_id, name=str(chat_id))
    	print(str(e))
    
    
    
    
    
    
    
    



@restrictedD
@run_async
@send_typing_action
def poll(update, context):
    """Sends a predefined poll"""
    #que = update.message.text()
    quest=(update.message.text)
    try:
        q=quest[0:-1]
        q=reaaa.sub("Poll to Text Bot\:\n|Soojh Boojh Bot - 02\:\n|NaN| Q.*\.|^\. |^\.", "", q)
        q=reaaa.sub(r"(\(|\[|)(A|B|C|D|a|b|c|d|अ|ब|बी|स|सी|डी|ड|क|ख|ग|घ|य|र|ल|व)(\)|\]|\.)(\.| |)", "\n", q)
        q=reaaa.sub("\n{2,}", "\n", q)
        q=reaaa.sub("☞", "", q)
        q=reaaa.split(r"[\n]", q)
        #update.message.reply_text(q)
        ques=q[0]
        ques=reaaa.sub(r"^(Q_|Q|)(\d{1,})(\.)(\ |){1,}", "", ques)
        que="☞ "+ ques
        #que=que+"\n\n  ■_𝗜𝗺𝗽𝗼𝗿𝘁𝗮𝗻𝘁_𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻_■"
        option1="(A) "+q[1]
        option2="(B) "+q[2]
        option3="(C) "+q[3]
        option4="(D) "+q[4]
        options=[option1, option2, option3, option4]
        corr=quest[-1]
        result = reaaa.match(r"[-+]?\d+$", corr)
        options5=q[5::1]
        options5="\n".join(options5)
        options5=reaaa.sub(r"@\w*", "", options5)
        if options5 == "":
            options5=""#options5="👇👇👇 Ask your Doubts here 👇👇👇\n👇👇👇        Only for Math        👇👇👇\nhttps://soojhboojh.xyz/ask-question/"
        else:
            options5=options5
            print(options5)
        #options5=re.sub(r"\@\w.*", "", options5)
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
            is_anonymous=False,
            allows_multiple_answers=False,
        )
        # Save some info about the poll the bot_data for later use in receive_poll_answer
    except Exception as e:
        print(str(e))
COPY, POLLS=range(2)




@restricted
@send_typing_action
def copyc(update,context):
    global chat1id
    print(str(update))
    chat1id=int(update.message.chat.id)
    if chat1id<=0:
    	try:
    		chat1id="@"+str(update.message.chat.username)#id
    	except Exception as e:
    		print(str(e))
    		
    else:
    	pass
    context.bot.send_message(chat_id=chat1id, text="Right Option only digit")

    return COPY



@run_async
def copy(update,context):
    global Time2
    global Tco
    userText=update.message.text
    Time2=userText
    #Time2=reaaa.split("", Time2)
    Tco=0
    context.bot.send_message(chat_id=chat1id, text="Send me polls.")
    return COPY

@send_typing_action
@restricted
def polls(update: Update, _: CallbackContext) -> int:
    #update.message.reply_text("yoo")
    global Tco
    try:
	    actual_poll = update.message.poll
	    print(str(actual_poll))
	    question= actual_poll.question
	    options=[o.text for o in actual_poll.options]
	    corr=str(int(Time2[Tco])-1)
	    Tco+=1
	    update.effective_message.reply_poll(
	            question= question,
	            options=options,
	            # with is_closed true, the poll/quiz is immediately closed
	            type=Poll.QUIZ,
	            correct_option_id =corr,
	            #explanation=exp,
	            is_closed=True,
	            is_anonymous=True,
	            reply_markup=ReplyKeyboardRemove()
	    )
	    #update.message.reply_text("send me more polls or /cancel")
    except Exception as e:
    	update.effective_message.reply_text('program finish /cancel \nError name = '+str(e))
    return COPY

POLLF,POLLN=range(2)
@run_async
@restricted2
@send_typing_action
def pollf(update,context):
    global chat___id
    global mesho01
    chat___id=int(update.message.chat.id)
    Ccc=update.message.from_user.id
    if chat___id<=0:
    	try:
    		
    		chat___id="@"+str(update.message.chat.username)#id
    		mesho01=context.bot.send_message(chat_id=chat___id, text="<a href=\"https://t.me/Soojhboojh_01bot?start\">🌐 find Quiz Name Here☜</a>\nSend me Quiz name that you want to play",parse_mode=ParseMode.HTML,disable_web_page_preview = True)
    		context.bot.send_message(chat_id=711296045, text="<a href=\"tg://openmessage?user_id="+str(Ccc)+"\"><b>user tring to share</b></a> = "+chat___id,parse_mode=ParseMode.HTML,disable_web_page_preview = True)

    	except Exception as e:
    		print(str(e))
    	return POLLF
    else:
	    db=client["Quiz_Data"]
	    x=(db.list_collection_names({}))
	    
	    for y in x:
	    	context.bot.send_message(chat_id=chat___id,text="<pre>"+y+"</pre>", parse_mode=ParseMode.HTML,disable_web_page_preview = True)
	    	
	    context.bot.send_message(chat_id=chat___id,text="copy one fo them 👆👆👆👆👆👆👆\n<a href=\"https://telegram.me/Soojhboojh_01bot?startgroup=true\">Click Here for Play Quiz in your group</a>", parse_mode=ParseMode.HTML,disable_web_page_preview = True)
    
    return ConversationHandler.END
    
@restricted2
def pollfname(update,context):
    global Time4
    Time4=update.message.text
    try:
    	context.bot.delete_message(chat_id=chat___id,message_id=mesho01.message_id)
    except:
    	pass
    col=client["Quiz"]["Quizlist"]
    x=col.find_one({"Id":Time4})
    context.bot.send_message(chat_id=711296045, text="Group_url = "+chat___id+"\n\n<a href=\"tg://openmessage?user_id="+str(update.message.chat.id)+"\"><b>Sender Quiz Name</b></a> = "+str(Time4), parse_mode=ParseMode.HTML)
    try:
    	coll=client["Quiz_Data"][Time4]
    	colldb=coll.find()
    	messa=context.bot.send_message(chat_id=chat___id, text="🎲 Get ready for the LIVE TEST \'"+Time4+"\'\n\n🖊 "+str(coll.count_documents({}))+" questions\n\n⏱ Voting Start "+str(time.ctime(time.time() +19800))+" \n\n📰 Votes are visible to group members and shared all polls \nevery ✔︎ Question gain ✙4 Marks\nevery ✖︎ Question gain –1 Mark\n\n<b>Playing Group "+str(chat___id)+"\n\nFor more #Soojh_Boojh</b>", parse_mode=ParseMode.HTML,disable_web_page_preview = True)
    	channel_ids=x["Channel_Id"]
    	colme=client["Quiz"]["Message"]
    	coldoc={"MessID":messa.message_id,"ID":chat___id+"_"+Time4}
    	print(coldoc)
    	try:
    		colme.delete_many({"ID":chat___id+"_"+Time4})
    		print("delete successful")
    	except Exception as e:
    		print("First time play or not play. "+str(e))
    	colme.insert_one(coldoc)
    	print("insert successful")
    	
    	try:
    		for y in x[Time4]:
	    		context.bot.forward_message(chat_id=chat___id,from_chat_id=channel_ids, message_id=y)
	    		'''if %4==2:
	    			time.sleep(5)'''
	    	context.bot.send_message(chat_id=chat___id, text="<a href=\"https://telegram.me/Soojhboojh_01bot?start\">🌐 Click Sharing ☜ </a>", parse_mode=ParseMode.HTML,disable_web_page_preview = True)
    	except:
    		context.bot.send_message(chat_id=chat___id, text="Give me Polls send permission to upload quiz here...", parse_mode=ParseMode.HTML)
    except Exception as e:
    	print(str(e))
    return ConversationHandler.END



def main() -> None:
    # Create the Updater and pass it your bot's token.
    bot_token=os.environ.get("BOT_TOKEN", "")
    #bot_token='1458427559:AAFDcDNOg6VfK6Gscrf7hhS6eciKr2Q_nT0'
    updater = Updater(bot_token,use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
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
            GHN: [MessageHandler(Filters.text & ~Filters.command & ~Filters.regex(r'^((https|http).*|@.*)$') & ~Filters.regex(r'^-\d{1,}$'), ghn), MessageHandler(Filters.regex(r'^(((https|http).*|@.*))|(-\d{1,})$'), time1c),MessageHandler(Filters.poll,  ghn1)],
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

    dispatcher.add_handler(conv_handler01R)
    dispatcher.add_handler(PollAnswerHandler(receive_poll_answer))
    
    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(conv_handler01F)
    dispatcher.add_handler(conv_handler01)
    dispatcher.add_handler(conv_handler0C)
    dispatcher.add_handler(conv_handler1C)
    dispatcher.add_handler(conv_handler02)
    dispatcher.add_handler(conv_handler012)
    dispatcher.add_handler(conv_handler0u)
    dispatcher.add_handler(CommandHandler('quizlist', quizlist))
    dp=updater.dispatcher
    dp.add_handler(CommandHandler('downloadfile',downloadfile))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, poll))
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
#
