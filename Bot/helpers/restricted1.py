from functools import wraps
from telegram import Update
from telegram.ext import CallbackContext

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
