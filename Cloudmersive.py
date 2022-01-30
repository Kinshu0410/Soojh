#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymongo import MongoClient
import dns

'''import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] # this is a google public dns server,  use whatever dns server you like here
# as a test, dns.resolver.query('www.google.com') should return an answer, not an exception'''
clientmongo=MongoClient('mongodb+srv://Kinshu04101:Qwert123@cluster0.ckcyx.mongodb.net/test?retryWrites=true&w=majority')

from pyrogram import Client
from pyrogram.handlers import MessageHandler, PollHandler
from pyrogram import filters
from pyrogram.types import Message, ReplyKeyboardRemove, Poll
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import  json
import time
import re as reaaa

app = Client("my_account",
#bot_token=ClientText["bot_token"],
api_id="13682659",
api_hash="b984d240c5258407ea911f042c9d75f6")
scheduler = AsyncIOScheduler(timezone="Asia/kolkata")
@app.on_message(filters.regex("^Cid") )#& filters.incoming)
async def cyid(client:Client,message:Message):
	await app.send_message(message.chat.id,str(message.chat.id))  

scheduler.start()
@app.on_message(filters.regex("The quiz") )#& filters.incoming)
async def job2_partener(client:Client,message:Message):
	if message.reply_markup:
		if message.reply_markup["inline_keyboard"][0][0].text=="Share quiz":
			name= clientmongo["group_schedule"].list_collection_names()
			now=""
			if str(message.chat.id) in name:
			    #print(message)
			    col=clientmongo["group_schedule"][str(message.chat.id)]
			    Nu=col.find_one({"Nu":{"$type":"array"}})["Nu"]
			    hour1=col.find_one({"Time":{"$type":"string"}})["Time"]
			    hour=reaaa.split(",",reaaa.sub(" ","",hour1))
			    current_time=int(time.ctime(time.time() +19800)[11:13])
			    for x in hour:
			        if current_time<int(x):
			            now=str(x)
			            break
			    if now:
			        now=now
			    else:
			        now=str(hour[0])
			    if int(now)>=13:
			        now=str(int(now)-12)+" PM"
			    else:
			        now=now+" AM"
			    await app.send_message(int(message.chat.id)," NEXT QUIZ at "+now+"\n\n"+ col.find_one({"data":{"$type":"array"}})["data"][Nu[0]][list(col.find_one({"data":{"$type":"array"}})["data"][Nu[0]].keys())[0]],disable_web_page_preview=True)
			name= clientmongo["group_schedule"].list_collection_names()
			for x in name:
				try:
					hour1=clientmongo["group_schedule"][str(x)].find_one({"Time":{"$type":"string"}})["Time"]
					print(str(x)+"=====Time====="+hour1)
					hour=reaaa.split(",",hour1)
					zz=""
					for y in range(len(hour)):
					    zz=zz+str(int(hour[y])-1)+","
					print(scheduler.add_job(job2, "cron",hour=zz[:-1], minute='58',replace_existing=True,args=(x,client,message,) ,id="job2"+str(x)))
					print(scheduler.add_job(job1, "cron", hour=hour1,replace_existing=True,args=(x,client,message,) ,id="job1"+str(x)))
					print("गूढ़")
				except Exception as e:
					print("गूढ़"+str(e))
	        
@app.on_message(filters.regex("schedule_start") )#& filters.incoming)
async def schedule_job(client:Client,message:Message):
	name= clientmongo["group_schedule"].list_collection_names()
	for x in name:
		try:
			hour1=clientmongo["group_schedule"][str(x)].find_one({"Time":{"$type":"string"}})["Time"]
			print(str(x)+"=====Time====="+hour1)
			hour=reaaa.split(",",hour1)
			zz=""
			for y in range(len(hour)):
			    zz=zz+str(int(hour[y])-1)+","
			print(scheduler.add_job(job2, "cron",hour=zz[:-1], minute='58',replace_existing=True,args=(x,client,message,) ,id="job2"+str(x)))
			print(scheduler.add_job(job1, "cron", hour=hour1,replace_existing=True,args=(x,client,message,) ,id="job1"+str(x)))
			print("गूढ़ schedule done")
		except Exception as e:
			print("गूढ़ schedule"+str(e))
					
	await app.send_message(int(message.chat.id),"Schedule update")
	scheduler.start()

@app.on_message(filters.regex("^Set time.*?") )#& filters.incoming)
async def setting_time(client:Client,message:Message):
	col=clientmongo["group_schedule"][str(message.chat.id)]
	cid=[]
	for member in await app.get_chat_members(message.chat.id, filter="administrators"):
		cid.append(member.user.id)
	#print(str(cid))
	if message.from_user.id in cid:
		myquery1 = {"Time":{"$type":"string"}}
		if col.find_one(myquery1):
			newvalues1= { "$set": {"Time":reaaa.sub("^Set time","",message.text)}}
			col.update_one(myquery1,newvalues1)
		else:
			col.insert_one({"Time":reaaa.sub("^Set time","",message.text)})
		
		await app.send_message(int(message.chat.id),"Schedule Reset")
	
async def job1(x,client:Client,message:Message):
	col=clientmongo["group_schedule"][str(x)]
	myquery1 = {"Nu":{"$type":"array"}}
	if col.find_one(myquery1):
		Nu=col.find_one(myquery1)["Nu"]
		if len(col.find_one({"data":{"$type":"array"}})["data"])==int(Nu[0]+1):
			Nu1=[0]
		else :
			Nu1=[int(Nu[0])+1]
		newvalues1 = { "$set": { "Nu":Nu1} }
		col.update_one(myquery1,newvalues1)
		try:
			mass_id=await app.send_message(int(x),"/start@quizbot "+ list(col.find_one({"data":{"$type":"array"}})["data"][Nu[0]].keys())[0])
			time.sleep(5)
			await client.request_callback_answer(chat_id=message.chat.id,message_id=mass_id.message_id+1,callback_data='{"a":"user_ready"}')
		except Exception as e:
			print("def job1 in cloudmersiver error name = "+str(e))


async def job2(x,client:Client,message:Message):
	#print(str(x))
	col=clientmongo["group_schedule"][str(x)]
	myquery1 = {"Nu":{"$type":"array"}}
	Nu=col.find_one(myquery1)["Nu"]
	now=""
	try:
		if int(time.ctime(time.time() +19800)[11:13])+1>=13:
			now=str(int(time.ctime(time.time() +19800)[11:13])+1-12)+" PM"
		else:
			now=str(int(time.ctime(time.time() +19800)[11:13])+1)+" AM"
		await app.send_message(int(x)," NEXT QUIZ play in 2 Minutes\n\n"+ col.find_one({"data":{"$type":"array"}})["data"][Nu[0]][list(col.find_one({"data":{"$type":"array"}})["data"][Nu[0]].keys())[0]],disable_web_page_preview=True)
		mass=await app.send_message(message.chat.id, "0:1:50")
		print(scheduler.add_job(job3, "interval", seconds=10,replace_existing=True,args=(x,mass,client,message,) ,id="job3"+str(x)))
	except Exception as e:
		print("def job2 in cloudmersiver error name = "+str(e))

async def job3(x,mass,client:Client,message:Message):
		
		mess1=await app.get_messages(x, mass.message_id)
		
		timer=reaaa.split(":",mess1.text)
		total=int(timer[0])*3600+int(timer[1])*60+int(timer[2])
		try:
			if total//10>=1:
				text=str((total-10)//3600)+":"+str((total-10)//60-((total-10)//3600)*60)+":"+str((total-10)-((total-10)//60-((total-10)//3600)*60)*60-((total-10)//3600)*3600)
				#mass=str((total-1-x*5)//3600)+":"+str((total-1-x*5)//60-((total-1-x*5)//3600)*60)+":"+str((total-1-x*5)-((total-1-x*5)//60-((total-1-x*5)//3600)*60)*60-((total-1-x*5)//3600)*3600)
				await app.edit_message_text(message.chat.id, mess1.message_id,text)
				
			else:
				await app.edit_message_text(message.chat.id, message.message_id,"Quiz is about to Play")
				scheduler.shutdown(id="job3"+str(x))  
				
		except:
			await app.edit_message_text(message.chat.id, message.message_id,"Some error comes...")
			scheduler.shutdown(id="job3"+str(x)) 
			
			
@app.on_message(filters.regex("^Del_ .*?") )#& filters.incoming)
async def dell(client:Client,message:Message):
	col=clientmongo["group_schedule"][str(message.chat.id)]
	myquery1 = {"data":{"$type":"array"}}
	if col.find_one(myquery1):
		data=col.find_one(myquery1)["data"]
		for i in data.copy():
			if i.get(reaaa.sub("^Del_ ","",message.text)):
				data.remove(i)
		newvalues1 = { "$set": { "data":data}} 
		col.update_one(myquery1,newvalues1)
		await app.send_message(message.chat.id, "Quiz Delete to schedule is successful.") 
	else:
		await app.send_message(message.chat.id, "Did not find quiz") 
	if len(col.find_one(myquery1)["data"])==0:
		print("drop Quiz "+str(message.chat.id)+".      "+str(len(col.find_one(myquery1)["data"])))
		col.drop()
	
@app.on_message(filters.text & filters.chat("POLLQZ") )#& filters.incoming)
async def forword(client:Client,message:Message):
    if message.reply_markup:
        await app.send_message("quizbot", message.reply_markup["inline_keyboard"][0][0].url)
@app.on_message(filters.regex("^Del_All$") & ~ filters.poll)#& filters.incoming)
async def delete_all_quiz(client:Client,message:Message):
	cid=[]
	for member in await app.get_chat_members(message.chat.id, filter="administrators"):
		cid.append(member.user.id)
	#print(cid)
	try:
		if int(message.from_user.id)  in  cid and str(message.chat.id) in clientmongo["group_schedule"].list_collection_names():
			col=clientmongo["group_schedule"][str(message.chat.id)].find_one_and_delete({"data":{"$type":"array"}})
			print("डिलीटेड")
			col=clientmongo["group_schedule"][str(message.chat.id)].find_one_and_delete({"Nu":{"$type":"array"}})
			print("डिलीटेड")
			
			await app.send_message(message.chat.id, 'Delete All sucessful \n अब और quiz add कीजिये')
	except:
		await app.send_message(message.chat.id, 'कोई भी क्विज नही पायी गयीं जिसे delete किया जिसके🙏🙏🙏')
@app.on_message(filters.regex("^Stop$") & ~ filters.poll)#& filters.incoming)
async def stop_quiz(client:Client,message:Message):
	cid=[]
	for member in await app.get_chat_members(message.chat.id, filter="administrators"):
		cid.append(member.user.id)
	#print(cid)
	try:
		if int(message.from_user.id)  in  cid and str(message.chat.id) in clientmongo["group_schedule"].list_collection_names():
			print("स्टॉप")
			await app.send_message(message.chat.id, '/stop@QuizBot')
	except:
		pass

@app.on_message(filters.regex("yooo") & ~ filters.poll)#& filters.incoming)
async def forworhd(client:Client,message:Message):
	
	print(await app.get_messages(-1001495791558, 11048))
	await client.request_callback_answer(-1001495791558,11048,callback_data='{"a":"user_ready"}')
	#await app.send_message("me", str(message.reply_markup["inline_keyboard"][0][0].callback_data))
	
	
	#if hasattr(message, 'reply_markup'):
		#if message.chat.id==-1001495791558:
			#print(message)#if hasattr(message, 'from_user'):
			#if hasattr(message.from_user, 'id'):
				#if str(message.from_user.id)=='983000232':
					
		#if message.reply_markup["inline_keyboard"][0][0].callback_data=='{"a":"user_ready"}':
		    #cid= clientmongo["group_schedule"].list_collection_names()
		    #cid.append('983000232')
	        
		    #if str(message.chat.id) in cid:
		        #await client.request_callback_answer(chat_id=message.chat.id,message_id=message.message_id,callback_data=message.reply_markup["inline_keyboard"][0][0].callback_data)

@app.on_message(filters.poll & filters.chat("Neha55bot") )#& filters.incoming)
async def forwortd(client:Client,message:Message):
	chatid=["Study_Quiz_India", "polls_quiz"]
	
	#print(message.message_id)
	try:
		
	    mess=(await client.vote_poll(chat_id=message.chat.id, message_id=message.message_id,options=1))
	except:
	    mess=message.poll
	#print(mess)
	    #print(mess)
	await app.delete_messages(chat_id="Neha55bot", message_ids=message.message_id)
	question=mess.question
	
	#question=reaaa.sub("\n","       ",question)
	question=reaaa.sub(r"((@|#)([0-9A-Za-z\-\_\.])*(\s|\n{1,}|))|((\n| |){1,}(Join|🔜)(\n| |)){1,}", "", question)
	print("que se aage gye")
	question=reaaa.sub(r"(http|ftp|https|t\.me|tg):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", "", question)
	#question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}|)", "", question)
	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}(\d{1,}\. |\d{1,}\.)", "", question)
	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	question=reaaa.sub(r"^(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	
	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)", "", question)
	question=reaaa.sub(r"🔰 C.A BY 🔰", "", question)
	question=reaaa.sub(r"🔰", "", question)
	
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
	    mess=(await app.send_poll(chat_id=x,question=question,options=options,correct_option_id =correct_option_id,is_anonymous=True,type="quiz"))
	    #print(mess)
	    #await app.stop_poll(chat_id=x,message_id=mess.message_id)


	
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
	
	#question=reaaa.sub("\n","       ",question)
	question=reaaa.sub(r"((@|#)([0-9A-Za-z\-\_\.])*(\s|\n{1,}|))|((\n| |){1,}(Join|🔜)(\n| |)){1,}", "", question)
	print("que se aage gye")
	question=reaaa.sub(r"(http|ftp|https|t\.me|tg):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", "", question)
	#question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}|)", "", question)
	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}(\d{1,}\. |\d{1,}\.)", "", question)
	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	question=reaaa.sub(r"^(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	
	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)", "", question)
	question=reaaa.sub(r"(\n| |){1,}(🔰|C\.A BY)(\n| |){1,}", "", question)
	question=reaaa.sub(r"🔰", "", question)
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

@app.on_message(filters.poll & filters.chat("Pdf2imgbot") )#& filters.incoming)
async def Biology(client:Client,message:Message):
	chatid=["Biology_Quiz4U"]
	
	#print(message.message_id)
	try:
		
	    mess=(await client.vote_poll(chat_id=message.chat.id, message_id=message.message_id,options=1))
	except:
	    mess=message.poll
	#print(mess)
	    #print(mess)
	await app.delete_messages(chat_id="Neha55bot", message_ids=message.message_id)
	question=mess.question
	
	#question=reaaa.sub("\n","       ",question)
	question=reaaa.sub(r"((@|#)([0-9A-Za-z\-\_\.])*(\s|\n{1,}|))|((\n| |){1,}(Join|🔜)(\n| |)){1,}", "", question)
	print("que se aage gye")
	question=reaaa.sub(r"(http|ftp|https|t\.me|tg):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", "", question)
	#question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}|)", "", question)
	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}(\d{1,}\. |\d{1,}\.)", "", question)
	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	question=reaaa.sub(r"^(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	
	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)", "", question)
	question=reaaa.sub(r"🔰 C.A BY 🔰", "", question)
	question=reaaa.sub(r"🔰", "", question)
	
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
	    mess=(await app.send_poll(chat_id=x,question=question,options=options,correct_option_id =correct_option_id,is_anonymous=True,type="quiz"))
	    #print(mess)
	    #await app.stop_poll(chat_id=x,message_id=mess.message_id)

	
def emojicut(que:str):
	emoji="😀😃😄😁😆😅😂🤣🥲☺️😊😇🙂🙃😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🥸🤩🥳😏😒😞😔😟😕🙁☹️😣😖😫😩🥺😢😭😤😠😡🤬🤯😳🥵🥶😶‍🌫😱😨😰😥😓🤗🤔🤭🤫🤥😶😐😑😬😴🥱😲😮😧😦😯🙄🤤😪😮‍💨😵😵‍💫🤐🥴🤢😈🤠🤑🤕🤒😷🤧🤮👿👹👺🤡👻💩💀☠😻😹😸😺🎃🤖👾👽😼😽🙀😿😾🤲👐🙌👏🤝👍👎👊✊🤛🤜🤞✌️🤟🤘👌🤌🤏👈🖖🖐🤚✋☝️👇👆👉👋🤙💪🦾🖕✍🙏🦶👂👅🦷👄💋💄🦿🦵🦻👃👣👁👀🫀🫁🧠👦🧒👧👶🫂👥👤🗣👩🧑👨👩‍🦱🧑‍🦱👨‍🦱👩‍🦰🧑‍🦰👩‍🦲👨‍🦳🧑‍🦳👩‍🦳👱‍♂👱👱‍♀👨‍🦰🧑‍🦲👨‍🦲🧔‍♀🧔🧔‍♂👵🧓👴👮‍♂👮👮‍♀🧕👳‍♂👳👳‍♀👲👷‍♀👷👷‍♂💂‍♀💂💂‍♂🕵‍♀🕵👩‍🍳👨‍🌾🧑‍🌾👩‍🌾👨‍⚕🧑‍⚕👩‍⚕🕵‍♂🧑‍🍳👨‍🍳👩‍🎓🧑‍🎓👨‍🎓👩‍🎤🧑‍🎤👨‍🎤🧑‍💻👩‍💻👨‍🏭🧑‍🏭👩‍🏭👨‍🏫🧑‍🏫👩‍🏫👨‍💻👩‍💼🧑‍💼👨‍💼👩‍🔧🧑‍🔧👨‍🔧👩‍🔬🧑‍🔬👨‍🔬👩‍🎨🧑‍🎨👨‍🎨👩‍🚒🧑‍🚒👨‍🚒🧑‍⚖👩‍⚖👨‍🚀🧑‍🚀👩‍🚀👨‍✈️🧑‍✈️👩‍✈️👨‍⚖👰‍♀👰👰‍♂🤵‍♀🤵🤵‍♂👸🦹‍♂🦹🦹‍♀🦸‍♂🦸🦸‍♀🥷🤴🤶🧑‍🎄🎅🧙‍♀🧙🧙‍♂🧝‍♀🧝🧞‍♀🧟‍♂🧟🧟‍♀🧛‍♂🧛🧛‍♀🧝‍♂🧞🧞‍♂🧜‍♀🧜🧜‍♂🧚‍♀🧚🧚‍♂👼🤰🤱👩‍🍼🧑‍🍼👨‍🍼🙇‍♀🙇🙆‍♀🙅‍♂🙅🙅‍♀💁‍♂💁💁‍♀🙇‍♂🙆??‍♂🙋‍♀🙋🙋‍♂??‍♀🧏🧏‍♂🙎🙎‍♀🤷‍♂🤷??‍♀🤦‍♂🤦🤦‍♀🙎‍♂🙍‍♀🙍🙍‍♂💇‍♀💇💇‍♂💆‍♀💃🤳💅🧖‍♂🧖🧖‍♀??‍♂💆🕺👯‍♀👯👯‍♂🕴👩‍??🧑‍🦽👨‍🦽🧑‍🦯👩‍🦯🚶‍♂🚶🚶‍♀👨‍🦼🧑‍🦼👩‍🦼👨‍🦯🧎‍♀🧎🧎‍♂🏃‍♀🏃🏃‍♂🧍‍♀💑👩‍❤️‍👩??‍❤️‍👨👬👭👫🧍‍♂🧍👨‍❤️‍👨👩‍❤️‍💋‍👨👩‍❤️‍💋‍👩💏👨‍❤️‍💋‍👨👨‍👩‍👦👨‍👩‍👧👨‍👩‍👧‍👦👨‍👨‍👦👩‍👩‍👧‍👧👩‍👩‍👦‍👦👩‍👩‍👧‍👦👩‍👩‍👧👩‍👩‍👦👨‍👩‍👧‍👧👨‍👩‍👦‍👦👨‍👨‍👧👨‍👨‍👧‍👦👨‍👨‍👦‍👦👨‍👨‍👧‍👧👩‍👦👩‍👧👩‍👧‍👦👩‍👦‍👦🧶🪢👨‍👧‍👧👨‍👦‍👦👨‍👧‍👦👨‍👧👨‍👦👩‍??‍👧🧵🪡🧥🥼🦺👚👕👖🥻👘🩱👙👗👔🩳🩲🩴🥿👠👡👢👞👟🥾⛑🎓👒🧢🎩🧣🧤🧦🪖👑💍👝👛👜💼🎒🌂🥽🕶👓🧳🐶🐱🐭🐹🐰🦊🐻🐼🐸🐽🐷🐮🦁🐯🐨🐻‍❄️🐵🙈🙉🙊🐒🐔🐧🐦🐺🦇🦉🦅🦆🐥🐣🐤🐗🐴🦄🐝🪱🐛🦋🐌🕷🦗🦟🪳🪲🪰🐜🐞🕸🦂🐢🐍🦎🦖🦕🐙🐬🐟🐠🐡🦀🦞🦐🦑🐳🐋🦈🦭🐊🐅🐆🦓🐫🐪🦏🦛🐘🦣🦧🦍🦒🦘🦬🐃🐂🐄🐎🐖🦮🐩🐕🦌🐐🦙🐑🐏??‍🦺🐈🐈‍⬛️??🐓??🦤🦚🦡🦨🦝🐇🕊🦩🦢🦜🦫🦦🦥🐀🐁🐿🦔🐾🪵🌴🌳🌲🎄🌵🐲🐉🌱🌿☘🍀🎍🪴🎋🍃🌷💐🌾🪨🐚🍄🍁🍂🌹🥀🌺🌸🌼🌻🌞🌝🌑🌘🌗🌖🌕🌚🌜🌛🌒🌓🌔🌙🌎🌍🌏🪐🔥💥☄⚡️✨🌟⭐️💫🌪🌈☀️🌤⛅️🌥☁️🌦🌬⛄️☃️❄️🌨🌩⛈🌧💨💧💦☔️☂🌊🌫🍇🍉🍌🍋🍊🍐🍎🍏🍓🫐🍈🍒🍑🥭🍍🥥🌶🥒🥬🥦🥑🍆🍅🥝🫑🌽🥕🫒🧄🧅🥔🍠🍳🧀🥨🥖🍞🥯🥐🧈🥞🧇🥓🥩🍖🍗🦴🧆🥙🥪🫓🍕🍟🍔🌭🌮🌯🫔🥗🥘🫕🥫🍝🍤🦪🥟🍱🍣🍛🍲🍜🍙🍚🍘🍥🥠🥮🍢🍡🍮🎂🍰🧁🥧🍦🍨🍧🍭🍬🍫🍿🍩🍪🌰🥜🥤🧃🍵☕️🫖🍼🥛🍯🧋🍶🍺🍻🥂🍷🥃🍸🥣🍽🍴🥄🧊🍾🧉🍹🥡🥢🧂⚽️🏀🏈⚾️🥎🎾🏐🏉🥍🏑🏒🏸🏓🪀🎱🥏🏏🪃🥅⛳️🪁🏹🎣🤿🥌⛸🛷🛼🛹🎽🥋🥊🎿⛷🏂🪂🏋‍♀🏋🏋‍♂🤼‍♀⛹‍♂⛹⛹‍♀🤸‍♂🤸🤸‍♀🤼‍♂🤼🤺🤾‍♀🤾🤾‍♂🏌‍♀🏌🏌‍♂🏇🏊🏊‍♀🏄‍♂🏄🏄‍♀🧘‍♂??🧘‍♀🧗‍♀🚣‍♂🚣🚣‍♀🤽‍♂🤽🤽‍♀🏊‍♂🚴‍♂🚴🚴‍♀🚵‍♂🚵🚵‍♀🧗‍♂🧗🎗🎖🏅🥉🥈🥇🏆🩰🤹‍♂🤹🤹‍♀🎪🎟🎫🪘🎹🎼🎧🎤🎬🎨♟🎻🪕🎸🪗🎺🎷🧩🎰🎮🎳🎯🚑🏎🚎🚌🚙🚕🚗🦽🦯🚜🚛🚚🛻🚐🚒🚔🛺🏍🛵🚲🛴🦼🚋🚃🚟🚠🚡🚖🚘🚍🚇🚆🚂🚈🚅🚄🚝🚞🛰💺🛩🛬🛫✈️🚉🚊🛳🛥🚤⛵️🛶🚁🛸🚀🚥🚦🚧⛽️🪝⚓️🚢⛴🏟🏯🏰🗼🗿🗺🚏🏜🏖⛱⛲️🎠🎢🎡🏠🛖⛺️🏕🗻🏔⛰🌋🏣🏬🏢🏭🏗🏚🏘🏡💒🏫🏪🏨🏦🏥🏤🛤🕋🛕🕍🕌⛪️🏛🎇🌄🌅🏞🎑🗾🛣🌁🌉🌌🌃🏙🌆🌇🎆🖱🖥⌨💻📲📱⌚️📼💿💾💽🗜🕹🖲☎️📞🎞📽🎥📹📸📷🧭🎚🎙📻📠📟🔋⏳⌛️🕰⏰⏲💸🧯🪔🕯🔦💡🔌💎💰🪙💷💶💴💵🛠🔨🔧🪛🧰🪜⚖🧲🧱🪤⚙🔩🪚⛏🛡🗡🔪🪓🧨💣🔫🧿🔮🏺⚱🪦🚬💊🩺🕳🩹🔬🔭⚗💈🧹🧪🦠🧬🩸🛀🚿🚽????🔑🧴🪣🧽🪒🪥🧼??🛌🛋🚪🎏🎁🛒🛍🪟🪞🖼🎐🎎??🎊??🪄🎀📤💌📧📨✉️🧧📮📬📫📪🪧🏷📦📈🧾📑📄📃📜🗃🗑📅📆🗓🗒📉📰🗂📂📁📋🗄🗳📚📙📘📗📕📒📔📓📏🖇📎🧷🔖🖌🖋🖊✂️📍🧮🔒🔏🔎✏️📝🔓❤️💛💙💜💓🤎❤️‍🔥❤️‍🩹❣💞💗💘💟✝☮☪🕉✡🕎☯☦🛐⛎♉️♊️♌️♍️♏️♐️♒️♓️🆔🉑☢📴📳🈚️🈸🈺🈷🆚🉐㊙️🈴🅾🆑🅱🈲🈵🆘⭕️🛑📛💯🔞🚳🚷♨️🚭❗️❓❕❔⁉️‼️🔅♻️⚜🔱🚸⚠️〽️🔆✅💹✳️🌐🛗♿️Ⓜ️💤🚺🛅🈳🛂🔣📶🚮⚧🚼🎦ℹ️🔡🔠🆖🆗🆙🆒5⃣4⃣3⃣2⃣0⃣🆓🆕6⃣7⃣8⃣9⃣🔟🔢#⃣*⃣⏮⏺⏹⏯⏸▶️⏏️⏩⏪⏫⏬◀️🔼🔽➡️↕️↖️↙️↘️↗️⬇️⬆️⬅️↔️↪️↩️⤴️⤵️🔀🔁🔂✖️➗➖➕🎶🎵🔃🔄♾💲💱™©®👁‍🗨🔚✔️➿➰〰🔜🔝🔛🔙☑️🔘🔴🟠🟡🟢🔵🟣🔶🔹🔸🔻🔺🟤⚪️⚫️🔷🔲▪️▫️◾️◽️◼️⬛️🟪🟦🟩🟨🟧🟥◻️⬜️🟫🔈🔇🔉🔊🔔🔕♥️♣️♠️💭💬📢📣♦️🃏🎴🀄️🕐🕑🕒🕓🕛🕙🕘🕗🕖🕕🕔🕜🕝🕞🕟🕡🕣🕤🕦🕧🏳🏴🏴‍☠🏁🚩🏳‍🌈🏳‍⚧🇺🇳🇦🇮🇦🇴🇦🇩🇦🇸🇩🇿🇦🇱🇦🇽🇦🇫🇦🇶🇦🇬🇦🇷🇦🇲🇦🇼🇦🇺🇦🇹🇦🇿🇧🇯🇧🇿🇧🇪🇧🇾🇧🇧🇧🇩🇧🇭🇧🇸🇧🇲🇧🇹🇧🇴🇧🇦🇧🇼🇧🇷🇻🇬🇧🇳🇨🇻🇮🇨🇨🇦🇨🇲🇰🇭🇧🇮🇧🇫🇧🇬🇧🇶🇰🇾🇨🇫🇹🇩🇮🇴🇨🇱🇨🇳🇨🇽🇨🇮🇨🇷🇨🇰🇨🇩🇨🇬🇰🇲🇨🇴🇨🇨🇭🇷🇨🇺🇨🇼🇨🇾🇨🇿🇩🇰🇩🇯🇩🇲🇸🇿🇪🇪🇪🇷🇬🇶🇸🇻🇪🇬🇪🇨🇩🇴🇪🇹🇪🇺🇫🇰🇫🇴🇫🇯🇫🇮🇫🇷🇬🇫🇬🇮🇬🇭🇩🇪🇬🇪🇬🇲🇬🇦🇹🇫🇵🇫🇬🇷🇬🇱🇬🇩🇬🇵🇬🇺🇬🇹🇬🇬🇬🇳🇮🇳🇯🇲🇽🇰🇮🇸🇮🇹🇰🇮🇭🇺🇰🇪🇭🇰🇮🇲🇰🇿🇭🇳🇭🇹🇬🇾🇬🇼🇮🇩🇮🇷🇮🇶🇮🇪🇯🇴🇯🇪🎌🇱🇮🇰🇼🇰🇬🇱🇦🇱🇻🇱🇧🇱🇸🇲🇻🇲🇼🇲🇴🇱🇹🇲🇱🇲🇭🇲🇶🇲🇷🇲🇺🇾🇹🇲🇽🇲🇿🇲🇦🇲🇸🇲🇪🇲🇳🇲🇨🇲🇩🇫🇲🇲🇲🇳🇦🇳🇷🇳🇵🇳🇱🇳🇨🇳🇿🇳🇮🇳🇴🇲🇵🇲🇰🇰🇵🇳🇫🇳🇺🇳🇬🇳🇪🇴🇲🇵🇰🇵🇼🇵🇸🇵🇦🇵🇬🇵🇾🇵🇪🇷🇴🇷🇪🇶🇦🇵🇷🇵🇹🇵🇱🇵🇳🇵🇭🇷🇺🇷🇼🇼🇸🇸🇲🇸🇹🇸🇦🇸🇳🇷🇸🇸🇧🇬🇸🇸🇮🇸🇰🇸🇽🇸🇬🇸🇱🇸🇨🇸🇴🇿🇦🇰🇷🇸🇸🇪🇸🇱🇰🇧🇱🇸🇭🇨🇭🇸🇷🇸🇩🇻🇨🇵🇲🇱🇨🇰🇳🇸🇾🇹🇼🇹🇿🇹🇯🇹🇭🇹🇱🇹🇬🇹🇰🇺🇬🇹🇻🇹🇨🇹🇲🇹🇷🇹🇳🇹🇹🇹🇴🇺🇦🇦🇪🇬🇧🏴󠁧󠁢󠁥󠁮󠁧󠁿🏴󠁧󠁢󠁳󠁣󠁴󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🇺🇸🇺🇾🇪🇭🇻🇳🇻🇪🇻🇦🇻🇺🇺🇿🇻🇮🇾🇪🇿🇼💢💚🔰💖🎲🧡💿💽💝❤️🧡💛💚💙💜🖤🤍💓💞💕❣❤️‍🩹❤️‍🔥💔🤎💗??💘💝💟☮✝☪🛐☦☯🕎🔯✡☸🕉⛎♈️♉️♊️♋️♌️♍️♎️⚛🆔♓️♒️♑️♐️♏️🉑🈺🈸🈚️🈶📳📴☣☢🈷✴️🆚💮🉐㊙️㊗️🈴🅾🆑🆎🅱🅰🈲🈹🈵🆘❌⭕️🛑⛔️📛🚫💯📵🔞🚱🚳🚯🚷♨️💢🚭❗️❕❓❔‼️⁉️🔅♻️🔰⚜🔱🚸⚠️〽️🔆✅🈯️💹❇️✳️❎🌐💠Ⓜ️🌀💤🏧🚾♿️🅿️🛗🈳🈂🛂🛃🛄🛅🚹🚺🚼📀🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉"
	xyz=[2592,1886,2593]
	for zz in range(len(emoji)):
		print(zz)
		if zz in xyz:
		    pass
		else:
		    que=reaaa.sub(str(emoji[zz]),"",que)
	return que
	
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
async def start_command1(client:Client,message:Message):
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
	#question=reaaa.sub("\n","       ",question)
	question=reaaa.sub(r"((@|#)([0-9A-Za-z\-\_\.])*(\s|\n{1,}|))|((\n| |){1,}(Join|🔜)(\n| |)){1,}", "", question)
	print("que se aage gye")
	question=reaaa.sub(r"(http|ftp|https|t\.me|tg):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", "", question)
	#question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}|)", "", question)
	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}(\d{1,}\. |\d{1,}\.)", "", question)
	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	question=reaaa.sub(r"^(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	
	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)", "", question)
	question=reaaa.sub(r"🔰 C.A BY 🔰", "", question)
	question=reaaa.sub(r"🔰", "", question)
	options=[o.text for o in mess.options]
	#question=emojicut(question)
	#zzzz=[emojicut(yy) for yy in options]
	#options=zzzz
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

@app.on_message(filters.regex("\d{1,2}:\d{1,2}:\d{1,2}") & filters.outgoing)
async def timer(client:Client,message:Message):
	print("start")
	scheduler.add_job(job, "interval", seconds=10 ,args=(client,message,))
	print("add job")
	scheduler.start()
	print("schedule")

async def job(client:Client,message:Message):
		mess1=await app.get_messages(message.chat.id, message.message_id)
		#print(mess1)
		timer=reaaa.split(":",mess1.text)
		total=int(timer[0])*3600+int(timer[1])*60+int(timer[2])
		try:
			if total//10>=1:
				mass=str((total-10)//3600)+":"+str((total-10)//60-((total-10)//3600)*60)+":"+str((total-10)-((total-10)//60-((total-10)//3600)*60)*60-((total-10)//3600)*3600)
				#mass=str((total-1-x*5)//3600)+":"+str((total-1-x*5)//60-((total-1-x*5)//3600)*60)+":"+str((total-1-x*5)-((total-1-x*5)//60-((total-1-x*5)//3600)*60)*60-((total-1-x*5)//3600)*3600)
				await app.edit_message_text(message.chat.id, message.message_id,mass)
				
			else:
				await app.edit_message_text(message.chat.id, message.message_id,"Times Up!!!")
				
		except:
			await app.edit_message_text(message.chat.id, message.message_id,"Some error comes...")
			
			

		
		
		
	
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
from poll_to_text import polltotext

@restricted
@run_async
@send_typing_action
def poll(update, context):
    quest=(update.message.text)
    if update.effective_chat.id<=0:
            time.sleep(5)
    asyncio.run(texttopoll(quest,update,context))
    if update.effective_chat.id<=0:
            time.sleep(5)
    
#@run_async
@restricted
@send_typing_action
def receive_poll(update, context):
    """On receiving polls, reply to it by a closed poll copying the received poll"""
    actual_poll = update.effective_message.poll
    asyncio.run(polltotext(actual_poll,update,context))
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
    updater.idle()#
    
if __name__ == '__main__':
    main()