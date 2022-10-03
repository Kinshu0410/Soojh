from pyrogram import Client, idle
app = Client("my_live_bot",#session_string="BQDQx-MAAcKa6bmK3-vwhmKd0v3v4-SXoQ7PWIIqkl6-0j_96Gq6apAJ1vRFPUQrWwbcHoNLj0ouYgn5yCAvkT-BW8iE-1lYomM1VwAzEKHNuUVqTYrFDpCsAZE2ko1DudXnRUWz1SBkxk8f6JzrDS57sBmx2oEgUBXfiyGjJXJYn2KC-TsCao4Cbt-x6pE3LWwPprjAqsN6LHY2y2WA4QnQVagTclIrp5_Cc4FZbRnyNcL_MwQ-7hLF_5psbi4c1hXOYXYCnjx3KQ0Q--f0ISiGSt8h3xRu39RozHP1ANrB3pz4e_Unmoe8ad7hmhzwuil8uVqaV1qspejkWDo_3cyyadzV2QAAAAAqZYQtAA",
bot_token="1877489613:AAEWv36y-bbUjQPCemmJ53vSADAgKZB1A-U",
api_id="13682659",
api_hash="b984d240c5258407ea911f042c9d75f6")
import re as reaaa
import time



def get_mess_py(x,y):
	try:
		app.start()
		print(y)
		return_mess= app.get_messages(x,int(y))
		app.stop()
		return return_mess.text
	except Exception as e:
		#app.restart()
		pass#get_mess_py(x,y)

	
	
	
def check_mess(X,Y):
	x=X
	y=Y
	print(x)
	if len(x)<280:
		
		y.append(x)
		#x=reaaa.sub("\n".join(res[:-2]),"",x)
		return y
	else:
		res=reaaa.split("\n",x[:280])
		y.append("\n".join(res[:-2]))
		x=reaaa.sub("^"+"\n".join(res[:-2]),"",x)
		check_mess(x,y)