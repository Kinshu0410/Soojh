from pyrogram import Client
from pyrogram.handlers import MessageHandler, PollHandler
from pyrogram import filters
from pyrogram.types import Message, ReplyKeyboardRemove, Poll
app = Client("my_account",
#bot_token=ClientText["bot_token"],
api_id="13682659",
api_hash="b984d240c5258407ea911f042c9d75f6")
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
	    mess=(await app.send_poll(chat_id=x,question=question,options=options,correct_option_id =correct_option_id,is_anonymous=False,type="quiz"))
	    #print(mess)
	    #await app.stop_poll(chat_id=x,message_id=mess.message_id)