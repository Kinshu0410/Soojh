from pyrogram import Client
from pyrogram.handlers import MessageHandler, PollHandler
from pyrogram import filters
from pyrogram.types import Message, ReplyKeyboardRemove, Poll
import re as reaaa

@app.on_message(filters.poll & filters.chat("Neha55bot") & ~filters.chat("Soojhboojh_01bot"))
async def start_(client:Client,message:Message):
	chatid=["Polls_Quiz"]
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



@app.on_message(filters.poll & filters.chat("POLLQZ") & ~filters.chat("Soojhboojh_01bot"))
async def start_command(client:Client,message:Message):
	chatid=["POLLQZ"]
	try:
	    mess=(await client.vote_poll(chat_id=message.chat.id, message_id=message.message_id,options=1))
	except:
	    mess=message.poll
	await app.delete_messages(chat_id="POLLQZ", message_ids=message.message_id)
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


#zaa=app.run()