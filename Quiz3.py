from pymongo import MongoClient
import dns

'''import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] # this is a google public dns server,  use whatever dns server you like here
# as a test, dns.resolver.query('www.google.com') should return an answer, not an exception'''
client=MongoClient('mongodb+srv://Kinshu04101:Qwert123@cluster0.ckcyx.mongodb.net/test?retryWrites=true&w=majority')

#!/usr/bin/env pyth#
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
# import xlsxwriter
import sqlite3
from telegram.ext.dispatcher import run_async

from telegram import ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup, ReplyKeyboardRemove, Update, Poll, Update, ChatAction, ParseMode
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    PollAnswerHandler,
    PollHandler,
    ConversationHandler,
    CallbackContext,
    CommandHandler, 
    CallbackQueryHandler, 
    CallbackContext
    
)


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

GENDER, PHOTO, LOCATION, BIO, QUIZ, DELETE, RESULT, TIME, Re = range(9)


import asyncio
from create_results import save_results, save_photos


def send_typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)
        return func(update, context,  *args, **kwargs)

    return command_func

LIST_OF_ADMINS_CQ = ["711296045"]

def restrictedCQ(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        
        userName = str(update.message.chat.id)
        userName1=str(update.message.from_user.id)
        if userName and userName1 not in LIST_OF_ADMINS_CQ:
            #update.message.reply_text(f"Unauthorized access denied for {update.effective_user.mention_html()}.", parse_mode=ParseMode.HTML)
            return
        return func(update, context, *args, **kwargs)
    return wrapped


LIST_OF_ADMINS = ["711296045","1001183009","776365745","1527108544","2020953330","1202919365","1309577346","875026044","5094761615","786181993","1341437687","1353892576","5028705992","781968811","2111134423","1952288751","5259697190","1211101855"]

def restricted(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        
        #userName = str(update.message.chat.id)
        userName1=str(update.message.from_user.id)
        if userName1 not in LIST_OF_ADMINS:
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
            #xid.append(update.message.chat.id)
            for x in y:
                print(x['user']['id'])
                xid.append(x['user']['id'])
        except:
            pass
        if chatiid<=0:
            try:
                try:
                        pass#context.bot.delete_message(chat_id=str(chatiid),message_id=mid)
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


LIST_OF_ADMINS = ["711296045","1001183009","776365745","2020953330","875026044","1468125551","1527108544","1202919365","1086189598","1309577346","5094761615","555919730","786181993","1341437687","1353892576","5028705992","781968811","2111134423","1952288751","5259697190"]

def restrictedD(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        global Xiii
        if Xiii==1:
            due=7201
            chat_id11=711296045
            context.job_queue.run_once(alarm, due, context=chat_id11, name=str(chat_id11))
        userName = str(update.message.chat.id)
        userName1=str(update.message.from_user.id)
        if userName1 not in LIST_OF_ADMINS:
            #update.message.reply_text(f"Unauthorized access denied for {update.effective_user.mention_html()}.", parse_mode=ParseMode.HTML)
            return
        
        return func(update, context, *args, **kwargs)
    return wrapped



@restrictedCQ
@run_async
@send_typing_action
def createquiz(update: Update, _: CallbackContext) -> int:
    

    update.message.reply_text(
        "Hello Quizers \n\n Send me a name of your quiz..."
    )

    return GENDER

Textstr=""
#@run_async
def gender(update,context):
    user = update.message.from_user
    logger.info("Gender of %s: %s", user.first_name, update.message.text)
    global Textstr
    userText=update.message.text
    asyncio.run(save_results(userText,update,context))
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
    que=reaaa.sub(" "," ",question)
    que=reaaa.sub("(by|golu).*?(✍️){1,}"," ",que)
    que=reaaa.sub("(\n| |)✍{0,} Priti Gupta ✍{0,}(\n| |)","",que)
    que=reaaa.sub("(\n| |)Sandeep Choudhary(\n| |)","",que)
    que=reaaa.sub("(\n| |)🤗.*?🤗(\n| |)","",que)
    que=reaaa.sub("(\n){1,}","\n",que)
    que=reaaa.sub("^\n","",que) 
    question= reaaa.sub(r"(@\w*)|(http(s|)://[a-zA-Z0-9_/\.])", "", que)
    question= reaaa.sub(r"^(\[\d{1,}/\d{1,}\] ){1,}", "", question)
    options=[o.text for o in user.options]
    correct_option_id=user.correct_option_id
    exp=user.explanation
    
    if exp:
        if reaaa.findall("@[a-zA-Z0-9_-]",exp):
        	exp=reaaa.sub(" "," ",exp) 
        	exp=None
        elif reaaa.findall("http(s|)://",exp):
        	exp=reaaa.sub(" "," ",exp) 
        	exp=None
    if exp is not None:
        exp= reaaa.sub(r"(#\w*)|(http(s|)://[a-zA-Z0-9_/])", "", exp)
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
    new={'que':user_location, 'op':False, 'cor':False, 'exp':False, 'ID':Textstr, 'User_ID':update.message.chat.id}
    col=client["Quiz_Data"][Textstr]
    col.insert_one(new)
    '''logger.info(
        "Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude
 )'''
    return PHOTO
    #return BIO


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
        asyncio.run(save_results(userTex,update,context))
        asyncio.run(save_photos(userTex,update,context))
        context.bot.delete_message(chat_id=chat__id,message_id=meid)
    except Exception as e:
        print("connection fail "+str(e))
    mydoc = col.find().sort("Marks", -1)
    try:
        colme=client["Quiz"]["Message"]
        coldoc={"ID":str(chat__id)+"_"+userTex1}
        print("ID==="+str(chat__id)+"_"+userTex1)
        Colm=colme.find_one(coldoc)
        colmessage=Colm["MessID"]
        print(colmessage)
    except Exception as e:
        print("colmessage=="+str(e))

    # try:
    #     if True:
    #         if True:
    #             try:
    #                 if True:
    #                     if True:
    #                         try:
    #                             os.remove('Result.xlsx')
    #                         except:
    #                             print("removing Result.xlsx File")
    #                         workbook = xlsxwriter.Workbook('Result.xlsx')
    #                         worksheet = workbook.add_worksheet()
    #                         cell_format = workbook.add_format()
    #                         cell_format1 = workbook.add_format()
    #                         cell_format10 = workbook.add_format()
    #                         cell_format.set_align('center')
    #                         cell_format1.set_align('center')
    #                         cell_format1.set_font_color('green')
    #                         cell_format1.set_bold()
    #                         worksheet.set_column('A:A', 5)
    #                         worksheet.set_column('C:E', 9)
    #                         worksheet.set_column('B:B', 37)
    #                         worksheet.set_column('F:F', 17)
    #                         worksheet.write('A1', 'Rank', cell_format1)
    #                         worksheet.write('B1', 'Name', cell_format1)
    #                         worksheet.write('C1', '︎✔︎ Options', cell_format1)
    #                         worksheet.write('D1', '︎✖ Options', cell_format1)
    #                         worksheet.write('E1', 'Marks', cell_format1)
    #                         worksheet.write('F1', 'User Name', cell_format1)
    #                         cell_format10.set_align('center')
    #                         cell_format10.set_num_format('[Green]General;[Red]-General;General')
    #                         COUNTR=""
    #                         for x in mydoc:
    #                             Fname=x["Fname"]
    #                             Rname=x["✔︎"]
    #                             Wname=x["︎✖"]
    #                             Uname=x["User_Name"]
    #                             Usid=x["User_ID"]
    #                             Rs=x["Marks"]
    #                             #print("data loading start")
    #                             if Uname !="None":
    #                                 if COUNTJ<=9:
    #                                     COUNTR=COUNTR+""+str(COUNTJ+1)+". <b>@"+str(Uname)+"</b> 🎰 "+str(Rs)+"\n"
    #                                     COUNTJ+=1
    #                             else:
    #                                 if COUNTJ<=9:
    #                                     COUNTR=COUNTR+""+str(COUNTJ+1)+". <a href=\"tg://openmessage?user_id="+str(Usid)+"\"><b>"+Fname+"</b></a> 🎰 "+str(Rs)+"\n"
    #                                     COUNTJ+=1
                                
                                
                                
    #                             worksheet.write('A'+str(rnumb+1), str(rnumb), cell_format)
    #                             if False:
    #                                 worksheet.write_url('B'+str(rnumb+1), "tg://openmessage?user_id="+str(Usid), cell_format=cell_format, string=str(Fname))
    #                             else:
    #                                 worksheet.write_url('B'+str(rnumb+1), "tg://openmessage?user_id="+str(Usid), cell_format=cell_format, string=str(Fname))
    #                             worksheet.write('C'+str(rnumb+1), str(Rname), cell_format)
    #                             worksheet.write('D'+str(rnumb+1), str(Wname), cell_format)
    #                             worksheet.write('E'+str(rnumb+1), int(Rs), cell_format10)
    #                             if Uname is None:
    #                                 worksheet.write('F'+str(rnumb+1), 'None', cell_format)
    #                             else:
    #                                 worksheet.write('F'+str(rnumb+1), "@"+str(Uname), cell_format)
    #                                 Uname=None
    #                             #print(COUNTR)
    #                             rnumb+=1
    #                         workbook.close()
    #                         print("webhook close")
                            
                                    
                            
    #             except Exception as e:
    #                 print("e===="+str(e))
    #                 context.bot.send_document(chat_id=chat__id, text="quiz not found")
    #     caption1="🏁 The quiz \'<pre>"+userTex+"</pre>\' has finished!\nQuiz Attempt 👉🏻 "+str(col.count_documents({"User_ID":{ "$type" : "int" }}))+" Persons.\nCurrent Time = "+str(time.ctime(time.time() +19800))+" \n"+str(colldb)+" questions answered\n\n"+COUNTR+"\n🏆 Congratulations to the winners!\n\nTag Message में full Quiz है🙏"
    #     #print(caption1)
    #     try:
    #         context.bot.send_document(chat__id, open('Result.xlsx', "rb"),caption=caption1, parse_mode=ParseMode.HTML,reply_to_message_id=colmessage)
    #         print(colmessage)
    #     except Exception as e:
    #         print(str(e))
    #         context.bot.send_document(chat__id, open('Result.xlsx', "rb"),caption=caption1, parse_mode=ParseMode.HTML)
    # except Exception as e:
    #     context.bot.send_message(chat_id=chat__id, text="no live quiz at now come next time.\n error name = "+str(e))
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

@run_async
def doc_poll(update,context):
    if update.message.from_user.id==711296045:
        #print(update)
        filename="yo.txt"
        file_id = update.message.document.file_id
        newFile = context.bot.get_file(file_id)
        qwer=newFile.download(filename)
        with open(qwer,"r") as poll_file:
            dbq = poll_file.read()
        link=update.message.caption
        q=reaaa.split("\n\n",dbq)
        X=0
        
        keyboard=None
        reply_markup=None
        Xy=client["youtube"]["time"]
        Time=Xy.find_one({})["Time"]
        yoo=0
        for x in q:
        	if link is not None:
        	    keyboard=[[InlineKeyboardButton("Explanation", url=link+"?t="+str(int(yoo)))]]
        	    reply_markup=InlineKeyboardMarkup(keyboard)
        	x=reaaa.split("(?=Sol\.\(.\))",x)
        	yoo=yoo+Time[X]
        	X+=1
        	ex=x[1]
        	t=reaaa.split("(?=\(a\)|\(b\)|\(c\)|\(d\))",x[0])
        	if ex[5]=="a":
        	    correct_option_id=0
        	elif ex[5]=="b":
        	    correct_option_id=1
        	elif ex[5]=="c":
        	    correct_option_id=2
        	elif ex[5]=="d":
        	    correct_option_id=3
        	
        
        	try:
        	  try:
        	    context.bot.send_poll(
        	chat_id=update.effective_chat.id,
                                question=t[0],
                                options=t[1:],
                                type=Poll.QUIZ,
                                correct_option_id =correct_option_id,
                                #open_period=int(Time),
                                explanation="Subscribe On youtube : https://youtube.com/channel/UCDnlmiR6XtdjRe7kolFQHLA\n\n👆👆👆",
                                is_closed=False,
                                is_anonymous=True,
                                reply_markup=reply_markup,
                                parse_mode=ParseMode.HTML
                            )
        
        	  except:
        	    context.bot.send_poll(
        	chat_id=update.effective_chat.id,
                                question=t[0],
                                options=t[1:],
                                type=Poll.QUIZ,
                                correct_option_id =correct_option_id,
                                #open_period=int(Time),
                                #explanation=exp,
                                is_closed=False,
                                is_anonymous=False,
                                reply_markup=reply_markup,
                            )
        
        	except:
        	  context.bot.send_message(update.effective_chat.id, text="\n".join(t[:]),reply_markup=reply_markup)
        	time.sleep(5)
    	
    	
    	
        
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
    context.bot.send_message(chat_id=chatid, text="Send me group username Which you want to play quiz")
    #return CHN
    return QUIZ
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
    channelid="@ONLY_FOR_US"
    Mid = []
    J=0

    userText=update.message.text

    Textstr0=userText

    coll=client["Quiz_Data"][userText]
    colldb=coll.find()
    if True: 
        try:
            
            messa=context.bot.send_message(chat_id=channelid, text="🎲 Get ready for the LIVE TEST \'<pre>"+userText+"</pre>\'\n\n🖊 "+str(coll.count_documents({}))+" questions\n\n📰 Votes are visible to group members and shared all polls \nevery ✔︎ Question gain ✙4 Marks\nevery ✖︎ Question gain –1 Mark\n\n<b>Result Comes on "+str(time.ctime(time.time() + int(Time)+19800))+"\n\nPlaying Group "+str(channelid)+"\n\nFor more #Soojh_Boojh</b>",parse_mode=ParseMode.HTML)
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
                Zno=coll.count_documents({"cor":{"$type":"int"}})-y
                
                question=reaaa.sub("Q\d{1,}(\.|)","",X["que"])
                options=X["op"]
                correct_option_id =X["cor"]
               
                exp=X["exp"]
                if exp =="":
                    exp=None
                
                try:
                    print("1")
                    if True:
                    

                        message = context.bot.send_poll(
                            chat_id=channelid,
                            question=str(Zno)+". "+question,
                            options=options,
                            type=Poll.QUIZ,
                            correct_option_id =correct_option_id,
                            #open_period=int(Time),
                            explanation=exp,
                            is_closed=False,
                            is_anonymous=False,
                            reply_markup=ReplyKeyboardRemove(),    
                        )
                        y+=1
                    print("5")
                    Mid.append(message.message_id)
                    time.sleep(5)

                except Exception as e:
                    message = context.bot.send_message(chat_id=channelid, text=question)
                    print("5")
                    Mid.append(message.message_id)
                    time.sleep(5)
                    
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
            
            unique_url=asyncio.run(save_results(userText,update,context))
            print("https://telegram.me/Soojhboojh_01bot?startgroup=Share"+unique_url[23:])
            keyboard = [
                [
                    InlineKeyboardButton("Play Quiz", callback_data='3',url="https://telegram.me/Soojhboojh_01bot?start=Play"+unique_url[23:]),
                    InlineKeyboardButton("Result", callback_data='2',url=unique_url),],[
        #],[
        InlineKeyboardButton("Play in Group", callback_data='1',url="https://telegram.me/Soojhboojh_01bot?startgroup=Share"+unique_url[23:]),
                ],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            context.bot.send_message(chat_id=channelid,text='<b>'+userText+'</b>', reply_markup=reply_markup, parse_mode=ParseMode.HTML)
            context.bot.send_message(chat_id="@SOOJH_BOOJH_BOT_discussion_grouo",text='<b>'+userText+'</b>', reply_markup=reply_markup, parse_mode=ParseMode.HTML)
            
            
            
            
            
            #context.bot.send_message(chat_id=channelid, text="<a href=\"https://telegram.me/Soojhboojh_01bot?start\">🌐 Click Sharing ☜ </a>", parse_mode=ParseMode.HTML ,disable_web_page_preview = True)

                


                
            
            

            
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

from create_results import save_user_photo

def receive_poll_answer(update:Update,context:CallbackContext):
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
        due=7201
        chat_id11=711296045
        context.job_queue.run_once(alarm, due, context=chat_id11, name=str(chat_id11))
        Xiii+=1
    else:
        pass
    try:
        answer = update.poll_answer
        username=answer.user.username
        user_id=answer.user.id
        poll_id = answer.poll_id
        print("poll_id="+poll_id)

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
                quizresults = client.Results.quizresults
                if quizresults.find_one({"quizname":Quizname,"userid":user_id}) is None:
                    # runs when user is not present in the database
                    try:
                        asyncio.run(save_user_photo(user_id,context))
                    except Exception:
                        pass

                    if answer.user.last_name:
                        last_name = f" {answer.user.last_name}"
                    else:
                        last_name = ""
                    
                    quizresults.insert_one({
                        "quizname":Quizname,
                        "userid":user_id,
                        "name" : answer.user.first_name + last_name,
                        "username":username,
                        "correct":0,
                        "incorrect":0,
                        "marks":0,
                    })

                
                corec = str(yoo[poll_id]["cor"])
                if str(answer.option_ids[0])==corec:
                    # if answer is correct increase marks by 4 and increase the correct count
                    quizresults.update_one({"quizname":Quizname,"userid":user_id},{'$inc':{"correct":1,"marks":4}})

                else:
                    # if answer is incorrect decrease marks by 1 and increase the incorrect count
                    quizresults.update_one({"quizname":Quizname,"userid":user_id},{'$inc':{"incorrect":1,"marks":-1}})

            except Exception as e:
                print("wrong01 "+str(e))
    except Exception as e:
        print("wrong02 "+str(e))
                	
                
                
                
                
                
                
            
TIME1, GHN2=range(2)
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
    context.bot.send_message(chat_id=chat0id, text="Send me message.")
    return GHN

@run_async
def ghn(update,context):
    global due1
    global admin2
    userText=update.message.text
    try:
        global No
        global x
        if reaaa.match(r"^\d{1,}$",userText):
            context.bot.delete_message(chat_id=Time1,message_id=int(userText))
        elif reaaa.match(r"^Done$",userText):
            due=10
            chat_id=update.message.chat.id
            context.job_queue.run_once(alarm, due, context=chat_id, name=str(chat_id))
        elif reaaa.match(r"^!\d{1,}$",userText):
            userText=reaaa.sub(r"!","",userText)
            due1=int(userText)
        elif reaaa.match(r"^#\d{1,}$",userText):
            userText=reaaa.sub(r"#","",userText)
            No=userText
        elif reaaa.match(r"^Add .*$",userText):
            userText=reaaa.sub("^Add ","",userText)
            userText=reaaa.split(r"[ ]", userText)
            admin2=[]
            for X in range(len(userText)):
                admin2.append("-100"+userText[X])
                x=0
            return GHN2
            
        else:
            userText=reaaa.sub(r"@@","<a href=\"",userText)
            userText=reaaa.sub(r"##","\"><b>",userText)
            userText=reaaa.sub(r"%%","</b></a>",userText)
            context.bot.send_message(chat_id=Time1, text=userText,parse_mode=ParseMode.HTML,disable_web_page_preview = True)
    except Exception as e:
        context.bot.send_message(chat_id=Time1, text="Error Name = "+str(e))
    return GHN

ali=[-1001443924980,-1001271547569,-1001517843177,-1001478660095,-1001173492501,-1001177789955,-1001342905358,-1001725784523,-1001664461759,-1001412214082,-1001412214082,-1001244305820,-1001393712887,-1001612419726,-1001569069801,-1001169740180,-1001702776152,-1001195321663]
ali2=[-1001443924980,-1001271547569,-1001517843177,-1001478660095,-1001173492501,-1001177789955,-1001342905358,-1001725784523,-1001664461759,-1001412214082,-1001412214082,-1001244305820,-1001393712887,-1001612419726,-1001569069801,-1001169740180,-1001702776152,-1001195321663]
#
print(str(ali))
[ali.append(x["Uid"]) for x in client["user"]["sub"].find({})]
zzz=[]
for x in ali:
	if x not in zzz:
		zzz.append(x)
ali=zzz
zzz=None
Man=[711296045,1001183009,776365745,1527108544,2020953330,1202919365,1309577346,875026044,5094761615,786181993,1341437687,1353892576,5028705992,781968811,2111134423,1952288751,5259697190]
Group=[-1001517843177,-1001183315065,-1001293483771,-1001362563196,-1001307100573,-1001187254179,-1001368097755,-1001222891254,-1001164423875,-1001487436278,-1001428838285,-1001664461759,-1001664461759,-1001415742406,-1001725784523,-1001718523021,-1001459269318]
@run_async
@restricted
def ghppp10(update,context):
    if update.message.chat.id==-1001682640576:
    	print(update)
    	if update.message.from_user.id==711296045:
    	    if hasattr(update.message,'text'):
    	        newv=-1
    	        print(str(update.message))
    	        if update.message.text.startswith("https://t.me/ONLY_FOR_US/"):
	                nn=int(reaaa.sub("https://t.me/ONLY_FOR_US/\d{,}/","",update.message.text))
	                print(nn)
	                uid=reaaa.sub("https://t.me/","@",update.message.text)
	                uid=reaaa.sub("/\d{1,}/\d{,}","",uid)
	                text=reaaa.sub("https://t.me/ONLY_FOR_US/","",update.message.text)
	                text=int(reaaa.sub("/\d{,}","",text))
	                for x in ali:
	                    for z in range(nn):
	                        newv+=1
	                        try:
	                            context.bot.forward_message(chat_id=x,from_chat_id=uid,message_id=int(text)+z)
	                            #if x in ali2:
	                                #time.sleep(5)
	                            #else:
	                                #time.sleep(1)
	                        except Exception as e:
	                            if reaaa.findall("Flood control exceeded. Retry in ",str(e)):
	                                te=reaaa.sub("Flood control exceeded. Retry in ","",str(e))
	                                te=reaaa.sub(" seconds","",str(te))
	                                context.bot.send_message(chat_id=update.message.chat_id, text="sleeping for "+str(te)+"\ntotal send message = "+str(newv))
	                                time.sleep(int(te)+1)
	                                context.bot.send_message(chat_id=update.message.chat_id, text="Bot now activate")
	                                context.bot.forward_message(chat_id=x,from_chat_id=update.message.chat_id,message_id=update.message.message_id)
	            
    	        else:
    	            for x in ali:
    	                try:
    	                    context.bot.forward_message(chat_id=x,from_chat_id=update.message.chat_id,message_id=update.message.message_id)
    	                    time.sleep(5)
    	                except Exception as e:
    		
    	                    print(str(x)+str(e))
    	                    if reaaa.findall("Flood control exceeded. Retry in ",str(e)):
    	                        te=reaaa.sub("Flood control exceeded. Retry in ","",str(e))
    	                        te=reaaa.sub(" seconds","",str(te))
    	                        context.bot.send_message(chat_id=update.message.chat_id, text="sleeping for "+str(te))
    	                        time.sleep(int(te)+1)
    	                        context.bot.forward_message(chat_id=x,from_chat_id=update.message.chat_id,message_id=update.message.message_id)
    	                    else:
    	                        client["user"]["sub"].find_one_and_delete({"Uid":x})
    		
    	        time.sleep(5)
    	        context.bot.send_message(chat_id=update.message.chat_id, text="Next Total subscriber "+str(len(ali)))
    	ali1={555919730:[-1001173492501],875026044:[-1001222891254,-1001164423875,-1001593542899]}
    	if update.message.from_user.id in ali1.keys():
	        
	        for x in ali1[update.message.from_user.id]:
	            try:
	                context.bot.forward_message(chat_id=x,from_chat_id=update.message.chat_id,message_id=update.message.message_id)
	            except Exception as e:
		
	                print(str(x)+str(e))
	                if reaaa.findall("Flood control exceeded. Retry in ",str(e)):
	                    te=reaaa.sub("Flood control exceeded. Retry in ","",str(e))
	                    te=reaaa.sub(" seconds","",str(te))
	                    context.bot.send_message(chat_id=update.message.chat_id, text="sleeping for "+str(te))
	                    time.sleep(int(te)+1)
	                    context.bot.forward_message(chat_id=x,from_chat_id=update.message.chat_id,message_id=update.message.message_id)
	                else:
	                    pass
		
	        time.sleep(5)
	        context.bot.send_message(chat_id=update.message.chat_id, text="Next")
	
@restricted
def ghppp1(update,context):
    if True:
        cid=""
        id=""
        for li1 in range(len(Man)):
            if str(update.message.chat.id) in str(Man[li1]):
                cid=Group[li1]
                id=Man[li1]
        userText=update.message.poll
        context.bot.send_message(chat_id=-1001539629311, text="<a href=\"tg://openmessage?user_id="+str(cid)+"\">chat info</a>\n<a href=\"tg://openmessage?user_id="+str(id)+"\">grouo</a>",parse_mode=ParseMode.HTML,disable_web_page_preview = True)
        print("ghn1 started")
        que=userText.question
        que=reaaa.sub(" "," ",que)
        que=reaaa.sub("^(☞( ){1,}|(((\[\d{1,}/\d{1,}\] ){1,}|)(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|)))","",que)
        que=reaaa.sub("(\n| |)✍{0,} Priti Gupta ✍{0,}(\n| |)","",que)
        que=reaaa.sub("(\n| |)Sandeep Choudhary(\n| |)","",que)
        que=reaaa.sub("(\n| |)🤗.*?🤗(\n| |)","",que)
        que=reaaa.sub("(\n){1,}","\n",que)
        que=reaaa.sub("^\n","",que)
        que= reaaa.sub("([^\u0041-\u005a\u0061-\u007a\u0040\u0020\u0900-\u097F\u0030-\u0039\u002c])","", reaaa.sub(r"(@\w*)|(http(s|)://[a-zA-Z0-9_/\.])", "", que))
        options=[o.text for o in userText.options]
        for yx in range(len(options)):
            options[yx]=reaaa.sub(" "," ",options[yx])
        co=userText.correct_option_id
        explan=userText.explanation
        
    
        if explan:
            explan=reaaa.sub(" "," ",explan)
            if reaaa.findall("@[a-zA-Z0-9_-]",explan):
                explan=None
            elif reaaa.findall("t\.me",explan):
                explan=None
            elif reaaa.findall("^\d{8,}$",explan):
                explan=None
         
        if update.message.chat.id==786181993:
        	if explan is None:
        	    explan="@Study_Quiz_India\n@Maths_Quiz_Notes\n@Current_Affairs_Quiz_Notes"
        	else:
        	    explan=explan+"\n\n@Study_Quiz_India"
        
        context.bot.send_poll(
                chat_id=int(cid),
                question=que,
                options=options,
                type=Poll.QUIZ,
                correct_option_id=co,
                explanation=explan,
                is_anonymous=True,
                allows_multiple_answers=False,
                parse_mode=ParseMode.MARKDOWN_V2)
        context.bot.send_poll(
                chat_id=int(-1001539629311),
                question=que,
                options=options,
                type=Poll.QUIZ,
                correct_option_id=co,
                explanation=explan,
                is_anonymous=True,
                allows_multiple_answers=False,
                parse_mode=ParseMode.HTML)
        time.sleep(5)
        #return ConversationHandler.END
x=0
admin2=[]
def ghn2(update,context):
    global x
    print(str(x))
    x+=1
    z=""
    userText=update.message.poll
    que=userText.question
    que1=reaaa.sub("^(☞( ){1,}|)(((\[\d{1,}/\d{1,}\] ){1,}|)(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|)(\d{1,}\. |\d{1,}\.|))","",que)

    for y in admin2:
        col2=client["Schedule"]["Quiz"]
        try:
            Noo=col2.find_one({"Uid":str(y)})
            No=Noo['No']
            #print('suss======'+No+'======suss')
        except:
            No="1"
        que=No+".  "+que1
        options=[o.text for o in userText.options]
        co=userText.correct_option_id
        explan=userText.explanation
        try:
            col=client["Schedule"][str(y)]
            c={"chat_id":int(y),"question":que,"options":options,"correct_option_id":co,"explanation":explan}
            col.insert_one(c)
            col2=client["Schedule"]["Quiz"]
            if col2.find_one({"Uid":str(y)}) is None:
                col2.insert_one({"Uid":str(y),'No':No})
                print("new account")
            No=str(int(No)+1)
            col2=client["Schedule"]["Quiz"]
            #print("yoyoyk")
            myquery1 = {"Uid":str(y)}
            #print("yoyoyk")
            newvalues1 = { "$set": { "No":No} }
            #print("yoyoyk")
            col2.update_one(myquery1, newvalues1)
            z = z+" "+str(No)
        except Exception as e:
            print(str(e))
    z=reaaa.sub("^",str(x),z)
    context.bot.send_message(chat_id=711296045, text=z)
    return GHN2	


#@run_async
due1=18000
def alarm(context: CallbackContext):
    
    job = context.job
    due=due1
    try:
        col=client["Schedule"]
        #yy=col.list_collection_names({})
        for yyy in range(10):
            yy=col.list_collection_names({})
            yy.remove('Quiz')
            yy.remove('-1001517843177')
            for y in yy:
                coly=col[y]
                cou=coly.count_documents({})
                z=coly.find_one({})
                if cou==1:
                    coly.drop()
                chat_id=z["chat_id"]
                try:
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
                    coly.find_one_and_delete({})
                except:
                    pass
            time.sleep(5)
        context.job_queue.run_once(alarm, due, context=chat_id, name=str(chat_id))
        #time.sleep(5)
    except Exception as e:
        context.job_queue.run_once(alarm, due, context=chat_id, name=str(chat_id))
        print(str(e))
    
    
    
    
    
    
    
    


import fitz
#@restrictedD
@run_async
@send_typing_action
def poll(update, context):
    """Sends a predefined poll"""
    if reaaa.match("https://t.me/(c/|).*?/\d{1,}/.*?",update.message.text):
    	NewVar1=reaaa.split(r"\n", update.message.text)
    	print(NewVar1)
    	for x in NewVar1:
    	    NewVar=reaaa.sub("^https://t\.me/", "",x)
    	    NewVar=reaaa.sub("^c/", "-100",NewVar)
    	    NewVar=reaaa.split("/", NewVar)
    	    try:
    	        
    	        NewVar[0]=int(NewVar[0])
    	        cid1=str(NewVar[0])
    	    except:
    	        cid1=str(NewVar[0])
    	        NewVar[0]="@"+str(NewVar[0])
    	    try:
    	        Qn=int(NewVar[3])
    	    except:
    	        Qn=1
    	    NewVar2=reaaa.split("(,|)", NewVar[2])
    	    while '' in NewVar2: NewVar2.remove('')
    	    context.bot.forward_message(chat_id=-1001534819469,from_chat_id=NewVar[0],message_id=int(NewVar[1]))
    	    context.bot.send_message(chat_id=-1001534819469,text=update.message.text)
    	    zzz=int(NewVar[1])+1
    	    last=int(zzz)+len(NewVar2)
    	    for y in range(len(NewVar2)):
    	        reply_markup=None
    	        
    	        
    	        if y+1==len(NewVar2):
    	            explanation="find more on @polls_quiz"
    	            
    	            context.bot.send_message(chat_id=update.message.chat.id,text="/start@Soojhboojh_01bot share_quiz"+cid1+"moum"+str(NewVar[1])+"moum"+str(int(zzz)-int(NewVar[1]))+"moum"+str(last-int(NewVar[1])))
    	            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Share Quiz",url="tg://share?text=/start@Soojhboojh_01bot share_quiz"+cid1+"moum"+str(NewVar[1])+"moum"+str(int(zzz)-int(NewVar[1]))+"moum"+str(last-int(NewVar[1])))]])
    	        else:
    	            explanation=None
    	            reply_markup=None
    	        try:
    	            mess=context.bot.send_poll(
	            NewVar[0],
	            "Question Number "+str(Qn),
	            ["Option (A)","Option (B)","Option (C)","Option (D)"],
	            is_anonymous=False,type=Poll.QUIZ,
	            correct_option_id=int(NewVar2[y])-1,explanation=explanation,
	            reply_to_message_id=int(NewVar[1]),
	            allows_multiple_answers=False,reply_markup= (reply_markup),parse_mode=ParseMode.HTML,disable_web_page_preview = True
	        )
    	            Qn+=1#
    	            if y+2==len(NewVar2):
    	                last=int(mess.message_id)+1
    	            if y==0:
    	                zzz=int(mess.message_id)
    	        except:
    	            pass
    	        
    	        time.sleep(5)
    
    if reaaa.match("\d/.*",update.message.text):
    	global coded
    	coded[update.message.chat.id]=update.message.text
    	context.bot.send_message(chat_id=update.message.chat.id,text="add your token to my database for 1 h")
    
    if update.message.text=="My_quiz":
        col=client["group_schedule"][str(update.message.chat.id)]
        Nu=col.find_one({"Nu":{"$type":"array"}})["Nu"]
        data=col.find_one({"data":{"$type":"array"}})["data"]
        Time=col.find_one({"Time":{"$type":"string"}})["Time"]
        current_quiz=col.find_one({"data":{"$type":"array"}})["data"][Nu[0]][list(col.find_one({"data":{"$type":"array"}})["data"][Nu[0]].keys())[0]]
        keyboard=False
        if Nu[0]==0:
            keyboard=[[InlineKeyboardButton("Previous",callback_data="My_quiz"+str(len(data)-1)),InlineKeyboardButton("Next Play",callback_data="My_quiz"+"1")]]
        elif Nu[0]+1==len(data):
            keyboard=[[InlineKeyboardButton("Previous",callback_data="My_quiz"+str(Nu[0]-1)),InlineKeyboardButton("Next Play",callback_data="My_quiz0")]]
        else:
            keyboard=[[InlineKeyboardButton("Previous",callback_data="My_quiz"+str(Nu[0]-1)),InlineKeyboardButton("Next Play",callback_data="My_quiz"+str(Nu[0]+1))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=update.message.chat.id, text="Playing Next Quiz Number = "+str(Nu[0]+1)+"/"+str(len(data))+"\n\nSchedule Daily Time : - "+Time+"\n\n"+current_quiz,reply_markup=reply_markup,parse_mode=ParseMode.HTML,disable_web_page_preview = True)
    elif update.message.reply_markup:
	    #print(update.message.reply_markup.inline_keyboard[0][0].url)
	    if reaaa.match("^https://t\.me/QuizBot\?start\=.*?", update.message.reply_markup.inline_keyboard[0][0].url):
		    #print("huaa")
		    y=context.bot.get_chat_administrators(chat_id=update.message.chat.id)
		    xid=[]
		    for x in y:
		    	xid.append(x['user']['id'])
		    if update.message.from_user.id in xid:
		    	qname=update.message.reply_markup.inline_keyboard[0][0].url[27:]
		    	qdata=update.message.text
		    	col=client["group_schedule"][str(update.message.chat.id)]
		    	myquery1 = {"data":{"$type":"array"}}
		    	
		    	if col.find_one(myquery1):
		    		data=col.find_one(myquery1)["data"]
		    		data.append({qname:qdata})
		    		newvalues1 = { "$set": { "data":data} }
		    		col.update_one(myquery1,newvalues1)
		    	else:
		    		col.insert_one({"data":[{qname:qdata}]})
		    		col.insert_one({"Nu":[0]})
		    		if col.find_one({"Time":{"$type":"string"}}):
			    		pass
		    		else:
			    		col.insert_one({"Time":"10,12,19,20,21,22"})
		    	context.bot.send_message(chat_id=update.message.chat.id, text="Quiz added") 
		    	time.sleep(5)
    elif str(update.message.from_user.id) in LIST_OF_ADMINS:
	    try:
	        from excle_c import main
	        data,filename=main(update.message.text)
	        import xlsxwriter
	        #context.bot.send_message(chat_id=update.message.chat.id, text=str(data))
	        workbook = xlsxwriter.Workbook(filename+'.xlsx')
	        worksheet = workbook.add_worksheet()
	        #context.bot.send_message(chat_id=update.message.chat.id, text=str(data))
	        for x in range(len(data)):
	            for y in range(len(data[x])):
	                worksheet.write(x,y, data[x][y])
	        workbook.close()
	        #context.bot.send_document(update.message.chat.id, open(filename+'.xlsx', "rb"))#,caption=caption1, parse_mode=ParseMode.HTML,reply_to_message_id=colmessage)
	        from quickstart import Drive_OCR
	        filename1=Drive_OCR(filename+'.xlsx').main1()
	        
	        context.bot.send_document(update.message.chat.id, open(filename1, "rb"))#,caption=caption1, parse_mode=ParseMode.HTML,reply_to_message_id=colmessage)
	        
	        
	        #context.bot.send_message(chat_id=update.message.chat.id, text="Quiz added")
	        #context.bot.send_document(update.message.chat.id, open('Result.pdf', "rb"))#,caption=caption1, parse_mode=ParseMode.HTML,reply_to_message_id=colmessage)
	    except Exception as e:
	        pass#context.bot.send_message(chat_id=update.message.chat.id, text=str(e))
	    quest=(update.message.text)
	    #
	    quest=reaaa.sub("Sol\.\(a\).*", "1", quest)
	    quest=reaaa.sub("Sol\.\(b\).*", "2", quest)
	    quest=reaaa.sub("Sol\.\(c\).*", "3", quest)
	    quest=reaaa.sub("Sol\.\(d\).*", "4", quest)
	    print("test")
	    print("poll Conversation = "+update.message.text)
	    try:
	        q=quest[0:-1]
	        q=reaaa.sub("Poll to Text Bot\:\n|Soojh Boojh Bot - 02\:\n|NaN| Q.*\.|^\. |^\.", "", q)
	        q=reaaa.sub(r"(\n| )(\(|\[|)(A|B|C|D|a|b|c|d|अ|ब|बी|स|सी|डी|ड|द|क|ख|ग|घ|1|2|3|4)(\)|\]|\.)(\.| |)", "\n", q)
	        q=reaaa.sub("\n{2,}", "\n", q)
	        q=reaaa.sub("☞", "", q)
	        q=reaaa.split(r"[\n]", q)
	        #update.message.reply_text(q)
	        ques=q[0]
	        ques=reaaa.sub(r"^((((\[\d{1,}/\d{1,}\] ){1,}|)(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|)))", "", ques)
	        que= ques
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
	        chatiid=int(update.message.chat.id)
	        if chatiid<=0:
	            if reaaa.findall("(.*?\n{1,}){4,}.*?",update.message.text):
	                print("restrictedD wants to delete message")
	                #context.bot.delete_message(chat_id=chatiid,message_id=update.message.message_id)
	        time.sleep(5)
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
    uurrl=""
    chat___id=int(update.message.chat.id)
    Ccc=update.message.from_user.id
    if chat___id<=0:
        try:
            if update.message.text.startswith("/start@Soojhboojh_01bot share_quiz"):
                try:
                    context.bot.delete_message(chat_id=update.message.id,message_id=update.message.message_id)
                except:
                    pass
                print(update.message.text)
                x=reaaa.sub("/start@Soojhboojh_01bot share_quiz","",update.message.text)
                x=reaaa.split("moum",x)
                try:
                    x[0]=int(x[0])
                except:
                    x[0]="@"+str(x[0])
                context.bot.forward_message(chat_id=update.message.chat.id,from_chat_id=x[0],message_id=int(x[1]))
                for y in range(int(x[1])+int(x[2]),int(x[1])+int(x[3])+1):
                    try:
                        context.bot.forward_message(chat_id=update.message.chat.id,from_chat_id=x[0],message_id=int(y))
                    except:
                        pass
            elif update.message.text.startswith("/start@Soojhboojh_01bot Share"):
                db = client.get_database('QuizList')
                results = db.get_collection('quizlist')
                unique_id=reaaa.sub("/start@Soojhboojh_01bot Share","",update.message.text)
                quiz_name=results.find_one({"quizid":unique_id})["quizname"]
                col=client["Quiz"]["Quizlist"]
                x=col.find_one({"Id":quiz_name})
                context.bot.send_message(chat_id=711296045, text="<a href=\"tg://openmessage?user_id="+str(Ccc)+"\"><b>User</b></a>\nGroup = @"+update.message.chat.username+"\n"+quiz_name,parse_mode=ParseMode.HTML,disable_web_page_preview = True)
                try:
                    keyboard = [
                [
                    #InlineKeyboardButton("Play Quiz", callback_data='3',url="https://telegram.me/Soojhboojh_01bot?start=Play"+unique_url[23:]),
                    InlineKeyboardButton("Result", callback_data='2',url="https://quizresults.cf/"+unique_id),#],[
        #],[
        #InlineKeyboardButton("Play in Group", callback_data='1',url="https://telegram.me/Soojhboojh_01bot?startgroup=Share"+unique_url[23:]),
                ],
                	]
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    coll=client["Quiz_Data"][quiz_name]
                    colldb=coll.find()
                    messa=context.bot.send_message(chat_id=chat___id, text="🎲 Get ready for the LIVE TEST \'"+quiz_name+"\'\n\n🖊 "+str(coll.count_documents({}))+" questions\n\n📰 Votes are visible to group members and shared all polls \nevery ✔︎ Question gain ✙4 Marks\nevery ✖︎ Question gain –1 Mark\n\n<b>Playing Group @"+str(update.message.chat.username)+"\n\nFor more #Soojh_Boojh</b>", reply_markup=reply_markup, parse_mode=ParseMode.HTML,disable_web_page_preview = True)
                    channel_ids=x["Channel_Id"]
                    colme=client["Quiz"]["Message"]
                    coldoc={"MessID":messa.message_id,"ID":"@"+update.message.chat.username+"_"+quiz_name}
                    print(coldoc)
                    try:
                        colme.delete_many({"ID":"@"+update.message.chat.username+"_"+quiz_name})
                        print("delete successful")
                    except Exception as e:
                        print("First time play or not play. "+str(e))
                    colme.insert_one(coldoc)
                    print("insert successful")
                    
                    try:
                        for y in x[quiz_name]:
                            context.bot.forward_message(chat_id=chat___id,from_chat_id=channel_ids, message_id=y)
                            '''if %4==2:
                                time.sleep(5)'''
                        keyboard = [
                [
                    InlineKeyboardButton("Play Quiz", callback_data='3',url="https://telegram.me/Soojhboojh_01bot?start=Play"+unique_id),
                    InlineKeyboardButton("Result", callback_data='2',url="https://quizresults.cf/"+unique_id),],[
        #],[
        InlineKeyboardButton("Play in Group", callback_data='1',url="https://telegram.me/Soojhboojh_01bot?startgroup=Share"+unique_id),
                ],
            ]
                        reply_markup = InlineKeyboardMarkup(keyboard)
                        context.bot.send_message(chat_id=chat___id,text='<b>'+quiz_name+'</b>', reply_markup=reply_markup,parse_mode=ParseMode.HTML)
                        #context.bot.send_message(chat_id=chat___id, text="<a href=\"https://telegram.me/Soojhboojh_01bot?start\">🌐 Click Sharing ☜ </a>", parse_mode=ParseMode.HTML,disable_web_page_preview = True)
                    except Exception as e:
                        context.bot.send_message(chat_id=chat___id, text="Give me Polls send permission to upload quiz hereaaa...\nerror name = "+str(e), parse_mode=ParseMode.HTML)
                except Exception as e:
                    print(str(e))
                            
                            
            else:
                chat___id="@"+str(update.message.chat.username)#id
                mesho01=context.bot.send_message(chat_id=chat___id, text="<a href=\"https://t.me/Soojhboojh_01bot?start\">🌐 find Quiz Name Here☜</a>\nSend me Quiz name that you want to play",parse_mode=ParseMode.HTML,disable_web_page_preview = True)
                context.bot.send_message(chat_id=711296045, text="<a href=\"tg://openmessage?user_id="+str(Ccc)+"\"><b>user tring to share</b></a> = "+chat___id,parse_mode=ParseMode.HTML,disable_web_page_preview = True)


        except Exception as e:
            print(str(e))
        return POLLF
    elif update.message.text.startswith("/start Play"):
        if True:
            if True:
                db = client.get_database('QuizList')
                results = db.get_collection('quizlist')
                unique_id=reaaa.sub("/start Play","",update.message.text)
                quiz_name=results.find_one({"quizid":unique_id})["quizname"]
                col=client["Quiz"]["Quizlist"]
                x=col.find_one({"Id":quiz_name})
                context.bot.send_message(chat_id=-611934865, text="<a href=\"tg://openmessage?user_id="+str(Ccc)+"\"><b>User</b></a>\n"+quiz_name,parse_mode=ParseMode.HTML,disable_web_page_preview = True)
                try:
                    coll=client["Quiz_Data"][quiz_name]
                    colldb=coll.find()
                    messa=context.bot.send_message(chat_id=chat___id, text="🎲 Get ready for the LIVE TEST \'"+quiz_name+"\'\n\n🖊 "+str(coll.count_documents({}))+" questions\n\n📰 Votes are visible to group members and shared all polls \nevery ✔︎ Question gain ✙4 Marks\nevery ✖︎ Question gain –1 Mark\n\n<b>For more #Soojh_Boojh</b>", parse_mode=ParseMode.HTML,disable_web_page_preview = True)
                    channel_ids=x["Channel_Id"]
                    #colme=client["Quiz"]["Message"]
#                    coldoc={"MessID":messa.message_id,"ID":"@"+update.message.chat.username+"_"+quiz_name}
#                    print(coldoc)
#                    try:
#                        colme.delete_many({"ID":"@"+update.message.chat.username+"_"+quiz_name})
#                        print("delete successful")
#                    except Exception as e:
#                        print("First time play or not play. "+str(e))
#                    colme.insert_one(coldoc)
#                    print("insert successful")
                    
                    try:
                        for y in x[quiz_name]:
                            context.bot.forward_message(chat_id=chat___id,from_chat_id=channel_ids, message_id=y)
                            '''if %4==2:
                                time.sleep(5)'''
                        keyboard = [
                [
                    InlineKeyboardButton("Play Quiz", callback_data='3',url="https://telegram.me/Soojhboojh_01bot?start=Play"+unique_id),
                    InlineKeyboardButton("Result", callback_data='2',url="https://quizresults.cf/"+unique_id),],[
        #],[
        InlineKeyboardButton("Play in Group", callback_data='1',url="https://telegram.me/Soojhboojh_01bot?startgroup=Share"+unique_id),
                ],
            ]
                        reply_markup = InlineKeyboardMarkup(keyboard)
                        context.bot.send_message(chat_id=chat___id,text='<b>'+quiz_name+'</b>', reply_markup=reply_markup,parse_mode=ParseMode.HTML)
                        #context.bot.send_message(chat_id=chat___id, text="<a href=\"https://telegram.me/Soojhboojh_01bot?start\">🌐 Click Sharing ☜ </a>", parse_mode=ParseMode.HTML,disable_web_page_preview = True)
                    except Exception as e:
                        context.bot.send_message(chat_id=chat___id, text="Give me Polls send permission to upload quiz hereaaa...\nerror name = "+str(e), parse_mode=ParseMode.HTML)
                except Exception as e:
                    print(str(e))
    else:
        db=client["user"]["sub"]
        col=db.find_one(({"Uid":update.message.chat.id}))
        if bool(col):
            pass
        else:
            db.insert_one({"Uid":update.message.chat.id})
        query=update.message.text
        #print(query)
        query=reaaa.sub("/start ","",query)
        ddd=reaaa.split("_",query)
        qN=ddd[0]
        qQ=str(ddd[1])
        col=client["QuizC"][qN]
        yy=col.find({"cor":{"$type":"string"}})
        exp=yy[int(qQ)-1]["exp"]
        uurrl="_".join(ddd[3:])
        uurrl=reaaa.sub("_701400400000000","/",uurrl)
        uurrl="https://t.me/"+uurrl
        print("uurrl = "+str(uurrl))
        keyboard = [[InlineKeyboardButton("Go Back to Question", url=uurrl),],]
        reply_markup = InlineKeyboardMarkup(keyboard)
        if bool(reaaa.findall(r"^https://t\.me/.*",exp)):
            context.bot.sendPhoto(chat_id=int(chat___id), photo=(exp),reply_markup=reply_markup,parse_mode=ParseMode.HTML)
        else:
            context.bot.send_message(chat_id=int(chat___id), text=exp,reply_markup=reply_markup,parse_mode=ParseMode.HTML)
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
            context.bot.send_message(chat_id=chat___id, text="Give me Polls send permission to upload quiz hereaaa...", parse_mode=ParseMode.HTML)
    except Exception as e:
        print(str(e))
    return ConversationHandler.END

PDF = range(1)
from KrutidevToUnicode3 import KrutidevToUnicode
def pdf(update,context):
	update.message.reply_text("Send me pdf text that you want ro convert into hindi text.\nSome pdf can convert some not...\n\nCancel any time click /cancel")
	return PDF

def pdfc(update,context):
	"""Echo the user message."""
	x=str(update.message.text)
	update.message.reply_text(KrutidevToUnicode.convert_to_unicode(x))
	return PDF
	

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if bool(reaaa.match("^My_quizset\d{1,}$",query.data)):
	       col=client["group_schedule"][str(query.message.chat.id)]
	       Nu=[int(reaaa.sub("My_quizset","",query.data))]
	       y=context.bot.get_chat_administrators(chat_id=query.message.chat.id)
	       xid=[]
	       print(str(query))
	       for x in y:
	         print(x['user']['id'])
	         xid.append(x['user']['id'])
	       if query.from_user.id in xid:
	         col.update_one({"Nu":{"$type":"array"}},{"$set":{"Nu":Nu}})
	         query.answer("Set Successfully")
	       else:
	         query.answer("You are'not admin in this Group")
    elif bool(reaaa.match("^My_quiz\d{1,}$",query.data)):
	       col=client["group_schedule"][str(query.message.chat.id)]
	       Nu=[int(reaaa.sub("My_quiz","",query.data))]
	       Time=col.find_one({"Time":{"$type":"string"}})["Time"]
	       data=col.find_one({"data":{"$type":"array"}})["data"]
	       current_quiz=col.find_one({"data":{"$type":"array"}})["data"][Nu[0]][list(col.find_one({"data":{"$type":"array"}})["data"][Nu[0]].keys())[0]]
	       query.answer()
	       keyboard=False
	       if Nu[0]==0:
	           keyboard=[[InlineKeyboardButton("Previous",callback_data="My_quiz"+str(len(data)-1)),InlineKeyboardButton("Set Quiz",callback_data="My_quiz"+"set0"),InlineKeyboardButton("Next Play",callback_data="My_quiz"+"1")]]
	       elif Nu[0]+1==len(data):
	           keyboard=[[InlineKeyboardButton("Previous",callback_data="My_quiz"+str(Nu[0]-1)),InlineKeyboardButton("Set Quiz",callback_data="My_quiz"+"set"+str(Nu[0])),InlineKeyboardButton("Next Play",callback_data="My_quiz"+str(0))]]
	       else:
	           keyboard=[[InlineKeyboardButton("Previous",callback_data="My_quiz"+str(Nu[0]-1)),InlineKeyboardButton("Set Quiz",callback_data="My_quiz"+"set"+str(Nu[0])),InlineKeyboardButton("Next Play",callback_data="My_quiz"+str(Nu[0]+1))]]
	       reply_markup = InlineKeyboardMarkup(keyboard)
	       query.edit_message_text(text="Quiz Number = "+str(Nu[0]+1)+"/"+str(len(data))+" DATA\n\nSchedule Daily Time : - "+Time+"\n\n"+current_quiz,reply_markup=reply_markup,parse_mode=ParseMode.HTML,disable_web_page_preview = True)
    else:
    	ddd=reaaa.split("_",query.data)
    	qN=ddd[0]
    	qQ=str(ddd[1])
    	print(qQ)
    	qA=ddd[2]
    	#print(qA)
    	col=client["QuizC"][qN]
    	cou1=str(col.count_documents({"type":"Quiz"}))
    	yy=col.find({"cor":{"$type":"string"}})
    	cor=yy[int(qQ)-1]["cor"]
    	
    	exp=yy[int(qQ)-1]["exp"]
    
    	
    	uId=(query.from_user.id)
    	coll=client["QuizCData"][qN]
    	
    	qq=None
    	if coll.find_one({"uid":uId,qQ:{"$type":"string"}}):
    		#print("2")
    		
    		M="0"
    		ccc=coll.find_one({"uid":uId,qQ:{"$type":"string"}})
    		qq=str(ccc[qQ])
    		try:
    			Marks = ccc["Marks"]
    		except:
    			Marks = "0"
    	elif coll.find_one({"uid":uId}):
    		#coll.find_and_modify
    		print(qA)
    		print("yooo")
    		print(cor)
    		if str(qA)!="0":
    			if str(qA)==str(cor):
    				M="4"
    			else:
    				M="-1"
    		else:
    			M="0"
    		
    		ccc=coll.find_one({"uid":uId})
    		#print(str(ccc))
    		try:
    			Marks = ccc["Marks"]
    		except:
    			Marks="0"
    		myquery1 = {"uid":uId}
    		Marks=int(Marks)+int(M)
    		newvalues1 = {"uid":uId, qQ:qA,"Marks":str(Marks)}
    		#print(myquery1)
    		#print(newvalues1)
    		if qA!="0":
    			coll.update_one(myquery1,{"$set":newvalues1})
    	else:
    		if qA!="0":
    			Marks="0"
    			if qA==cor:
    				M="4"
    			else:
    				M="-1"
    			Marks=int(Marks)+int(M)
    			coll.insert_one({"uid":uId,qQ:qA,"Marks":str(Marks)})
    	exp1=""
    	if qA=='0':
    		if qq:
    			print("https://t.me/Soojhboojh_01bot?start="+str(update.callback_query.data)+"_"+str(update.callback_query.message.chat.username)+"/"+str(update.callback_query.message.message_id))
    			if bool(reaaa.match("^$",exp)):
    				query.answer(text="Now we don't have Explanation\n\nहमारे पास अभी कोई भी hint नहीं है।🙏🙏", show_alert=True)
    				#context.bot.sendPhoto(chat_id=int(uId), photo=(exp))
    				print(bool(reaaa.match("^$",exp)))
    			elif bool(reaaa.findall(r"^https://t\.me/.*",exp)):
    				
    				try:
    					#context.bot.sendPhoto(chat_id=int(uId), photo=(exp))#caption=caption)
    					query.answer(text="@soojhboojh_01bot Bot send you a file or Photo message please check\n\nsoojhboojh_01bot ने आपको message send किया है अभी", show_alert=True,url="https://t.me/Soojhboojh_01bot?start="+str(update.callback_query.data)+"_"+str(update.callback_query.message.chat.username)+"_701400400000000"+str(update.callback_query.message.message_id))
    				except:
    					query.answer(text="First go to @soojhboojh_01bot and start conversation.\n\nसबसे पहले @soojhboojh_01bot पर जाइये और /start button दबाइये🙏🙏", show_alert=True,url="https://t.me/Soojhboojh_01bot?start="+str(update.callback_query.data)+"_"+str(update.callback_query.message.chat.username)+"_701400400000000"+str(update.callback_query.message.message_id))
    			else:
    				try:
    					#context.bot.send_message(chat_id=int(uId), text=exp)
    					query.answer(text="@soojhboojh_01bot Bot send you a file or text message please check\n\nsoojhboojh_01bot ने आपको message send किया है अभी", show_alert=True,url="https://t.me/Soojhboojh_01bot?start="+str(update.callback_query.data)+"_"+str(update.callback_query.message.chat.username)+"_701400400000000"+str(update.callback_query.message.message_id))
    				except:
    					query.answer(text="First go to @soojhboojh_01bot and start conversation.\n\nसबसे पहले @soojhboojh_01bot पर जाइये और /start button दबाइये🙏🙏", show_alert=True,url="https://t.me/Soojhboojh_01bot?start="+str(update.callback_query.data)+"_"+str(update.callback_query.message.chat.username)+"_701400400000000"+str(update.callback_query.message.message_id))
    		else:
    			query.answer(text="First select option then click Q_Number for Hint\n\nसबसे पहले एक option select कीजिये तब आप explanation जान पाओगें यदि explanation होगी तो🙏🙏", show_alert=True)
    	elif qq:
    		
    		if exp!="":
    			exp1="\n\n\nFor explanation click Q_"+qQ+" button"
    		if qq==cor:
    			query.answer(text=f"Selected option: {qA}\nRight Ans: {cor}\nfirst time Selected option :{qq}\nyou gain = 4📈\n\nYour Marsk for this Quiz is == {Marks}"+exp1 , show_alert=True)
    		else:
    			query.answer(text=f"Selected option: {qA}\nRight Ans: {cor}\nfirst time Selected option :{qq}\nyou lost = 1📉\n\nYour Marsk for this Quiz is == {Marks}"+exp1 , show_alert=True)
    	elif cor==qA:
    		query.answer(text=f"Selected option: {qA}\nRight Ans: {cor}\nyou gain = 4📈\n\nYour Marsk for this Quiz is == {Marks}"+exp1 , show_alert=True)
    	else:
    		query.answer(text=f"Selected option: {qA}\nRight Ans: {cor}\nyou lost = 1📉\n\nYour Marsk for this Quiz is == {Marks}"+exp1 , show_alert=True)
    	if exp!="":
    		keyboard = [
            [
                InlineKeyboardButton("Q_"+str(qQ), callback_data=qN+"_"+str(qQ)+'_0'),
                InlineKeyboardButton("A", callback_data=qN+"_"+str(qQ)+'_1'),
                InlineKeyboardButton("B", callback_data=qN+"_"+str(qQ)+'_2'),
                InlineKeyboardButton("C", callback_data=qN+"_"+str(qQ)+'_3'),
                InlineKeyboardButton("D", callback_data=qN+"_"+str(qQ)+'_4'),],
        ]
    
    		reply_markup = InlineKeyboardMarkup(keyboard)
    		print(query.message.text)
    		try:
    			if reaaa.search("👇 Explanation here",str(query.message.caption)):
    				print("start caption")
    			else:
    				tex=query.message.caption
    				#print("main thing ="+str(query))
    				#tex=reaaa.sub("^","<b>",tex)
    				#tex=reaaa.sub("(?<=^.*?)\n","\n</b>",tex)
    				if tex is None:
    					tex=""
    				print(tex)
    				query.edit_message_caption(tex+"\n\n👇 Explanation here",reply_markup=reply_markup,parse_mode=ParseMode.HTML)
    				print("Done Caption")
    			print()
    		except:
    			
    			if reaaa.search("👇 Explanation here",query.message.text):
    				print("start text")
    			else:
    				tex=query.message.text
    				if tex is None:
    					tex=""
    				query.edit_message_text(tex+"\n\n👇 Explanation here",reply_markup=reply_markup,parse_mode=ParseMode.HTML)
    				print("Done Text")
    	


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")

file_text=""
def photos(update,context):
    global file_text
    bot=context.bot
    
    #file_text=update.message.caption
    #print(file_text)
    keyboard = [
        [
            InlineKeyboardButton("A", callback_data='1'),
            InlineKeyboardButton("B", callback_data='2'),
            InlineKeyboardButton("C", callback_data='3'),
            InlineKeyboardButton("D", callback_data='4'),],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    #file_id = update.message.photo[-1]
    #newFile = bot.getFile(file_id)
    #newFile.download('/storage/emulated/0/ADM/New Folder/test.jpg')
    #bot.sendPhoto(chat_id=update.message.chat_id,  photo='https://t.me/SudhirParihar/4856',caption='https://t.me/SudhirParihar/4856',reply_markup=reply_markup)
    #bot.sendDocument(chat_id=update.message.chat_id,  document=('https://t.me/PariharClasses/963'),caption="Here is your today Question",reply_markup=reply_markup)

quizName=""
CALL=range(1)
def upload1(update,context):
	global quizName
	update.message.reply_text("send me Quiz deta")
	quizName=(update.message.text)
	quizName=reaaa.sub("/create ","",quizName)
	
	return CALL
def call1(update,context):
	#print(update)
	callv=update.message.text
	callv=reaaa.sub("\n(\(a\) ){10,}\(a\)","",callv)
	#print(callv)
	if bool(reaaa.match("1|2|3|4",callv[-1])):
		data=callv[:-1]
		cor=callv[-1]
	else:
		data=callv
		cor=None
	col=client["QuizC"][quizName]
	if cor:
		new={"type":"text","data":data,"cor":cor,"exp":""}
	else:
		new={"type":"text","data":data,"cor":cor,"exp":""}
	print(new)
	col.insert_one(new)
	print("sussful")
	return CALL
def call2(update,context):
	col=client["QuizC"][quizName]
	#print(update)
	data="https://t.me/"+update.message.forward_from_chat.username+"/"+str(update.message.forward_from_message_id)
	
	if bool(reaaa.match("1|2|3|4",update.message.caption[-1])):
		caption=update.message.caption[:-1]
		cor=update.message.caption[-1]
	else:
		caption=update.message.caption
		cor=None
	if cor:
		new={"type":"photo","data":data,"text":caption,"cor":cor,"exp":""}
	else:
		new={"type":"photo","data":data,"text":caption,"cor":cor,"exp":""}
	print(new)
	col.insert_one(new)
	print("sussful")
	return CALL

def call6(update,context):
	poll=update.message.poll
	question=poll.question
	option=[o.text for o in poll.options]
	option="\n".join(option)
	cor=str(poll.correct_option_id+1)
	text=question+"\n\n"+option
	new={"type":"text","data":text,"cor":cor,"exp":""}
	col=client["QuizC"][quizName]
	col.insert_one(new)

def cancel(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END
#var3=1
def call3(update,context):
	print("start")
	#print(update)
	callv=update.message.text
	callv=reaaa.sub("/startquiz ","",callv)
	callv=reaaa.split("_", callv)
	var3=1
	print(callv)
	col=client["QuizC"][callv[0]]
	yy=col.find({})
	for y in yy:
		print("3")
		cor=y["cor"]
		type=y["type"]
		data=y["data"]
		try:
			caption=y["text"]
		except:
			caption=False
		print(data)
		keyboard = [
        [
            InlineKeyboardButton("Q_"+str(var3), callback_data=callv[0]+"_"+str(var3)+'_0'),
            InlineKeyboardButton("A", callback_data=callv[0]+"_"+str(var3)+'_1'),
            InlineKeyboardButton("B", callback_data=callv[0]+"_"+str(var3)+'_2'),
            InlineKeyboardButton("C", callback_data=callv[0]+"_"+str(var3)+'_3'),
            InlineKeyboardButton("D", callback_data=callv[0]+"_"+str(var3)+'_4'),],
    ]
		
	
		reply_markup = InlineKeyboardMarkup(keyboard)
		if cor:
			if type=="text":
				context.bot.send_message(chat_id=int(callv[1]), text=data, reply_markup=reply_markup,parse_mode=ParseMode.HTML)
			elif type=="photo":
				context.bot.sendPhoto(chat_id=int(callv[1]),  photo=(data),caption=caption,reply_markup=reply_markup,parse_mode=ParseMode.HTML)
			var3+=1
		else:
			if type=="text":
				context.bot.send_message(chat_id=int(callv[1]), text=data, parse_mode=ParseMode.HTML)
			elif type=="photo":
				context.bot.sendPhoto(chat_id=int(callv[1]),  photo=(data),caption=caption)#,reply_markup=reply_markup,parse_mode=ParseMode.HTML)
		time.sleep(5)
	
quizName1=""
CALL1=range(1)
def upload2(update,context):
	global quizName1
	update.message.reply_text("send me Quiz explain deta")
	quizName1=(update.message.text)
	#print(quizName1)
	quizName1=reaaa.sub("/adde ","",quizName1)
	
	return CALL1
def call4(update,context):
	#print(quizName1)
	callv=update.message.text
	#print(callv)
	var=reaaa.split("_",quizName1)
	#print(var)
	col=client["QuizC"][var[0]]
	colll=col.find({"cor":{"$type":"string"}})[int(var[1])-1]
	colll=colll["data"]
	#print(colll)
	myquery1 = {"data":colll}
	newvalues1 = {"exp":callv}
	#print(myquery1)
	#print(newvalues1)
	#col.update_one
	col.update_one(myquery1,{"$set":newvalues1})
	print("sussful")
	return ConversationHandler.END
def call5(update,context):
	print(quizName1)
	callv=data="https://t.me/"+update.message.forward_from_chat.username+"/"+str(update.message.forward_from_message_id)
	#print(callv)
	var=reaaa.split("_",quizName1)
	#print(var)
	col=client["QuizC"][var[0]]
	colll=col.find({"cor":{"$type":"string"}})[int(var[1])-1]
	colll=colll["data"]
	#print(colll)
	myquery1 = {"data":colll}
	newvalues1 = {"exp":callv}
	#print(myquery1)
	#print(newvalues1)
	#col.update_one
	col.update_one(myquery1,{"$set":newvalues1})
	print("sussful")
	return ConversationHandler.END

def current(update,context):
    """Sends a message with three inline buttons attached."""
    
    col=client["current"]["URL"]
    myquery1 = {"URL":{"$type":"array"}}
    #newvalues1 = {"URL":URL}
    URL=[]
    URL1=col.find_one(myquery1)["URL"]
    #print(URL1)
    for x in URL1:
    	print(x)
    	if x.startswith("https://"):
    	    URL.append(x)
    	    
    	
    URL.reverse()
    x=([[InlineKeyboardButton(i+j*7+1, url=URL[i+j*7]) for i in range(7)] for j in range(len(URL)//7)])
    x.append([InlineKeyboardButton(y+1, url=URL[y]) for y in range(len(URL)-len(URL)%7 ,len(URL))])
    reply_markup = InlineKeyboardMarkup(x)
    if str(update.message.chat.id)=="786181993":
    	x.append([InlineKeyboardButton("Maths Quiz", url="https://t.me/Maths_Quiz_Notes")])
    	x.append([InlineKeyboardButton("Study GK Quiz", url="https://t.me/Study_Quiz_India")])
    	x.append([InlineKeyboardButton("Current IQ", url="https://t.me/Current_Affairs_Quiz_Notes")])
    #elif str(update.message.chat.id)=="555919730":
    	#x.append([InlineKeyboardButton("Current GK", url="https://t.me/gk_current20")])
    context.bot.send_message(chat_id=update.message.chat.id,text='<b>🔊 मार्च 2022 के <u>Current Affairs</u> को <u>One Liner</u> के माध्यम से 2 मिनट में याद कर लीजिये 🤩</b>\n\n<b><tg-spoiler>● अपने दोस्तों को शेयर करना न भूलें 😊</tg-spoiler></b>', reply_markup=reply_markup,parse_mode=ParseMode.HTML,disable_web_page_preview = True)

from apiclient import discovery
from httplib2 import Http


import logging
import socket
import sys
from six.moves import BaseHTTPServer
from six.moves import http_client
from six.moves import input
from six.moves import urllib

from oauth2client import _helpers

def _CreateArgumentParser():
    try:
        from oauth2client import client, file, tools
        import argparse
    except ImportError:  # pragma: NO COVER
        return None
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--auth_host_name', default='localhost',
                        help='Hostname when running a local web server.')
    parser.add_argument('--noauth_local_webserver', action='store_true',
                        default=False, help='Do not run a local web server.')
    parser.add_argument('--auth_host_port', default=[8080, 8090], type=int,
                        nargs='*', help='Port web server should listen on.')
    parser.add_argument(
        '--logging_level', default='ERROR',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help='Set the logging level of detail.')
    return parser

class ClientRedirectServer(BaseHTTPServer.HTTPServer):
    """A server to handle OAuth 2.0 redirects back to localhost.

    Waits for a single request and parses the query parameters
    into query_params and then stops serving.
    """
    from oauth2client import client, file, tools
    query_params = {}

class ClientRedirectHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """A handler for OAuth 2.0 redirects back to localhost.

    Waits for a single request and parses the query parameters
    into the servers query_params and then stops serving.
    """

    def do_GET(self):
        """Handle a GET request.

        Parses the query parameters and prints a message
        if the flow has completed. Note that we can't detect
        if an error occurred.
        """
        from oauth2client import client, file, tools
        self.send_response(http_client.OK)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        parts = urllib.parse.urlparse(self.path)
        query = _helpers.parse_unique_urlencoded(parts.query)
        self.server.query_params = query
        self.wfile.write(
            b'<html><head><title>Authentication Status</title></head>')
        self.wfile.write(
            b'<body><p>The authentication flow has completed.</p>')
        self.wfile.write(b'</body></html>')

    def log_message(self, format, *args):
        """Do not log messages to stdout while running as cmd. line program."""


argparser = _CreateArgumentParser()

coded={}
@run_async
def call7(update,context):
	
	#from oauth2client import client
	from oauth2client import client, file, tools
	SCOPES = "https://www.googleapis.com/auth/forms.body"
	DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"
	
	store = file.Storage('token'+str(update.message.chat.id)+'.json')
	creds = None
	form_service=None
	if not creds or creds.invalid:
		flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
		flags=None
		if flags is None:
		    flags = argparser.parse_args()
		logging.getLogger().setLevel(getattr(logging, flags.logging_level))
		if not flags.noauth_local_webserver:
		     success = False
		     port_number = 0
		     for port in flags.auth_host_port:
		          port_number = port
		          try:
		              httpd = ClientRedirectServer((flags.auth_host_name, port),
                                             ClientRedirectHandler)
		          except socket.error:
		              pass
		          else:
		              success = True
		              break
		     flags.noauth_local_webserver = not success
		     oauth_callback = client.OOB_CALLBACK_URN
		     
		     flow.redirect_uri = oauth_callback
		     authorize_url = flow.step1_get_authorize_url()
		     context.bot.send_message(chat_id=update.message.chat.id,text=authorize_url)
		code = None
		def my():
		    try:
		        global coded
		        global form_service
		        
		        code=coded[update.message.chat.id].strip()
		        
		        try:
		            http=None
		            credential = flow.step2_exchange(code, http=http)
		        except client.FlowExchangeError as e:
		            context.bot.send_message(chat_id=update.message.chat.id,text=str(e))
		            sys.exit('Authentication has failed: {0}'.format(e))
		        print(coded)
		        store.put(credential)
		        credential.set_store(store)
		        
		        creds=credential
		        
		        form_service = discovery.build('forms', 'v1', http=creds.authorize(Http()),discoveryServiceUrl=DISCOVERY_DOC)
		        #from quickstart import Drive_OCR
		        #file=Drive_OCR(data[update.message.chat.id]['info']+" (Responce).xlsx").main2()
		        NEW_FORM = {"info": {"title": data[update.message.chat.id]['info']}}#,#"linkedSheetId":file}
		        
		        result = form_service.forms().create(body=NEW_FORM).execute()
		        #context.bot.send_message(chat_id=update.message.chat.id,text=str(file))
		        update1 = {
    "requests": [
        {
            "updateSettings": {
                "settings": {
                    "quizSettings": {
                        "isQuiz": True
                    }
                },
                "updateMask": "quizSettings.isQuiz"
            }
        }
    ]
}
		        form_service.forms().batchUpdate(formId=result["formId"],
                                                    body=update1).execute()
		        for x in data[update.message.chat.id]['Q']:
		            form_service.forms().batchUpdate(formId=result["formId"], body=x).execute()
		        time.sleep(5)
		        get_result = form_service.forms().get(formId=result["formId"]).execute()
		        context.bot.send_message(chat_id=update.message.chat.id,text=str(result))
		        #context.bot.send_message(chat_id=update.message.chat.id,text=str(file))
		        coded.pop(update.message.chat.id)
		    except Exception as p:
		        print(str(p))
		        time.sleep(2)
		        my()
		
	my()

AA,BB,CC= range(3)
data=""
@run_async
def call8(update,context):
    context.bot.send_message(chat_id=update.message.chat.id,text="title: ...h \n discription: any thing")
    return BB

def gfm(update,context):
    global data
    info = update.message.text
    context.bot.send_message(chat_id=update.message.chat.id,text="title: ... \n discription: ")
    data="""function createForm() {
  
   // create & name Form  
   var item = '"""+reaaa.sub("\n",r"\\n",reaaa.sub("(\"|\')","\\'",info))+"""';
   var ss = SpreadsheetApp.create(item);
   var form = FormApp.create(item)
     .setTitle(item)
     .setIsQuiz(true)
     .setShuffleQuestions(false)
     .setDescription("Please subscribe channal \\n\\nhttps://youtube.com/channel/UCDnlmiR6XtdjRe7kolFQHLA")
     .setConfirmationMessage('Thanks for Playing Quiz\\n\\nId of this Quiz : '+ss.getId())
     .setLimitOneResponsePerUser(true);    
     
   // Update the form's response destination.
   form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());
   // single line text field  
   item = "Your Name";  
   form.addTextItem()
     .setTitle(item)
     .setRequired(true);
     
   // radiobuttons
   Utilities.sleep(240000);
   item = "Handout format";  
"""
    
    
    return AA

def gfp(update,context):
    global data
    actual_poll = update.message.poll
    question= actual_poll.question
    opt=[o.text for o in actual_poll.options]
    options=[o.text for o in actual_poll.options]
    correct_option_id=actual_poll.correct_option_id
    exp=actual_poll.explanation
    op=""
    for o in range(len(options)):
    	if o==correct_option_id:
        	op=op+"""
        item1.createChoice('"""+reaaa.sub("\n",r"\\n",reaaa.sub("(\"|\')","\\'",options[o]))+"""',true),"""
    	else:
        	op=op+"""
        item1.createChoice('"""+reaaa.sub("\n",r"\\n",reaaa.sub("(\"|\')","\\'",options[o]))+"""',false),"""
    
    data=data+"""   var item1 = form.addMultipleChoiceItem();
   item1.setTitle('"""+reaaa.sub("\n",r"\\n",reaaa.sub("(\"|\')","\\'",question))+"""')
     .setChoices(["""+op+"""
        ])"""
    data=data+"""
     .setPoints(1);
      
"""
    if exp is not None:
        data=data+"""
   item1.setFeedbackForIncorrect(FormApp.createFeedback().setText('"""+reaaa.sub("\n",r"\\n",reaaa.sub("(\"|\')","\\'","Ans : "+options[correct_option_id]+"\n\n"+exp))+"""').addLink('https://t.me/Polls_Quiz').build());
   item1.setFeedbackForCorrect(FormApp.createFeedback().setText('"""+reaaa.sub("\n",r"\\n",reaaa.sub("(\"|\')","\\'","Ans : "+options[correct_option_id]+"\n\n"+exp))+"""').addLink('https://t.me/Polls_Quiz').build());"""
    if exp is None:
        data=data+"""
   item1.setFeedbackForIncorrect(FormApp.createFeedback().setText('"""+reaaa.sub("\n",r"\\n",reaaa.sub("(\"|\')","\\'","Ans : "+options[correct_option_id])+"""').addLink('https://t.me/Polls_Quiz').build());
   item1.setFeedbackForCorrect(FormApp.createFeedback().setText('"""+reaaa.sub("\n",r"\\n",reaaa.sub("(\"|\')","\\'","Ans : "+options[correct_option_id])+"""').addLink('https://t.me/Polls_Quiz').build());
    
    context.bot.send_message(chat_id=update.message.chat.id,text="send me next Que or /done")
    return AA

def gft(update,context):
    
    text = reaaa.sub("\n",r"\\n",reaaa.sub("(\"|\')","\\'",update.message.text))
    
    global data
    x=data
    for y in reaaa.finditer("item1\.setTitle\(\'.*?\'\)",data):
    	yx=y.span()
    
    data=x[0:yx[0]]+'item1.setTitle(\''+reaaa.sub("\ {2}","\xa0 ",reaaa.sub("\n",r"\\n",reaaa.sub("(\"|\')","'",text)))+'\')'+x[yx[1]:-1]
    
    #context.bot.send_message(chat_id=update.message.chat.id,text=x)
    #data=reaaa.sub(x,text,data)
    return AA
    

def gfph(update,context):
	context.bot.send_message(chat_id=update.message.chat.id,text=str(update.message))

def done(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    try:
    	from google_form import main4
    	main4(data+"\n}")
    	update.message.reply_text(
        'https://script.google.com/home/projects/1mWCV-kS59FbRsalsaMRH_TvvAYJLWuAUUInWTzBYFgBYgSEEQhwxd8f1/edit', reply_markup=ReplyKeyboardRemove()
    )
    except Exception as e :
    	update.message.reply_text(str(e))
    	update.message.reply_text(str(data))
    	
    
    
    

    return ConversationHandler.END


def main() -> None:
    # Create the Updater and pass it your bot's token.
    bot_token=os.environ.get("BOT_TOKEN", "")
    #bot_token='1293606633:AAHuGiRGZpdvMOpichWNy4mmzhB0-BL5_V8'
    updater = Updater(bot_token,use_context=True)
    conv_handlerGF= ConversationHandler(
        entry_points=[CommandHandler('sq1', call8)],
        states={
        #POLLN: [MessageHandler(Filters.regex('^.*$') & ~Filters.command, pollfsend),],
            AA: [MessageHandler(Filters.poll, gfp),MessageHandler(Filters.text & ~ Filters.command, gft),],
            BB:[MessageHandler(Filters.regex('^.*$') & ~Filters.command, gfm)]
        },
        fallbacks=[CommandHandler('done', done)],
    )
    updater.dispatcher.add_handler(conv_handlerGF)
    updater.dispatcher.add_handler(MessageHandler(Filters.all & Filters.chat(username="jsjdkdkkd"), ghppp10))# Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    #dispatcher.
    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
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
            PHOTO: [MessageHandler(Filters.poll, photo), CommandHandler('skip', skip_photo),MessageHandler(Filters.text& ~Filters.command, location),],
            LOCATION: [
                MessageHandler(Filters.text& ~Filters.command, skip_location),
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
        entry_points=[CommandHandler('p', playinc)],
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
        entry_points=[CommandHandler('gggg8', uploadfile)],
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
    
    updater.dispatcher.add_handler(conv_handler01R1)
    updater.dispatcher.add_handler(conv_handler01R2)
    updater.dispatcher.add_handler(CommandHandler('add', call4))
    updater.dispatcher.add_handler(CommandHandler('startquiz', call3))
    updater.dispatcher.add_handler(CommandHandler('sq2', call7))
    #updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.photo, photos))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    dispatcher.add_handler(conv_handler01PDF)
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
    dp=dispatcher
    dp.add_handler(CommandHandler('downloadfile',downloadfile))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, poll))
    
    dp.add_handler(MessageHandler(Filters.poll, ghppp1))
    dp.add_handler(MessageHandler(Filters.document,doc_poll))
    dp.add_handler(CommandHandler('current', current))
    # Start the Bot
    updater.start_polling(clean = True)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()