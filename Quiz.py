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

LIST_OF_ADMINS1 = ["Kinbin247", "Harsh_Avasthi", "TOXIC_MAVI", "imKkala", "Om_2611","Gksgj", "ANKITAdidi", "Sharma_jii_ki_betii","yogeshogesh","Unacademy_Quizer", "JayBhim00"]

def restricted1(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        mid=update.message.message_id
        userName = update.message.chat.username
        #print(userName)
        userName1=update.message.from_user.username
        chatiid=int(update.message.chat.id)
        #print(chatiid)
        chatiid=int(update.message.chat.id)
        	
        
        
        
        if userName and userName1 not in LIST_OF_ADMINS1 or userName is None:
            
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

LIST_OF_ADMINS_D = ["Kinbin247", "Harsh_Avasthi", "TOXIC_MAVI"]
def restrictedD(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
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
    global db
    with open('Newfile.text') as json_file:
        db = json.load(json_file)
        new={'que':[], 'op':[], 'cor':[]}
        if Textstr not in list(db.keys()):
            db[Textstr]=new
        db[Textstr]['que'].append(user.question)
        db[Textstr]['op'].append([o.text for o in user.options])
        db[Textstr]['cor'].append(user.correct_option_id)
        ##print(db[Textstr])
        with open('Newfile.text', 'w') as outfile:
            json.dump(db, outfile)
    update.message.reply_text("Send me more polls or quiz using /skip")
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
    with open('Newfile.text') as json_file:
        db = json.load(json_file)
    dbA={}
    with open('Result.html', 'w') as outfile:
        json.dump(dbA, outfile)
    
        try:
            
            context.bot.send_message(chat_id=chatid, text="🎲 Get ready for the LIVE TEST \'"+Textstr0+"\'\n\n🖊 "+str(len(db[Textstr0]['que']))+" questions\n⏱ "+Time+" seconds per question\n📰 Votes are visible to group members only\nevery ✔︎ Question gain ✙4 Marks\nevery ✖︎ Question gain –1 Mark\n\n<b>At least 1 voting for last 3 questions far calculating Results.</b>", parse_mode=ParseMode.HTML)
            mes=context.bot.send_message(chat_id=chatid, text="Quiz is about to start")
            time.sleep(2)
            for xooo in range(6):
                if xooo!=5:
                    context.bot.editMessageText(chat_id=chatid, message_id=mes.message_id, text=str(5-xooo))
                    time.sleep(1)
                if xooo==5:
                    context.bot.editMessageText(chat_id=chatid, message_id=mes.message_id, text="Best Of Luck 👍👍👍")
                    time.sleep(1)
                    
                
                
            
            
            for X in range(len(db[Textstr0]['que'])):
                
                Zno=len(db[Textstr0]['que'])-X
                correct_option_id =db[Textstr0]['cor'][X],
                question=str(X+1)+". "+db[Textstr0]['que'][X]
                options=db[Textstr0]['op'][X]
                if X==0:
                    pass
                else:
                    pass
                    #time.sleep(int(Time))
                #print("1")
                message = context.bot.send_poll(
                    update.effective_chat.id,
                    question=str(Zno)+". "+db[Textstr0]['que'][X],
                    options=db[Textstr0]['op'][X],
                    # with is_closed true, the poll/quiz is immediately closed
                    type=Poll.QUIZ,
                    correct_option_id =db[Textstr0]['cor'][X],
                    open_period=int(Time),
                    #explanation=Ex,
                    is_closed=False,
                    is_anonymous=False,
                    reply_markup=ReplyKeyboardRemove(),
                )
                #print(update.effective_chat.id)
                time.sleep(int(Time))
                try:
                    #print("start")
                    payload = {
                        message.poll.id: {
                            "cor": question,
                            "options": options,
                            "cor":correct_option_id,
                            "message_id": message.message_id,
                            "chat_id": update.effective_chat.id,
                            "que_no":X+1
                        }
                    }
                    context.bot_data.update(payload)
                
                except Exception as e:
                    pass
            message = context.bot.send_poll(
                update.effective_chat.id,
                question="Must attempt Free Hit.",
                options=["Option", "Option", "Option", "Option"],
                # with is_closed true, the poll/quiz is immediately closed
                type=Poll.QUIZ,
                correct_option_id =3,
                open_period=int(Time)+5,
                explanation="No point in this quistion.\nIt was only for result count",
                is_closed=False,
                is_anonymous=False,
                reply_markup=ReplyKeyboardRemove(),
            )
            #print(update.effective_chat.id)
            time.sleep(int(Time)+5)
            try:
                #print("start")
                payload = {
                    message.poll.id: {
                        "cor": question,
                        "options": options,
                        "cor":correct_option_id,
                        "message_id": message.message_id,
                        "chat_id": update.effective_chat.id,
                        "que_no":X+2
                    }
                }
                context.bot_data.update(payload)
                
            except Exception as e:
                pass
                    #print(e)
                    
                    
                    #return QUIZ2
                
                
        
            
            
            

            
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
    #print("from user ="+str(user))
    global Textstr1
    userText=update.message.text
    Textstr1=userText
    with open('Newfile.text') as json_file:
        db = json.load(json_file)
        try:
            db.pop(Textstr1)
            with open('Newfile.text', 'w') as outfile:
                json.dump(db, outfile)
            update.message.reply_text("Quiz "+Textstr1+" deleted", reply_markup=ReplyKeyboardRemove(),)
            
        except:
            update.message.reply_text("Name not exist", reply_markup=ReplyKeyboardRemove(),)

    return ConversationHandler.END

@restricted
@run_async
def quizlist(update: Update, _: CallbackContext) -> int:
    #global Uid
    #Uid=update.message.user_id
    user = update.message.from_user
    with open('Newfile.text') as json_file:
        db = json.load(json_file)
        List=list(db.keys())
        for L in range(len(List)):
            update.message.reply_text(List[L])


#@run_async
@restricted1
@send_typing_action
def quizresult(update, context):
    global dbR
    chat__id=int(update.message.chat.id)
    if chat__id<=0:
    	try:
    		chat__id="@"+str(update.message.chat.username)#id
    	except Exception as e:
    		print(str(e))
    else:
    	pass
    
    
    COUNTJ=0
    with open('Newfile.text') as outfile:
          db = json.load(outfile)
    with open('Result.html') as outfile:
          dbR = json.load(outfile)
    try:
        if True:
            if True:
                try:
                    
                        #mess=context.bot.send_message(chat_id=chatid, text="👆👆👆 Must attempt for RESULT")
                        #print("message ==="+str(mess.message_id))
                        
                    
                    #print("correct options = "+str(corec))
                    List=list(dbR[Textstr0].keys())
                    P=len(List)
                    dbbb=[]
                    if True:
                        if True:
                            for L in range(P):
                                Rs=dbR[Textstr0][List[L]]['result'][0]
                                dbbb.append(int(Rs))
                            #print(dbbb)
                            yest=list(([int(i[0]) for i in sorted(enumerate(dbbb), key=lambda k: k[1], reverse=True)]))
                            #print(yest)
                            rnumb=1
                            try:
                                os.remove('Result.xlsx')
                            except:
                                print("removing")
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
                            for L in yest:
                                print("list")
                                Fname=dbR[Textstr0][List[L]]['fname']
                                
                                
                                Lname=dbR[Textstr0][List[L]]['lname']
                                Rname=dbR[Textstr0][List[L]]['✔︎']
                                
                                Wname=dbR[Textstr0][List[L]]['✖︎']
                                
                                Uname=dbR[Textstr0][List[L]]['uname']
                                Usid=dbR[Textstr0][List[L]]['usid']
                                ##print(Uname)
                                Rs=dbR[Textstr0][List[L]]['result'][0]
                                print("data loading start")
                                if Uname is not None:
                                	if COUNTJ<=9:
                                		COUNTR=COUNTR+""+str(COUNTJ+1)+". @"+str(Uname)+"\n"
                                		COUNTJ+=1
                                elif Lname is not None:
                                	if COUNTJ<=9:
                                		COUNTR=COUNTR+""+str(COUNTJ+1)+". "+Fname+" "+Lname+"\n"
                                		COUNTJ+=1
                                else:
                                	if COUNTJ<=9:
                                		COUNTR=COUNTR+""+str(COUNTJ+1)+". "+Fname+"\n"
                                		COUNTJ+=1
                                
                                
                                
                                worksheet.write('A'+str(rnumb+1), str(rnumb), cell_format)
                                if Lname is not None:
                                	worksheet.write_url('B'+str(rnumb+1), "tg://openmessage?user_id="+str(Usid), cell_format=cell_format, string=str(Fname)+" "+str(Lname))
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
                                print(COUNTR)
                                rnumb+=1
                            workbook.close()
                            print("webhook close")
                            
                                    
                            
                except Exception as e:
                    print("e===="+str(e))
                    context.bot.send_message(chat_id=chat__id, text="quiz not found")
        caption1="🏁 The quiz \'"+Textstr0+"\' has finished!\nCurrent Time = "+str(time.ctime(time.time() +19800))+" \n"+str(len(db[Textstr0]['que']))+" questions answered\n\n"+COUNTR+"\n🏆 Congratulations to the winners!"
        print(caption1)
        context.bot.send_document(chat__id, open('Result.xlsx', "rb"),caption=caption1)
    except Exception as e:
        context.bot.send_message(chat_id=chat__id, text="no live quiz at now come next time.\n error name = "+str(e))

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
    f = 'Newfile.text'
    #print("1")
    chat_id=update.effective_chat.id
    #print(chat_id)
    #with open(f, "rb") as file:
        #context.bot.send_document(chat_id, document=file)
     
        
    try:
        context.bot.send_document(chat_id, open(f, "rb"))#document=file)
    except Exception as e:
        pass
        #print(e)
    
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


Textstr0=""
#@run_async
def quizc(update,context):
    user = update.message.from_user
    global payload
    global Textstr0
    global J
    global chatid
    global Dbz
    global Mid
    Mid = []
    J=0
    Dbz=[]
    userText=update.message.text
    Textstr0=userText
    with open('Newfile.text') as json_file:
        db = json.load(json_file)
    dbA={}
    with open('Result.html', 'w') as outfile:
        json.dump(dbA, outfile)
    
        try:
            
            context.bot.send_message(chat_id=channelid, text="🎲 Get ready for the LIVE TEST \'"+Textstr0+"\'\n\n🖊 "+str(len(db[Textstr0]['que']))+" questions\n\n⏱ Voting Start "+str(time.ctime(time.time() +19800))+"\n\n⏱ Voting End "+str(time.ctime(time.time() + int(Time) +19800))+" \n\n📰 Votes are visible to group members and shared all polls \nevery ✔︎ Question gain ✙4 Marks\nevery ✖︎ Question gain –1 Mark\n\n<b>Result Comes on "+str(time.ctime(time.time() + int(Time)+19800))+"\n\nPlaying Group "+str(channelid)+"\n\nFor more #Soojh_Boojh</b>", parse_mode=ParseMode.HTML)
            mes=context.bot.send_message(chat_id=channelid, text="Quiz is about to start")
            time.sleep(2)
            for xooo in range(6):
                if xooo!=5:
                    context.bot.editMessageText(chat_id=channelid, message_id=mes.message_id, text=str(5-xooo))
                    time.sleep(1)
                if xooo==5:
                    context.bot.editMessageText(chat_id=channelid, message_id=mes.message_id, text="Best Of Luck 👍👍👍")
                    time.sleep(1)
                    
                
                
            
            
            for X in range(len(db[Textstr0]['que'])):
                Zno=len(db[Textstr0]['que'])-X
                
                correct_option_id =db[Textstr0]['cor'][X],
                question=str(X+1)+". "+db[Textstr0]['que'][X]
                options=db[Textstr0]['op'][X]
                if X==0:
                    pass
                else:
                    pass
                    #time.sleep(int(Time))
                #print("1")
                #print(update.effective_chat)
                try:
                        print("1")
                        message = context.bot.send_poll(
                            chat_id=channelid,
                            question=str(Zno)+". "+db[Textstr0]['que'][X],
                            options=db[Textstr0]['op'][X],
                            # with is_closed true, the poll/quiz is immediately closed
                            type=Poll.QUIZ,
                            correct_option_id =db[Textstr0]['cor'][X],
                            #open_period=int(Time),
                            #explanation=Ex,
                            is_closed=False,
                            is_anonymous=False,
                            reply_markup=ReplyKeyboardRemove(),    
                        )
                        print(5)
                        Dbz.append(message.poll.id)
                        Mid.append(message.message_id)
                        time.sleep(5)
                except Exception as e:
                        print("e===="+str(e))
                try:
                    #print("start")
                    payload = {
                        message.poll.id: {
                            "cor": question,
                            "options": options,
                            "cor":correct_option_id,
                            "message_id": message.message_id,
                            "chat_id": update.effective_chat.id,
                            "que_no":X+1
                        }
                    }
                    context.bot_data.update(payload)
                    chatid=channelid
                except Exception as e:
                    pass
            
                    
            
                
    

                
            
            

            
        except Exception as e:
            print("e========"+str(e))
            update.message.reply_text("Name not exist.", reply_markup=ReplyKeyboardRemove(),)
    
    #update.message.reply_text("/result")
    try:
        return ConversationHandler.END
    except Exception as e:
        pass
    #print(str(Dbz))
    



Dbz=[]
        
#time.sleep(1)
print("Sleeping for one sec")
#@run_async
def receive_poll_answer(update,context):
    global dbR
    global ree
    global J
    global mess
    #print("jdjdjdjxj")
    try:
        answe=update
        answer = update.poll_answer
        #print(str(answe))
        #time.sleep(3)
        poll_id = answer.poll_id
        ui=str(answer.user.id)
        #print("answer"+str(answer))
        #print("Dbz = "+str(Dbz))
        if poll_id in Dbz:
            try:
                
                corec = context.bot_data[poll_id]["cor"][0]
                Y= context.bot_data[poll_id]["que_no"]
                #print("Y"+str(Y))
                ##print("questions ======="+questions)
            # this means this poll answer update is from an old poll, we can't do our answering then
            except Exception as e:
                pass
                #print("Exception as "+str(e))
            
            #print("answer ======"+str(answer))
            with open('Result.html') as json_file:
                dbR = json.load(json_file)
            with open('Newfile.text') as json_file:
                db = json.load(json_file)
                
                ##print(dbR)
                
                #print(corec)
                XY=len(db[Textstr0]['que'])+1
                #print("XY="+str(XY))
                newA={'fname':answer.user.first_name, 'lname':answer.user.last_name, 'uname':answer.user.username,"usid":answer.user.id ,'so':answer.option_ids[0], 'result':[0], '✔︎':[0] ,'✖︎':[0]}
                if Textstr0 not in list(dbR.keys()):
                    dbR[Textstr0]={}
                if ui not in list(dbR[Textstr0].keys()):
                    dbR[Textstr0][ui]=newA
                dbname=dbR[Textstr0][ui]
                dbname['so']=answer.option_ids[0]
                if poll_id in Dbz:
                    if dbname['so']==corec:
                        dbname['✔︎'] = [x+1 for x in dbname['✔︎']]
                        dbname['result'] = [x+4 for x in dbname['result']]
                    else:
                        dbname['result'] = [x-1 for x in dbname['result']]
                        dbname['✖︎'] = [x+1 for x in dbname['✖︎']]
                ##print(str(dbR))
                with open('Result.html', 'w') as outfile:
                    json.dump(dbR, outfile)
                #print("bdR = "+str(dbR))
                

    except:
        print("fail")
        
            
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
    userText=update.message.text
    Time1=userText
    Time1=reaaa.sub("(https|http)://t\.me/", "@", Time1)
    context.bot.send_message(chat_id=chat0id, text="Send me message.")
    return GHN

@run_async
def ghn(update,context):
    userText=update.message.text
    try:
	    if reaaa.match(r"^\d{1,}$",userText):
	    	context.bot.delete_message(chat_id=Time1,message_id=int(userText))
	    else:
	    	context.bot.send_message(chat_id=Time1, text=userText)
    except Exception as e:
    	context.bot.send_message(chat_id=Time1, text="Error Name = "+str(e))
    return GHN
    
#@run_async
def ghn1(update,context):
    userText=update.message.poll
    que=userText.question
    options=[o.text for o in userText.options]
    co=userText.correct_option_id
    explan=userText.explanation
    try:
    	context.bot.send_poll(
    		chat_id=Time1,
    		question=que,
    		options=options,
            type=Poll.QUIZ,
            correct_option_id=co,
            explanation=explan,
            is_anonymous=False,
            allows_multiple_answers=False,
        )
    except Exception as e:
    	print(str(e))
    return GHN


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
        result = reaaa.match("[-+]?\d+$", corr)
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

POLLF=range(1)

@restricted1
@send_typing_action
def pollf(update,context):
    chat___id=int(update.message.chat.id)
    if chat___id<=0:
    	try:
    		chat___id="@"+str(update.message.chat.username)#id
    	except Exception as e:
    		print(str(e))
    else:
    	pass
    context.bot.send_message(chat_id=chat___id, text="Send me group link")
    return POLLF
    
def pollfsend(update,context):
    global Time3
    global Tco
    global db
    userText=update.message.text
    Time3=userText
    ChanId=reaaa.sub(r"(https|http)://t\.me/", "@", Time3)
    try:
    	with open('Newfile.text') as json_file:
    		db = json.load(json_file)
    	context.bot.send_message(chat_id=ChanId, text="🎲 Get ready for the LIVE TEST \'"+Textstr0+"\'\n\n🖊 "+str(len(db[Textstr0]['que']))+" questions\n\n⏱ Voting Start "+str(time.ctime(time.time() +19800))+" \n\n📰 Votes are visible to group members and shared all polls \nevery ✔︎ Question gain ✙4 Marks\nevery ✖︎ Question gain –1 Mark\n\n<b>Playing Group "+str(ChanId)+"\n\nFor more #Soojh_Boojh</b>", parse_mode=ParseMode.HTML)
    	for d in range(len(Mid)):
    		context.bot.forward_message(chat_id=ChanId,from_chat_id=channelid, message_id=Mid[d])
    		if d%4==2:
    			time.sleep(5)
    except Exception as e:
    	print(str(e))
    return POLLF



def main() -> None:
    # Create the Updater and pass it your bot's token.
    bot_token=os.environ.get("BOT_TOKEN", "")
    #bot_token='1458427559:AAFDcDNOg6VfK6Gscrf7hhS6eciKr2Q_nT0'
    updater = Updater(bot_token,use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler01F= ConversationHandler(
        entry_points=[CommandHandler('pollf', pollf)],
        states={
            POLLF: [MessageHandler(Filters.regex('^.*$') & ~Filters.command, pollfsend),],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
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
            GHN: [MessageHandler(Filters.text & ~Filters.command & ~Filters.regex(r'^((https|http).*|@.*)$'), ghn), MessageHandler(Filters.regex(r'^((https|http).*|@.*)$'), time1c),MessageHandler(Filters.poll,  ghn1)],
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


    dispatcher.add_handler(CommandHandler('quizresult',quizresult))
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

