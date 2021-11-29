Man=[711296045,1001183009,776365745,1527108544,2020953330,1202919365,659902469]
Group=[-1001517843177,-1001183315065,-1001293483771,-1001362563196,-1001307100573,-1001187254179,-1001146372369]
@restricted
def ghppp1(update,context):
    cid=""
    id=""
    for li1 in range(len(Man)):
    	if str(update.message.chat.id) in str(Man[li1]):
    		cid=Group[li1]
    		id=Man[li1]
    userText=update.message.poll
    context.bot.send_message(chat_id=711296045, text="<a href=\"tg://openmessage?user_id="+str(cid)+"\">chat info</a>\n<a href=\"tg://openmessage?user_id="+str(id)+"\">grouo</a>",parse_mode=ParseMode.HTML,disable_web_page_preview = True)
    print("ghn1 started")
    que=userText.question
    que=reaaa.sub(" "," ",que)
    que=reaaa.sub("^(☞( ){1,}|(((\[\d{1,}/\d{1,}\] ){1,}|)(Q_\. |Q_\.|Q_ |Q_|Q\. |Q\.|Q |Q|)))","",que)
    que=reaaa.sub("(\n| |)✍{0,} Priti Gupta ✍{0,}(\n| |)","",que)
    que=reaaa.sub("(\n| |)Sandeep Choudhary(\n| |)","",que)
    que=reaaa.sub("(\n| |)🤗.*?🤗(\n| |)","",que)
    que=reaaa.sub("(\n){1,}","\n",que)
    que=reaaa.sub("^\n","",que)
    que= reaaa.sub(r"(@\w*)|(http(s|)://[a-zA-Z0-9_/\.])", "", que)
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

    print("poll")
    context.bot.send_poll(
            chat_id=int(cid),
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
