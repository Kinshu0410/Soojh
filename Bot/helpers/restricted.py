from functools import wraps
from telegram import ChatAction, Update
from telegram.ext import CallbackContext

LIST_OF_ADMINS = ["711296045","1001183009","776365745","1527108544","2020953330","1202919365","659902469"]

def restricted(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        
        userName = str(update.message.chat.id)
        userName1=str(update.message.from_user.id)
        if userName and userName1 not in LIST_OF_ADMINS:
            #update.message.reply_text(f"Unauthorized access denied for {update.effective_user.mention_html()}.", parse_mode=ParseMode.HTML)
            return
        return func(update, context, *args, **kwargs)
    return wrapped
