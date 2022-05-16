#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymongo import MongoClient
import dns

'''import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] # this is a google public dns server,  use whatever dns server you like here
# as a test, dns.resolver.query('www.google.com') should return an answer, not an exception'''
clientmongo=MongoClient('mongodb+srv://Kinshu04101:Qwert123@cluster0.ckcyx.mongodb.net/test?retryWrites=true&w=majority')
#
from pyrogram import Client, enums
from pyrogram.raw import functions
from pyrogram.raw import types
from pyrogram.handlers import MessageHandler, PollHandler
from pyrogram import filters
from pyrogram.types import Message, ReplyKeyboardRemove, Poll
from pyrogram.enums import PollType
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
from pyrogram.errors import FloodWait
import  json
import time, random
import re as reaaa
import requests
#app = Client("my_account",
#bot_token=ClientText["bot_token"],
#api_id="13682659",
#api_hash="b984d240c5258407ea911f042c9d75f6")
app=Client("my_account",session_string="BQDQx-MAgCWZcH5E_yMYE_LtOoecmqbtroBlbtZShm6tIydTJ3aIFUCjVRy0b6vsjU_H2SpD9IKrIWgZUX1Bs7Y2gMdTDwe1wkub-8zkgy6uhuYcDd2Vr9dKxmyC4JWW3EtenPCe3LPLnGcLaWpZfDb11nZLe3gbfFPbWiFIpSa-bEol_bveyfcDq5hkxwsKayrv_0pk1h30HhyJyuyUUKUSb3qAjqDKLaXxWm_zBtF8YG7AsARzfVoEQqKz2pNt-4rr56VPR-RBVcm9xwr3sZRRIPnrAgallbnlqZ1M_Gc23RxcpIKPuEDhCMTJtYYa-VlauKQsp5pA-iY3NZ3Rkagnfm7y9QAAAAAqZYQtAA",api_id="13682659",api_hash="b984d240c5258407ea911f042c9d75f6")


from pyrogram.enums import PollType
scheduler = AsyncIOScheduler(timezone="Asia/kolkata")
@app.on_message(filters.regex("^Cid") )#& filters.incoming)
async def cyid(client:Client,message:Message):
	await app.send_message(message.chat.id,str(message.chat.id))  

scheduler.start()
@app.on_message(filters.regex("The quiz")  )#& filters.incoming )
async def job2_partener(client:Client,message:Message):
	if message.reply_markup:
		if message.reply_markup.inline_keyboard[0][0].text=="Share quiz":
			name= clientmongo["group_schedule"].list_collection_names()
			now=""
			if str(message.chat.id) in name:
			    name1= clientmongo["channal_schedule"].list_collection_names()
			    for zz in name1:
			        
			        scheduler.add_job(job4, "cron", hour="12",minute="5-12",replace_existing=True,args=(zz,client,message,) ,id="job4"+str(zz))
			        try:
			            scheduler.start()
			        except:
			            pass
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
			    await app.send_message(int(message.chat.id),"💬 NEXT QUIZ AT "+now+"\n\n"+ col.find_one({"data":{"$type":"array"}})["data"][Nu[0]][list(col.find_one({"data":{"$type":"array"}})["data"][Nu[0]].keys())[0]],disable_web_page_preview=True)
			name= clientmongo["group_schedule"].list_collection_names()
			for x in name:
				try:
					hour1=clientmongo["group_schedule"][str(x)].find_one({"Time":{"$type":"string"}})["Time"]
					#print(str(x)+"=====Time====="+hour1)
					hour=reaaa.split(",",hour1)
					zz=""
					for y in range(len(hour)):
					    zz=zz+str(int(hour[y])-1)+","
					print(scheduler.add_job(job2, "cron",hour=zz[:-1], minute='58',replace_existing=True,args=(x,client,message,) ,id="job2"+str(x)))
					print(scheduler.add_job(job1, "cron", hour=hour1,replace_existing=True,args=(x,client,message,) ,id="job1"+str(x)))
					#print("")
				except Exception as e:
					print(""+str(e))
	
			    
	        
@app.on_message(filters.regex("schedule_start") )#& filters.incoming)
async def schedule_job(client:Client,message:Message):
	name= clientmongo["group_schedule"].list_collection_names()
	for x in name:
		try:
			hour1=clientmongo["group_schedule"][str(x)].find_one({"Time":{"$type":"string"}})["Time"]
			#print(str(x)+"=====Time====="+hour1)
			hour1=reaaa.sub(" ","",hour1)
			hour=reaaa.split(",",hour1)
			zz=""
			for y in range(len(hour)):
			    zz=zz+str(int(hour[y])-1)+","
			print(scheduler.add_job(job2, "cron",hour=zz[:-1], minute='58',replace_existing=True,args=(x,client,message,) ,id="job2"+str(x)))
			print(scheduler.add_job(job1, "cron", hour=hour1,replace_existing=True,args=(x,client,message,) ,id="job1"+str(x)))
			#print(" schedule done")
		except Exception as e:
			await app.send_message(int(message.chat.id),"schedule error in chat id = "+str(x)+"\nerror name = "+str(e))
					
	await app.send_message(int(message.chat.id),"Schedule update")
	name= clientmongo["group_schedule"].list_collection_names()
	
	name= clientmongo["channal_schedule"].list_collection_names()
	for x in name:
	    scheduler.add_job(job4, "cron", hour="12",minute="17-24",replace_existing=True,args=(x,client,message,) ,id="job4"+str(x))
	scheduler.start()

@app.on_message(filters.regex("^Set time.*?") )#& filters.incoming)
async def setting_time(client:Client,message:Message):
	col=clientmongo["group_schedule"][str(message.chat.id)]
	cid=[]
	async for member in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
		cid.append(member.user.id)
	##print(str(cid))
	if message.from_user.id in cid:
		myquery1 = {"Time":{"$type":"string"}}
		if col.find_one(myquery1):
			newvalues1= { "$set": {"Time":reaaa.sub("^Set time","",message.text)}}
			col.update_one(myquery1,newvalues1)
		else:
			col.insert_one({"Time":reaaa.sub("^Set time","",message.text)})
		
		await app.send_message(int(message.chat.id),"Schedule Reset")
	scheduler.start()

@app.on_message(filters.text & filters.outgoing & filters.chat("TempMail_org_bot"))
async def job_ads(client:Client,message:Message):
	xx=message.text
	entities=message.entities
	Admin=[711296045,-1001487436278,-1001135796728,-1001309576992,-1001443924980,
-1001472989895,-1001222891254,-1001517843177,-1001478660095,-1001173492501,-1001177789955,-1001342905358,-1001725784523,-1001664461759]
	Admin1=[-1001412214082,-1001412214082,-1001244305820,-1001393712887,]
	for x in Admin:
		#await app.set_parse_mode()
		try:
			await app.send_message(int(x),xx,entities=entities,disable_web_page_preview=True,disable_notification=True,parse_mode="markdown")
		except:
			await app.send_message("me",str(x),entities=entities,disable_web_page_preview=True,disable_notification=True,parse_mode="markdown")
	for x in Admin1:
		#await app.set_parse_mode()
		try:
			await app.send_message(int(x),"/current",entities=entities,disable_web_page_preview=True,disable_notification=True,parse_mode="markdown")
		except:
			await app.send_message("me",str(x),entities=entities,disable_web_page_preview=True,disable_notification=True,parse_mode="markdown")
		
	
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
			time.sleep(2)
			await client.request_callback_answer(int(x),int(mass_id.id)+1,callback_data='{"a":"user_ready"}')
		except Exception as e:
			print("def job1 in cloudmersiver error name = "+str(e))


async def job2(x,client:Client,message:Message):
	##print(str(x))
	col=clientmongo["group_schedule"][str(x)]
	myquery1 = {"Nu":{"$type":"array"}}
	Nu=col.find_one(myquery1)["Nu"]
	now=""
	try:
		if int(time.ctime(time.time() +19800)[11:13])+1>=13:
			now=str(int(time.ctime(time.time() +19800)[11:13])+1-12)+" PM"
		else:
			now=str(int(time.ctime(time.time() +19800)[11:13])+1)+" AM"
		await app.send_message(int(x),"💬 NEXT QUIZ play in 2 Minutes\n\n"+ col.find_one({"data":{"$type":"array"}})["data"][Nu[0]][list(col.find_one({"data":{"$type":"array"}})["data"][Nu[0]].keys())[0]],disable_web_page_preview=True)
		time.sleep(10)
		mass=await app.send_message(int(x), "0:1:30")
		scheduler.add_job(job3, "interval", seconds=10,replace_existing=True,args=(mass,client,message,) ,id="job3"+str(x))
		#print("job3 added for = "+str(message.first_name))
	except Exception as e:
		print("def job2 in cloudmersiver error name = "+str(e))
import os
from quickstart import Drive_OCR
@app.on_message(filters.photo & filters.chat(chats=["POLLQZ",-1001132926651]))
@app.on_message(filters.photo & filters.private )
async def img_text(client:Client,message:Message):
	print("download start")
	fname=id_generator()
	file=await app.download_media(message,file_name=fname+"sample.png")
	print(file)
	await app.send_message(message.chat.id,str(reaaa.sub("^.*?\n.*?\n","",Drive_OCR('/app/downloads/'+fname+'sample.png').main())))
	os.remove(file)
	os.remove('/app/downloads/'+fname+'sample.png')
import string
import random
def id_generator(size=10, chars=string.ascii_uppercase):
	return ''.join(random.choice(chars) for _ in range(size))

import fitz, random

@app.on_message(filters.regex("^.cp ") & filters.private)
@app.on_message(filters.regex("^.cp ") & filters.chat(chats=["POLLQZ",-1001132926651]))
async def crop_pdf(client:Client,message:Message):
	print(message.reply_to_message)
	non=0
	text=reaaa.sub("^\.cp","",message.text)
	te=reaaa.split("\n",text)
	text=reaaa.sub(" ","",te[0])
	tex=reaaa.split(",",te[1])
	text=reaaa.split(":",text)
	fname1=id_generator()
	fname=fname1
	file=await app.download_media(await app.get_messages(message.chat.id, message.reply_to_message.id),file_name=fname+".pdf")
	print(file)
	doc=fitz.open(file)
	noOfPages = doc.pageCount
	
	f=open(fname1+".txt", 'w',encoding='utf-8')
	image_folder='/app/downloads/'
	
	for pageNo in range(int(tex[0])-1,int(tex[1])):
		for x in text:
			
			y=reaaa.split(",",x)
			fname=id_generator()
			zoom=2
			page=doc.load_page(pageNo)
			mat = fitz.Matrix(zoom, zoom)
			pix=page.get_pixmap(matrix = mat)
			pix.writePNG(image_folder+fname+".png")
			from PIL import Image
			
			im = Image.open(image_folder+fname+".png")
			cropped=im.crop((int(y[0]),int(y[1]),int(y[2]),int(y[3])))
			cropped.save(image_folder+fname+".png")
			f.write(str(reaaa.sub("^.*?\n.*?\n","",Drive_OCR(image_folder+fname+".png").main()))+"\n")
			#await app.send_document(message.chat.id, image_folder+fname+".png")
			os.remove(image_folder+fname+".png")
			non+=1
			#if non%25==0:
				#await app.send_document(message.chat.id, fname1+".txt",caption="total pages "+str(int(non/25))+"/"+str(int(noOfPages)/25))
				#f.truncate(0)
			
	f.close()
	await app.send_document(message.chat.id, fname1+".txt")
	os.remove(fname1+".txt")
	#os.remove(image_folder+fname1+".pdf")
	os.remove(file)
		
		#
@app.on_message(filters.regex("^.c ") & filters.private)
@app.on_message(filters.regex("^.c ") & filters.chat(chats=["POLLQZ",-1001132926651]))
async def crop(client:Client,message:Message):
	print("start")
	text=reaaa.sub("^\.c","",message.text)
	text=reaaa.sub(" ","",text)
	text=reaaa.split(":",text)
	for x in text:
		y=reaaa.split(",",x)
		print(message.reply_to_message)
		
		fname=id_generator()
		print("start")
		file=await app.download_media(await app.get_messages(message.chat.id, message.reply_to_message.id),file_name=fname+".png")
		print(file)
		from PIL import Image
		im = Image.open(file)
		cropped=im.crop((int(y[0]),int(y[1]),int(y[2]),int(y[3])))
		cropped.save(file)
		await app.send_document(message.chat.id, file)
		os.remove(file)
#@app.on_message(filters.document & filters.chat(chats=["POLLQZ",-1001132926651]) &~filters.chat(chats=[711296045]))
#@app.on_message(filters.document & filters.chat(chats=[711296045]))
@app.on_message(filters.document & filters.chat(chats=["POLLQZ",-1001132926651]) )
@app.on_message(filters.document & filters.private & ~filters.chat("Neha55bot"))
async def pdf_img_textpri(client:Client,message:Message):
    	z=""
    	fname=id_generator()
    	file=await app.download_media(message,file_name=fname+".pdf")
    	
    	with fitz.open(file) as doc:
    		zoom = 2 
    		mat = fitz.Matrix(zoom, zoom)
    		noOfPages = doc.pageCount
    		image_folder='/app/downloads/'
    		
    		for x in range(3):
    		    page = doc.load_page(random.randint(1, noOfPages))
    		    pix = page.get_pixmap(matrix = mat)
    		    pix.writePNG(image_folder+str(message.chat.id)+fname+".png")
    		    from PIL import Image
    		    from PIL import ImageDraw
    		    im = Image.open(image_folder+str(message.chat.id)+fname+".png")
    		    w, h = im.size
    		    I1 = ImageDraw.Draw(im)
    		    for W in range(1,int(w)//50):
    		        for H in range(1,int(h)//50):
    		            I1.text((W*50, H*50), "("+str(W*50)+","+str(H*50)+")", fill=(255, 0, 0))
    		            
    		    im.save(image_folder+str(message.chat.id)+fname+".png")
    		    time.sleep(1)
    		    await app.send_document(message.chat.id, image_folder+str(message.chat.id)+fname+".png",caption="total pages "+str(noOfPages)+"\nX - coordinate ="+str(w)+"\nY - coordinate ="+str(h)+"\n\n.c 0,0,"+str(w)+","+str(h))
    		    os.remove(image_folder+str(message.chat.id)+fname+".png")
    		    
    	

#@app.on_message(filters.document & filters.chat(chats=["POLLQZ",-1001132926651]) )
#@app.on_message(filters.document & filters.private & ~filters.chat("Neha55bot") &~filters.chat(chats=[711296045]))
async def pdf_img_text(client:Client,message:Message):
    if True:#if reaaa.findall(".pdf$",message.file_name):
    	non=0
    	
    	z=""
    	fname=id_generator()
    	file=await app.download_media(message,file_name=fname+".pdf")
    	f=open(fname+".txt", 'w',encoding='utf-8')
    	with fitz.open(file) as doc:
    		zoom = 2 
    		mat = fitz.Matrix(zoom, zoom)
    		noOfPages = doc.pageCount
    		
    		await app.send_message(message.from_user.id,"Last Page Number = "+str(noOfPages))
    		image_folder='/app/downloads/'
    		for pageNo in range(noOfPages):
    			#await app.send_message(message.chat.id,str(pageNo))
    			page = doc.load_page(pageNo)
    			pix = page.get_pixmap(matrix = mat)
    			pix.writePNG(image_folder+str(message.chat.id)+fname+".png")
    			f.write(str(reaaa.sub("^.*?\n.*?\n","",Drive_OCR(image_folder+str(message.chat.id)+fname+".png").main()))+"\n")
    			non+=1
    			if non%25==0:
    			    #await app.send_message(message.chat.id,"sucessful")
    			    await app.send_document(message.chat.id, fname+".txt",caption="total pages "+str(noOfPages))
    			    f.truncate(0)
    			print(image_folder+str(message.chat.id)+fname+".png")
    		
    		f.close()
    		await app.send_document(message.chat.id, fname+".txt",caption="total pages "+str(noOfPages))
    		os.remove(fname+".txt")
    		os.remove(image_folder+str(message.chat.id)+fname+".png")
    		os.remove(file)
		
from youtube_uploader import yootube
@app.on_message(filters.video & filters.outgoing & filters.chat("Neha55bot"))
@app.on_message(filters.document & filters.outgoing & filters.chat("Neha55bot"))
async def job2_partbegne(client:Client,message:Message):
	xx=(message.text)
	cred=[]
	async def progress(current, total):
		print(f"{current * 100 / total:.1f}%")
	down=await app.download_media(message, progress=progress)
	print(down)
	for file in os.listdir("you_c"):
		if file.endswith(".json"):
			cred.append(os.path.join("you_c", file))
	#return await yoo(cred,down,client,message)

async def yoo(cred,down,client,message):
	Nu=clientmongo["youtube"]["token"].find_one({})["Nu"]
	try:
		yootube(down,cred[Nu])
		cred1=[]
		for file in os.listdir("/app/downloads"):
			#if file.endswith(".mp4"):
			cred1.append(os.path.join("/app/downloads", file))
		print(cred1)
		for yy in cred1:
			os.remove(yy)
			#print(yy)
		try:
			await app.send_message(message.chat.id,"sucessful")#
		except FloodWait as e:
			await asyncio.sleep(e.x)
	except Exception as zz:
		if Nu == len(cred):
			Nu=0
		else :
			Nu+=1
		clientmongo["youtube"]["token"].update_one({},{"$set": { "Nu":Nu} })
		try:
			await app.send_message(message.chat.id,"Trying to another Api = "+str(zz)+"\n"+str(Nu))
		except FloodWait as e:
			await asyncio.sleep(e.x)
		return await yoo(cred,down,client,message)
		
from pytube import YouTube

@app.on_message(filters.regex("^https://youtu.be/") & filters.outgoing)
async def job2_partegne(client:Client,message:Message):
	xx=(message.text)
	url=xx
	cred=[]
	Nu=clientmongo["youtube"]["token"].find_one({})["Nu"]
	for file in os.listdir("you_c"):
		if file.endswith(".json"):
			cred.append(os.path.join("you_c", file))
	try:
		my_video = YouTube(url)
	except:
		pass
	print(my_video.title)
	my_video = my_video.streams.get_highest_resolution()
	#print(my_video.download())
	down=my_video.download()
	print(down)
	try:
			pass#yootube(down,cred[Nu])
	except Exception as e:
			await app.send_message(message.chat.id,str(e)+str(Nu))
			if Nu == len(cred):
				Nu=0
			else :
				Nu+=1
			clientmongo["youtube"]["token"].update_one({},{"$set": { "Nu":Nu} })
	await app.send_video("me", file_name=my_video.title, video=down,caption=xx)
	os.remove(down)
	
@app.on_message(filters.regex("^Y") & filters.outgoing)
async def job2_partene(client:Client,message:Message):
	xx=reaaa.sub("^Y","",message.text)
	fname=id_generator()
	z=1
	#r = requests.get(xx)
	chunk_size = 10000
	r = requests.get(xx, stream=True)
	with open(fname+".mp4", "wb") as f:
		#print("in file")
		for chunk in r.iter_content(chunk_size=chunk_size):
			f.write(chunk)
			z+=1
			if z==100:
				break
	
	try:
		try:
			from youtube_uploader import yootube
			pass#yootube(fname+".mp4")
		except:
			pass
		await app.send_document(message.chat.id, fname+".mp4")
	except Exception as e:
		await app.send_message(message.chat.id,str(e))
	os.remove(fname+".mp4")

@app.on_message(filters.regex("^Z") & filters.outgoing)
async def job2_hhpartene(client:Client,message:Message):
	xx=reaaa.sub("^Z","",message.text)
	fname=id_generator()
	z=1
	#r = requests.get(xx)
	r = requests.get(xx)
	with open(fname+".mp4", "wb") as f:
		#print("in file")
		f.write(r.content)
	
	try:
		await app.send_document(message.chat.id, fname+".mp4")
	except Exception as e:
		await app.send_message(message.chat.id,str(e))
	os.remove(fname+".mp4")

@app.on_message(filters.regex("^\d{1,}-\d{1,}$") )#& filters.incoming)
async def job2_partener1(client:Client,message:Message):
        xx=reaaa.split("-",message.text)
        count=1
        from quickstart import Drive_OCR
        body = {"title": 'Result.pdf'}
        id=Drive_OCR(body).create()
        mess1="vote alreddy given"
        result={}
        new_result = {}
        tmarks=0
        for x in range(int(xx[0]),int(xx[1])+1):
    		#print(str(result))
            try:
            	try:
            		mess1=(await client.vote_poll(chat_id=message.chat.id, message_id=x,options=1))
            	except:
            		mess1=await app.get_messages(message.chat.id,x)
            		mess1=mess1.poll
            	off_set=None
            	for xxxx in range(mess1.total_voter_count//50+1):
            		mess2=await app.invoke(functions.messages.GetPollVotes(peer=await app.resolve_peer(message.chat.id),id=x,limit=mess1.total_voter_count,offset=off_set))
            		off_set=mess2.next_offset
        		#print(str(mess1.total_voter_count))
        		#print(mess2.next_offset)
        		#print(len(mess2.votes))
            		correct_option_id = 0
            		for i in range(len(mess1.options)):
            	
            		    print(mess1)
            		    if mess1.options[i].correct:
            		        correct_option_id = i
            		        break
            		
            		#print("correct_option_id = "+str(correct_option_id))
            		for mmid in range(len(mess2.votes)):
            		    #print(mess2.votes[mmid]["option"])
            		    if mess2.votes[mmid].user_id not in result.keys():
            		        #print
            		        fname=mess2.users[mmid].username
            		        if fname is None:
            		            fname=mess2.users[mmid].first_name
            		        else:
            		            fname="@"+fname
            		        if int.from_bytes(mess2.votes[mmid].option, "big") == correct_option_id or int.from_bytes(mess2.votes[mmid].option, "big") -48== correct_option_id:
            		            result[(mess2.votes[mmid].user_id)]={"fname":fname,"Marks":4}
            		        else:
            		            result[(mess2.votes[mmid].user_id)]={"fname":fname,"Marks":-1}
            		    else:
            		        Marks=result[(mess2.votes[mmid].user_id)]["Marks"]
            		        if int.from_bytes(mess2.votes[mmid].option, "big") == correct_option_id or int.from_bytes(mess2.votes[mmid].option, "big") -48== correct_option_id:
            		            result[(mess2.votes[mmid].user_id)]["Marks"]=Marks+4
            		        else:
            		            result[(mess2.votes[mmid].user_id)]["Marks"]=Marks-1
            	tmarks+=4
            except Exception as e:
                print(str(e))
    		    
        for key in sorted(result, key=lambda x: result[x]['Marks'], reverse=True):
    	    new_result[key] = result[key]
    	#print(new_result)
        text = []
        i = 0
        for chat_id in new_result.keys():
    	    i += 1
    	    fname = new_result[chat_id]['fname']
    	    marks = new_result[chat_id]['Marks']
    	    text.append(f"{i}. {fname} got {marks} marks")
        z=1
        for x in new_result:
            print(x)
            new_result[x]["Rank"]=z
            z+=1
        #count=len(Text)+1
        print(new_result)
        body={"requests":[{"insertTable":{"endOfSegmentLocation":{"segmentId":""},"columns":3,"rows":len(new_result)+1,},},]}
        
        try:
            Drive_OCR(body).update(id)
        except Exception as e:
            print(e)
        count+=1
        new={0: {'fname': 'First Name', 'Marks': 'Marks',"Rank":"Rank"}}
        new.update(new_result)
        for x in new:
            for key in ["Rank",'fname','Marks']:
                new[x][key] = new[x].pop(key)
        new_result=new
        
        for x in new_result:
            zz=len(new_result[x])
            
            for y in new_result[x]:
                print("=========="+str(zz))
                if zz==3:
                    count=count+3
                else:
                    count=count+2
                zz-=1
                Text=reaaa.sub("([^\u0000-\u05C0\u2100-\u214F\u0900-\u097F])","", str(new_result[x][y]))
                body={"requests":[{"insertText":{"location":{"index":count},"text":reaaa.sub("([^\u0000-\u05C0\u2100-\u214F\u0900-\u097F])","", str(new_result[x][y]))},},],}
                count=count+len(Text)
                #print(len(str(new_result[x][y])))
                #print(body)
                try:
                    Drive_OCR(body).update(id)
                
                except Exception as e:
                    print(e)
        count=count+len(Text)
        #Drive_OCR(body).update(id)
        try:
            await app.send_document(message.chat.id, Drive_OCR(body).download(id),caption="Total Number of Participents "+str(len(new_result)-1)+"\nTotal Marks "+str(tmarks)+"\n\n"+'\n'.join(text[0:20]))
            Drive_OCR(body).delete(id),
        except:
            for xy in range(len(text)//20+1):
                final_text='\n'.join(text[xy*20:(xy+1)*20])
                await app.send_message(message.chat.id, final_text)
                time.sleep(10)

@app.on_message(filters.regex("^force stop$") & ~ filters.private )#& filters.incoming)
async def job2_partener1212(client:Client,message:Message):
	global Tt
	try:
		tim=message.text
		
		Tt[message.chat.id]["s"]=(tim)
		await app.delete_messages(chat_id=message.chat.id,message_ids=message.id)
	except:
		pass

@app.on_message(filters.regex("^s\.t {,}\d{1,}$") & ~ filters.private )#& filters.incoming)
async def job2_partener12(client:Client,message:Message):
	global Tt
	try:
		tim=reaaa.sub("s.t {,}","",message.text)
		
		Tt[message.chat.id]["t"]=int(tim)
		await app.delete_messages(chat_id=message.chat.id,message_ids=message.id)
	except:
		await app.send_message(message.chat.id, "👎")
Tt={}

@app.on_message(filters.regex("^/start@quizbot.*?") & ~ filters.scheduled)#& filters.incoming)
async def job2_partener21(client:Client,message:Message):
        try:
            await app.delete_messages(chat_id=message.chat.id, message_ids=message.id)
        except:
            pass
        	

@app.on_message(filters.regex("^https://t.me/.*?/\d{1,}/\d{1,}$") & ~ filters.scheduled & ~ filters.private)#& filters.incoming)
async def job2_partener2(client:Client,message:Message):
        xx=reaaa.sub("https://t.me/","",message.text)
        xx=reaaa.sub("c/","-100",xx)
        global Tt
        
        tt=""
        try:
            await app.delete_messages(chat_id=message.chat.id, message_ids=message.id)
        except:
            pass
        xx=reaaa.split("/",xx)
        mess1="vote alreddy given"
        try:
        	xx[0]=int(xx[0])
        except:
        	pass
        result={}
        new_result = {}
        tmarks=0
        nn=1
        count=1
        from quickstart import Drive_OCR
        body = {"title": 'Result.pdf'}
        id=Drive_OCR(body).create()
        yy=None
        
        print(xx)
        li=[x for x in range(int(xx[1]),int(xx[1])+int(xx[2]))]
        random.shuffle(li)
        #await app.send_message(message.chat.id,str(li))
        for x in li:
    		#print(str(result))
    
            try:
                if Tt[message.chat.id]["s"]=="force stop":
                    tt1=30
                    break
            except:
                pass
            try:
                tt1=Tt[message.chat.id]["t"]
            except:
                Tt[message.chat.id]={}
                Tt[message.chat.id]["t"]=30
                tt1=30
            try:
            	try:
            		mess1=(await client.vote_poll(chat_id=xx[0], message_id=x,options=1))
            		#await app.send_message(message.chat.id,str(mess1))
            	except Exception as e:
            		#await app.send_message(message.chat.id,str(mess1))
            		#await app.send_message(message.chat.id, (str(e)))
            		mess1=(await app.get_messages(xx[0],x))
            		mess1=mess1.poll
            	off_set=None
            	question=mess1.question
            	explanation=mess1.exp
            	
            	if explanation is not None:
            	    explanation=reaaa.sub(r"(http|ftp|https|t\.me|tg):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", "", explanation)
            	    explanation=reaaa.sub(r"http.*? |@.*?( |$)|t.me.*? ", "", explanation)
            	    
            	#await app.send_message(message.chat.id, question)
            	
            	
            	
            	question=reaaa.sub(r"((@|#)([0-9A-Za-z\-\_\.])*(\s|\n{1,}|))|((\n| |){1,}(Join|)(\n| |)){1,}", "", question)
            	question=reaaa.sub(r"(http|ftp|https|t\.me|tg):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", "", question)
            	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}(\d{1,}\. |\d{1,}\.)", "", question)
            	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
            	question=reaaa.sub(r"^(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
            	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
            	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)", "", question)
            	question=reaaa.sub(r"(\n| |){1,}(|C\.A BY)(\n| |){1,}", "", question)
            	question=reaaa.sub(r"\n{,}(🪴:~ 🪴|⃝༺⃝꧁⃝ pragyagauri꧂⃝༻⃝)\n{,}", "", question)
            	question=reaaa.sub(r"", "", question)
            	options=[o.text for o in mess1.options]
            	lis=[]
            	Text=reaaa.sub("([^\u0000-\u05C0\u2100-\u214F\u0900-\u097F])","", "Q "+str(nn)+". "+question+"\n")
            	body={"requests":[{"insertText":{"text":Text,"location":{"segmentId":"","index":count},},},{"updateTextStyle":{"textStyle":{"foregroundColor":{"color":{"rgbColor":{"red":1,"green":0,"blue":0}}}},"fields":"*","range":{"segmentId":"","startIndex":count,"endIndex":count+len(Text)}}},],}
            	count=count+len(Text)
            	Drive_OCR(body).update(id)
            	for x in range(len(options)):
            	    options[x]=reaaa.sub("^(\[|\(|)(a|b|c|d|A|B|C|D|E|F|e|f)(\]|\)|)(\. |\.|)","",options[x])
            	    lis.append(x)#
            	
            	#await app.send_message(message.chat.id,str(lis))
            	random.shuffle(lis)
            	#await app.send_message(message.chat.id,str(lis))
            	
            	correct_option_id = 0
            	for i in range(len(mess1.options)):
            	    if mess1.options[i].correct:
            	        correct_option_id = i
            	        break
            	
            	
            	for i in range(len(lis)):
            	    if lis[i]==correct_option_id:
            	        correct_option_id = i
            	        break
            	options=[options[op] for op in lis]
            	
            	for o in range(len(options)):
            	    options[o]=bytes('(\\u004'+str(o+1), 'utf-8').decode('unicode-escape')+") "+options[o]
            	Text="\n".join(options)+"\n"
            	body={"requests":[{"insertText":{"text":Text,"location":{"segmentId":"","index":count},},},{"updateTextStyle":{"textStyle":{"foregroundColor":{"color":{"rgbColor":{"red":0,"green":0,"blue":0}}}},"fields":"*","range":{"segmentId":"","startIndex":count,"endIndex":count+len(Text)}}},],}
            	count=count+len(Text)
            	Drive_OCR(body).update(id)
            	mess2=(await app.send_poll(chat_id=message.chat.id,question=reaaa.sub("([^\u0000-\u05C0\u2100-\u214F\u0900-\u097F])","","Q "+str(int(xx[2])-nn+1)+". "+question),options=options,correct_option_id =correct_option_id,is_anonymous=False,type=PollType.QUIZ,open_period=tt1,explanation=explanation))
            	
            	if explanation is None:
            	    explanation="\n"
            	else:
            	    explanation="Explanation : "+explanation+"\n\n"
            	
            	Text=options[correct_option_id]+"✅\n"
            	body={"requests":[{"insertText":{"text":Text,"location":{"segmentId":"","index":count},},},{"updateTextStyle":{"textStyle":{"foregroundColor":{"color":{"rgbColor":{"red":0,"green":0,"blue":1}}}},"fields":"*","range":{"segmentId":"","startIndex":count,"endIndex":count+len(Text)}}},],}
            	count=count+len(Text)
            	Drive_OCR(body).update(id)
            	Text=reaaa.sub("([^\u0000-\u05C0\u2100-\u214F\u0900-\u097F])","", explanation)
            	body={"requests":[{"insertText":{"text":Text,"location":{"segmentId":"","index":count},},},{"updateTextStyle":{"textStyle":{"foregroundColor":{"color":{"rgbColor":{"red":0,"green":1,"blue":0}}}},"fields":"*","range":{"segmentId":"","startIndex":count,"endIndex":count+len(Text)}}},],}
            	count=count+len(Text)
            	Drive_OCR(body).update(id)
            	nn+=1
            	#await asyncio.sleep(10)
            	mess1=await client.forward_messages(chat_id=-608479342,from_chat_id=message.chat.id,message_ids=mess2.id)
            	if yy is not None:
            	    try:
            	        await app.delete_messages(chat_id=message.chat.id,message_ids=yy)
            	        
            	    except:
            	        pass
            	yy=mess2.id
            	await asyncio.sleep(tt1+1)
            	#await asyncio.sleep(1)
            	#print(mess1)
            	mess1=(await app.get_messages(-608479342,mess1.id))
            	#await app.send_message(message.chat.id, mess1)
            	#await app.send_message(message.chat.id, mess1.total_voter_count)
            	
            	
            	
            	
            	
            	
            	
            	
            	
            	
            	
            	for xxxx in range(mess1.poll.total_voter_count//50+1):
            		mess2=await app.invoke(functions.messages.GetPollVotes(peer=await app.resolve_peer(-608479342),id=mess1.id,limit=mess1.poll.total_voter_count,offset=off_set))
            		off_set=mess2.next_offset
        		#print(str(mess1.total_voter_count))
        		#print(off_set)
        		#print(len(mess2.votes))
            		correct_option_id = 0
            		mess1=(mess1.poll)
            		for i in range(len(mess1.options)):
            	
            		    #print(mess1)
            		    if mess1.options[i].correct:
            		        correct_option_id = i
            		        break
            		
            		print(off_set)
            		for mmid in range(len(mess2.votes)):
            		    #print(mess2.votes[mmid]["option"])
            		    if mess2.votes[mmid].user_id not in result.keys():
            		        #print
            		        fname=mess2.users[mmid].username
            		        if fname is None:
            		            fname=mess2.users[mmid].first_name
            		        else:
            		            fname="@"+fname
            		        if int.from_bytes(mess2.votes[mmid].option, "big") == correct_option_id or int.from_bytes(mess2.votes[mmid].option, "big") -48== correct_option_id:
            		            result[(mess2.votes[mmid].user_id)]={"fname":fname,"Marks":4}
            		        else:
            		            result[(mess2.votes[mmid].user_id)]={"fname":fname,"Marks":-1}
            		    else:
            		        Marks=result[(mess2.votes[mmid].user_id)]["Marks"]
            		        if int.from_bytes(mess2.votes[mmid].option, "big") == correct_option_id or int.from_bytes(mess2.votes[mmid].option, "big") -48== correct_option_id:
            		            result[(mess2.votes[mmid].user_id)]["Marks"]=Marks+4
            		        else:
            		            result[(mess2.votes[mmid].user_id)]["Marks"]=Marks-1
            	tmarks+=4
            except Exception as e:
                print(e)#await app.send_message(message.chat.id, (str(e)))
    		    
        try:
            await app.delete_messages(chat_id=message.chat.id,message_ids=yy)
        except:
            pass
        for key in sorted(result, key=lambda x: result[x]['Marks'], reverse=True):
    	    new_result[key] = result[key]
    	
    	#print(new_result)
        text = []
        i = 0
        for chat_id in new_result.keys():
    	    i += 1
    	    fname = new_result[chat_id]['fname']
    	    marks = new_result[chat_id]['Marks']
    	    text.append(f"{i}. {fname} got {marks} marks")
        z=1
        for x in new_result:
            print(x)
            new_result[x]["Rank"]=z
            z+=1
        #count=len(Text)+1
        print(new_result)
        if len(new_result)!=0:
            body={"requests":[{"insertTable":{"endOfSegmentLocation":{"segmentId":""},"columns":3,"rows":len(new_result)+1,},},]}
        try:
            Drive_OCR(body).update(id)
        except Exception as e:
            print(e)
        count+=1
        new={0: {'fname': 'First Name', 'Marks': 'Marks',"Rank":"Rank"}}
        new.update(new_result)
        for x in new:
            for key in ["Rank",'fname','Marks']:
                new[x][key] = new[x].pop(key)
        new_result=new
        
        for x in new_result:
            zz=len(new_result[x])
            if len(new_result)==1:
                break
            for y in new_result[x]:
                
                if zz==3:
                    count=count+3
                else:
                    count=count+2
                zz-=1
                Text=reaaa.sub("([^\u0000-\u05C0\u2100-\u214F\u0900-\u097F])","", str(new_result[x][y]))
                body={"requests":[{"insertText":{"location":{"index":count},"text":reaaa.sub("([^\u0000-\u05C0\u2100-\u214F\u0900-\u097F])","", str(new_result[x][y]))},},],}
                count=count+len(Text)
                #print(len(str(new_result[x][y])))
                #print(body)
                try:
                    Drive_OCR(body).update(id)
                
                except Exception as e:
                    print(e)
        if len(new_result)!=1:
            count=count+len(Text)
        #Drive_OCR(body).update(id)
        try:
            await app.send_document(message.chat.id, Drive_OCR(body).download(id),caption="Total Number of Participents "+str(len(new_result)-1)+"\nTotal Marks "+str(tmarks)+"\n\n"+'\n'.join(text[0:20]))
            Drive_OCR(body).delete(id),
        except:
            for xy in range(len(text)//20+1):
                final_text='\n'.join(text[xy*20:(xy+1)*20])
                await app.send_message(message.chat.id, final_text)
                time.sleep(10)

async def job3(mass,client:Client,message:Message):
		#
		try:
			mess1=await app.get_messages(mass.chat.id,mass.id)
			##print(str(mess1.text))
			##print(str(mess1.id))
			timer=reaaa.split(":",str(mess1.text))
			total=int(timer[0])*3600+int(timer[1])*60+int(timer[2])
		
			if total//10>=1:
				text1=str((total-10)//3600)+":"+str((total-10)//60-((total-10)//3600)*60)+":"+str((total-10)-((total-10)//60-((total-10)//3600)*60)*60-((total-10)//3600)*3600)
				#mass=str((total-1-x*5)//3600)+":"+str((total-1-x*5)//60-((total-1-x*5)//3600)*60)+":"+str((total-1-x*5)-((total-1-x*5)//60-((total-1-x*5)//3600)*60)*60-((total-1-x*5)//3600)*3600)
				await app.edit_message_text(int(mess1.chat.id), int(mess1.id),text1)
				
			else:
				await app.delete_messages(int(mess1.chat.id), mess1.id)
				print("job3")
				scheduler.shutdown(id="job3"+str(mess1.chat.id))  
				
		except:
			#await app.edit_message_text(int(mess1.chat.id), mess1.id,"Some error comes...")
			
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
		#print("drop Quiz "+str(message.chat.id)+".      "+str(len(col.find_one(myquery1)["data"])))
		col.drop()
	
@app.on_message(filters.text & filters.chat("POLLQZ") )#& filters.incoming)
async def forword(client:Client,message:Message):
    if message.reply_markup:
        await app.send_message("quizbot", message.reply_markup.inline_keyboard[0][0].url)
@app.on_message(filters.regex("^Del_All$") & ~ filters.poll)#& filters.incoming)
async def delete_all_quiz(client:Client,message:Message):
	cid=[]
	async for member in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
		cid.append(member.user.id)
	##print(cid)
	try:
		if int(message.from_user.id)  in  cid and str(message.chat.id) in clientmongo["group_schedule"].list_collection_names():
			col=clientmongo["group_schedule"][str(message.chat.id)].find_one_and_delete({"data":{"$type":"array"}})
			#print("")
			col=clientmongo["group_schedule"][str(message.chat.id)].find_one_and_delete({"Nu":{"$type":"array"}})
			#print("")
			
			await app.send_message(message.chat.id, 'Delete All Quiz sucessful \n अब ओर quiz add कीजिये')
	except:
		await app.send_message(message.chat.id, '       delete  ')
@app.on_message(filters.regex("^Stop$") & ~ filters.poll)#& filters.incoming)
async def stop_quiz(client:Client,message:Message):
	cid=[]
	async for member in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
		cid.append(member.user.id)
	##print(cid)
	try:
		if int(message.from_user.id)  in  cid and str(message.chat.id) in clientmongo["group_schedule"].list_collection_names():
			#print("")
			await app.send_message(message.chat.id, '/stop@QuizBot')
	except:
		pass

@app.on_message(filters.text & filters.chat("quizbot") )#& filters.incoming)
async def forworhd(client:Client,message:Message):
	
	#masss=(await app.get_messages(-1001495791558, 11061))
	##print(masss)
	##print(masss.reply_markup.inline_keyboard[0][0].callback_data)
	#await client.request_callback_answer(-1001495791558,11061,callback_data='{"a":"user_ready"}')
	#await app.send_message("me", str(message.reply_markup.inline_keyboard[0][0].callback_data))
	
	
	if hasattr(message, 'reply_markup'):
		#if message.chat.id==-1001495791558:
			##print(message)#if hasattr(message, 'from_user'):
			#if hasattr(message.from_user, 'id'):
				#if str(message.from_user.id)=='983000232':
					
		if message.reply_markup.inline_keyboard[0][0].callback_data=='{"a":"user_ready"}':
		    cid= clientmongo["group_schedule"].list_collection_names()
		    cid.append('983000232')
	        
		    if str(message.chat.id) in cid:
		        await client.request_callback_answer(chat_id=message.chat.id,message_id=message.id,callback_data=message.reply_markup.inline_keyboard[0][0].callback_data)

@app.on_message(filters.poll & filters.chat("Neha55bot") )#& filters.incoming)
async def forwortd(client:Client,message:Message):
	chatid=["Study_Quiz_India", "polls_quiz"]
	
	##print(message.id)
	try:
		
	    mess=(await client.vote_poll(chat_id=message.chat.id, message_id=message.id,options=1))
	except:
	    mess=message.poll
	##print(mess)
	    ##print(mess)
	await app.delete_messages(chat_id="Neha55bot", message_ids=message.id)
	question=mess.question
	
	#question=reaaa.sub("\n","       ",question)
	question=reaaa.sub(r"((@|#)([0-9A-Za-z\-\_\.])*(\s|\n{1,}|))|((\n| |){1,}(Join|)(\n| |)){1,}", "", question)
	#print("que se aage gye")
	question=reaaa.sub(r"(http|ftp|https|t\.me|tg):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", "", question)
	#question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}|)", "", question)
	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}(\d{1,}\. |\d{1,}\.)", "", question)
	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	question=reaaa.sub(r"^(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	
	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)", "", question)
	question=reaaa.sub(r" C.A BY ", "", question)
	question=reaaa.sub(r"", "", question)
	
	options=[o.text for o in mess.options]
	
	
	correct_option_id = 0
	for i in range(len(mess.options)):
	       if mess.options[i].correct:
	           correct_option_id = i
	           break
	#correct_option_id
	##print(message)
	#time.sleep(100)
	for x in chatid:
	    mess=(await app.send_poll(chat_id=x,question=question,options=options,correct_option_id =correct_option_id,is_anonymous=True,type=PollType.QUIZ))
	    ##print(mess)
	    #await app.stop_poll(chat_id=x,message_id=mess.id)


	
@app.on_message(filters.poll & filters.chat("quizbot") )#& filters.incoming)
async def forword(client:Client,message:Message):
	chatid=["POLLQZ"]
	
	##print(message.id)
	try:
		
	    mess=(await client.vote_poll(chat_id=message.chat.id, message_id=message.id,options=1))
	except:
	    mess=message.poll
	##print(mess)
	    ##print(mess)
	await app.delete_messages(chat_id="POLLQZ", message_ids=message.id)
	
	question=mess.question
	#question=reaaa.sub("\n","       ",question)
	question=reaaa.sub(r"((@|#)([0-9A-Za-z\-\_\.])*(\s|\n{1,}|))|((\n| |){1,}(Join|)(\n| |)){1,}", "", question)
	#print("que se aage gye")
	question=reaaa.sub(r"(http|ftp|https|t\.me|tg):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", "", question)
	#question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}|)", "", question)
	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}(\d{1,}\. |\d{1,}\.)", "", question)
	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	question=reaaa.sub(r"^(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	
	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)", "", question)
	question=reaaa.sub(r"(\n| |){1,}(|C\.A BY)(\n| |){1,}", "", question)
	question=reaaa.sub("([^\u0000-\u05C0\u2100-\u214F\u0900-\u097F])","",question)
	question=reaaa.sub(r"\n{,}(🪴:~ 🪴|⃝༺⃝꧁⃝ pragyagauri꧂⃝༻⃝)\n{,}", "", question)
	question=reaaa.sub(r"", "", question)
	options=[o.text for o in mess.options]
	
	
	correct_option_id = 0
	for i in range(len(mess.options)):
	       if mess.options[i].correct:
	           correct_option_id = i
	           break
	#correct_option_id
	##print(message)
	#time.sleep(100)
	for x in chatid:
	    mess=(await app.send_poll(chat_id=x,question=question,options=options,correct_option_id =correct_option_id,is_anonymous=False,type=PollType.QUIZ))
	    ##print(mess)
	    await app.stop_poll(chat_id=x,message_id=mess.id)

@app.on_message(filters.poll & filters.chat("Pdf2imgbot") )#& filters.incoming)
async def Biology(client:Client,message:Message):
	chatid=["Biology_Quiz4U"]
	
	##print(message.id)
	try:
		
	    mess=(await client.vote_poll(chat_id=message.chat.id, message_id=message.id,options=1))
	except:
	    mess=message.poll
	##print(mess)
	    ##print(mess)
	await app.delete_messages(chat_id="Neha55bot", message_ids=message.id)
	question=mess.question
	
	#question=reaaa.sub("\n","       ",question)
	question=reaaa.sub(r"((@|#)([0-9A-Za-z\-\_\.])*(\s|\n{1,}|))|((\n| |){1,}(Join|)(\n| |)){1,}", "", question)
	#print("que se aage gye")
	question=reaaa.sub(r"(http|ftp|https|t\.me|tg):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", "", question)
	#question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}|)", "", question)
	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}(\d{1,}\. |\d{1,}\.)", "", question)
	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	question=reaaa.sub(r"^(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	
	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)", "", question)
	question=reaaa.sub(r" C.A BY ", "", question)
	question=reaaa.sub(r"", "", question)
	
	options=[o.text for o in mess.options]
	
	
	correct_option_id = 0
	for i in range(len(mess.options)):
	       if mess.options[i].correct:
	           correct_option_id = i
	           break
	#correct_option_id
	##print(message)
	#time.sleep(100)
	for x in chatid:
	    mess=(await app.send_poll(chat_id=x,question=question,options=options,correct_option_id =correct_option_id,is_anonymous=False,type=PollType.QUIZ))
	    ##print(mess)
	    #await app.stop_poll(chat_id=x,message_id=mess.id)

#@app.on_message(filters.poll & filters.chat("me") )#& filters.incoming)
async def Current_iq(client:Client,message:Message):
	try:
		
	    mess=(await client.vote_poll(chat_id=message.chat.id, message_id=message.id,options=1))
	except:
	    mess=message.poll
	##print(mess)
	    ##print(mess)
	await app.delete_messages(chat_id=message.chat.id, message_ids=message.id)
	print("Current_iq")
	question=mess.question
	options=[o.text for o in mess.options]
	correct_option_id = 0
	for i in range(len(mess.options)):
	       if mess.options[i].correct:
	           correct_option_id = i
	           break
	await app.send_message("me", question+"\n"+"\n".join(options)+"\n"+str(correct_option_id))

@app.on_message(filters.poll & filters.chat("current_iq_bot") )#& filters.incoming)
async def Current_iq(client:Client,message:Message):
	chatid=["Current_Affairs_Quiz_Notes"]
	
	##print(message.id)
	try:
		
	    mess=(await client.vote_poll(chat_id=message.chat.id, message_id=message.id,options=1))
	except:
	    mess=message.poll
	##print(mess)
	    ##print(mess)
	await app.delete_messages(chat_id=message.chat.id, message_ids=message.id)
	question=mess.question
	
	#question=reaaa.sub("\n","       ",question)
	question=reaaa.sub(r"((@|#)([0-9A-Za-z\-\_\.])*(\s|\n{1,}|))|((\n| |){1,}(Join|)(\n| |)){1,}", "", question)
	#print("que se aage gye")
	question=reaaa.sub(r"(http|ftp|https|t\.me|tg):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", "", question)
	#question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}|)", "", question)
	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}(\d{1,}\. |\d{1,}\.)", "", question)
	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	question=reaaa.sub(r"^(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	
	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)", "", question)
	question=reaaa.sub(r" C.A BY ", "", question)
	question=reaaa.sub(r"", "", question)
	
	options=[o.text for o in mess.options]
	
	correct_option_id = 0
	for i in range(len(mess.options)):
	       if mess.options[i].correct:
	           correct_option_id = i
	           break
	#correct_option_id
	##print(message)
	#time.sleep(100)
	for x in chatid:
	    mess=(await app.send_poll(chat_id=x,question=question,options=options,correct_option_id =correct_option_id,is_anonymous=True,type=PollType.QUIZ))
	    ##print(mess)
	    #await app.stop_poll(chat_id=x,message_id=mess.id)

@app.on_message(filters.poll & filters.private )#& filters.incoming)
async def private_polls(client:Client,message:Message):
    chatid=[]
    if message.chat.id==1952288751:
        chatid=[-1001718523021]
    elif message.chat.id==388095945:
        chatid=[-1001309576992]
		
	#else#
	##print(message.id)
    if len(chatid)!=0:
    	try:
    		
    	    mess=(await client.vote_poll(chat_id=message.chat.id, message_id=message.id,options=1))
    	except:
    	    mess=message.poll
    	await app.delete_messages(chat_id=message.chat.id, message_ids=message.id)
    	print("private_polls")
    	question=mess.question
    	options=[o.text for o in mess.options]
    	correct_option_id = 0
    	for i in range(len(mess.options)):
    	       if mess.options[i].correct:
    	           correct_option_id = i
    	           break
    	#correct_option_id
    	##print(message)
    	#time.sleep(100)
    	for x in chatid:
    		try:
    			mess=(await app.send_poll(chat_id=x,question=question,options=options,correct_option_id =correct_option_id,is_anonymous=False,type=PollType.QUIZ))
    		except FloodWait as e:
    			await asyncio.sleep(e.x)
    	    #col=clientmongo["channal_schedule"][str(x)]
    	    #col.insert_one({'que':question,'op':options,'cor':correct_option_id})
    	    #scheduler.add_job(job4, "cron", hour="12",minute="5-12",replace_existing=True,args=(x,client,message,) ,id="job4"+str(x))
    	    #scheduler.start()
async def job4(x,client:Client,message:Message):
    col=clientmongo["channal_schedule"][str(x)]
    data=col.find_one_and_delete({})
    mess=(await app.send_poll(chat_id=x,question=data["que"],options=data["op"],correct_option_id= data["cor"],is_anonymous=True,type=PollType.QUIZ))
def emojicut(que:str):
	emoji="????????????????????????????????543206789#*??"
	xyz=[2592,1886,2593]
	for zz in range(len(emoji)):
		#print(zz)
		if zz in xyz:
		    pass
		else:
		    que=reaaa.sub(str(emoji[zz]),"",que)
	return que
	
@app.on_message(filters.poll & filters.chat("SOOJH_BOOJH_BOT_discussion_grouo"))
async def start_command(client:Client,message:Message):
	##print(message)
	chatid=["Soojhboojh_01bot"]
	
	##print(message.id)
	try:
	    mess=(await client.vote_poll(chat_id=message.chat.id, message_id=message.id,options=1))
	except:
	    mess=message.poll
	##print(mess)
	    ##print(mess)
	await app.delete_messages(chat_id="SOOJH_BOOJH_BOT_discussion_grouo", message_ids=message.id)
	question=mess.question
	options=[o.text for o in mess.options]
	correct_option_id = 0
	for i in range(len(mess.options)):
	       if mess.options[i].correct:
	           correct_option_id = i
	           break
	#correct_option_id
	##print(message)
	#time.sleep(100)
	for x in chatid:
	    await app.send_poll(chat_id=x,question=question,options=options,correct_option_id =correct_option_id,is_anonymous=False,type=PollType.QUIZ)#reply_markup=ReplyKeyboardRemove())

@app.on_message(filters.poll & filters.chat("SOOJH_BOOJH_BOT_discussion_grouo"))
async def start_command(client:Client,message:Message):
	##print(message)
	chatid=["Soojhboojh_01bot"]
	
	##print(message.id)
	try:
	    mess=(await client.vote_poll(chat_id=message.chat.id, message_id=message.id,options=1))
	except:
	    mess=message.poll
	##print(mess)
	    ##print(mess)
	await app.delete_messages(chat_id="SOOJH_BOOJH_BOT_discussion_grouo", message_ids=message.id)
	print("start_command")
	question=mess.question
	options=[o.text for o in mess.options]
	correct_option_id = 0
	for i in range(len(mess.options)):
	       if mess.options[i].correct:
	           correct_option_id = i
	           break
	#correct_option_id
	##print(message)
	#time.sleep(100)
	for x in chatid:
	    await app.send_poll(chat_id=x,question=question,options=options,correct_option_id =correct_option_id,is_anonymous=False,type=PollType.QUIZ)#reply_markup=ReplyKeyboardRemove())

@app.on_message(filters.poll & filters.chat("POLLQZ") & ~filters.chat("Soojhboojh_01bot"))
async def start_command1(client:Client,message:Message):
	##print(message)
	chatid=["POLLQZ"]
	
	##print(message.id)
	try:
		
	    mess=(await client.vote_poll(chat_id=message.chat.id, message_id=message.id,options=1))
	except:
	    mess=message.poll
	##print(mess)
	    ##print(mess)
	await app.delete_messages(chat_id="POLLQZ", message_ids=message.id)
	print("start_command1")
	question=mess.question
	#question=reaaa.sub("\n","       ",question)
	question=reaaa.sub(r"((@|#)([0-9A-Za-z\-\_\.])*(\s|\n{1,}|))|((\n| |){1,}(Join|)(\n| |)){1,}", "", question)
	#print("que se aage gye")
	question=reaaa.sub(r"(http|ftp|https|t\.me|tg):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", "", question)
	#question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}|)", "", question)
	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}(\d{1,}\. |\d{1,}\.)", "", question)
	question=reaaa.sub(r"^(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	question=reaaa.sub(r"^(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	
	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)(\[\d{1,}\/\d{1,}\] ){1,}", "", question)
	question=reaaa.sub(r"^(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q)(\d{1,}\. |\d{1,}\.)", "", question)
	question=reaaa.sub(r"\n{,}(🪴:~ 🪴|⃝༺⃝꧁⃝ pragyagauri꧂⃝༻⃝)\n{,}", "", question)
	question=reaaa.sub(r" C.A BY ", "", question)
	question=reaaa.sub(r"", "", question)
	options=[o.text for o in mess.options]
	#question=emojicut(question)
	#zzzz=[emojicut(yy) for yy in options]
	#options=zzzz
	correct_option_id = 0
	for i in range(len(mess.options)):
	       print(mess)
	       if mess.options[i].correct:
	           correct_option_id = i
	           break
	#correct_option_id
	##print(message)
	#time.sleep(100)
	for x in chatid:
	    mess=(await app.send_poll(chat_id=x,question=question,options=options,correct_option_id =correct_option_id,is_anonymous=False,type=PollType.QUIZ))
	    ##print(mess)
	    await app.stop_poll(chat_id=x,message_id=mess.id)

@app.on_message(filters.regex("\d{1,2}:\d{1,2}:\d{1,2}") )#& filters.outgoing)
async def timer(client:Client,message:Message):
	chatid=str(message.chat.id)
	scheduler.add_job(job, "interval", seconds=10,id="simple timer"+str(message.chat.id) ,replace_existing=True,args=(client,message,))
	#print("add job")
	scheduler.start()
	#print("schedule")

async def job(client:Client,message:Message):
		mess1=await app.get_messages(message.chat.id, message.id)
		##print(mess1)
		timer=reaaa.split(":",mess1.text)
		total=int(timer[0])*3600+int(timer[1])*60+int(timer[2])
		try:
			if total//10>=1:
				mass=str((total-10)//3600)+":"+str((total-10)//60-((total-10)//3600)*60)+":"+str((total-10)-((total-10)//60-((total-10)//3600)*60)*60-((total-10)//3600)*3600)
				#mass=str((total-1-x*5)//3600)+":"+str((total-1-x*5)//60-((total-1-x*5)//3600)*60)+":"+str((total-1-x*5)-((total-1-x*5)//60-((total-1-x*5)//3600)*60)*60-((total-1-x*5)//3600)*3600)
				await app.edit_message_text(message.chat.id, message.id,mass)
				
			else:
				await app.edit_message_text(message.chat.id, message.id,"Times Up!!!")
				scheduler.shutdown(id="simple timer"+str(message.chat.id)) 
				
		except:
			await app.edit_message_text(message.chat.id, message.id,"Some error comes...")
			scheduler.shutdown(id="simple timer"+str(message.chat.id)) 
			
			

		
		
		
	
@app.on_message(filters.text & filters.chat("KINBIN247_bot") & filters.incoming)
def forword(client:Client,message:Message):
    #if message.forward_from_chat:
#        forward=message.forward_from_chat
#    else:
#        forward=message.forward_from
#    
#    mess=(await app.get_history(forward.id, limit=1))
#    
#    ##print()
#    if mess:
#        for mid in range(mess[0].id-message.forward_from_message_id):
            
            client.forward_messages(chat_id="KINBIN247_bot",from_chat_id=message.chat.id,message_ids=message.id)
            app.delete_messages(chat_id="KINBIN247_bot",message_ids=message.id)
#    

@app.on_message(filters.poll & filters.chat("KINBIN247_bot") & filters.incoming)
def forword(client:Client,message:Message):
    
    client.forward_messages(chat_id="Soojhboojh_01bot",from_chat_id=message.chat.id,message_ids=message.id)
    app.delete_messages(chat_id="KINBIN247_bot",message_ids=message.id)


#@app.on_message(filters.regex("https://t.me/.*?/\d{1,}/\d{1,}") & filters.chat("jsjdkdkkd") & filters.outgoing )
def forword(client:Client,message:Message):
    chatid=message.text
    chatid=reaaa.sub("https://t.me/","",chatid)
    chatid=reaaa.split("/",chatid)
    #print(chatid)
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
            #print("start")#update.message.reply_text(f"Unauthorized access denied for {update.effective_user.mention_html()}.", parse_mode=ParseMode.HTML)
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
    #print(api_instance)
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
        #print("finish")
        context.bot.send_message(chat_id=chat_id , text="{}\n{}/{}".format(i,indt+1,len(x)+1))
        context.bot.send_message(chat_id=chat_id , text="{}".format(imgtext))
        #print("start")
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
    #print(indz)
    configuration = cloudmersive_ocr_api_client.Configuration()
    #Enter Your cloudmersive api key in place of  os.environ.get(...........)
    configuration.api_key['Apikey'] = x[indz]
    
    api_instance = cloudmersive_ocr_api_client.ImageOcrApi(cloudmersive_ocr_api_client.ApiClient(configuration))
    #print(query.data)
    #print(api_instance)
    try:
        lang=query.data
        #print("start")
        api_response = api_instance.image_ocr_post(filename,language=lang)
        #confidence=api_response.mean_confidence_level
        #context.bot.send_message(chat_id=chat_id , text="Confidence : "+str(confidence*100)+"% \nExtracted text:\n")
        global imgtext
        imgtext=api_response.text_result
        global apino
        apino=indz
        #print("good")
        ##print(api_response.text_result)
        
        #update.message.reply_text(api_response.text_result)
        #print("finish")
    except ApiException as e:
        my_fun(indz)
        #print("yo kya huaa")
        

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
    	tsr=tsr+"\n"+Textstr2[i]+"    "+Textstr3[i]
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
	    #print(Textstr2[z])
	    #print(Textstr3[z])
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
    idle()
    app.stop()
    updater.idle()#
    
if __name__ == '__main__':
    main()#