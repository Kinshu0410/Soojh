import telegram

from telegram import (
    Poll,
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
    CallbackQueryHandler
)

#1
import re


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
  update.message.reply_text('All sub Quiz   https://t.me/makefuturebright')
  update.message.reply_text('Math Question Bot   https://t.me/soojhboojh')

@run_async
@send_typing_action
def owner(update, context):
  update.message.reply_text("send your suggestions\n    1. @kinbin247 \n  2. @ANKITAdidi \n 3. comming soon \ud83d\ude1c")

@run_async
@send_typing_action
def poll(update, context):
    """Sends a predefined poll"""
    questions = ["Math_quiz_ans", "Royalworldmathdoubt", "Maths_Quiz_Notes", "learnwithaditya", " makefuturebright", "soojhboojh"]
    #que = update.message.text()
    quest=(update.message.text)
    q=quest[0:-1]
    q=re.sub("Poll to Text Bot\:\n|Soojh Boojh Bot - 02\:\n|NaN| Q.*\.|^\. |^\.", "", q)
    q=re.sub("\n\(.\) |\n.\. |\n.\) |\n\[.\] |\n.\. | \(.\) | .\) | .\. |\n\(.\) | \[.\] | (A|B|C|D|a|b|c|d|अ|ब|स|द)\.|\n(A|B|C|D|a|b|c|d|अ|ब|स|द)\.", "\n", q)
    q=re.sub("\n{2,}", "\n", q)
    
    q=re.split("[\n]", q)
    #update.message.reply_text(q)
    ques=q[0]
    que=""+ ques
    #que=que+"\n\n  ■_𝗜𝗺𝗽𝗼𝗿𝘁𝗮𝗻𝘁_𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻_■"
    option1="(A) "+q[1]
    option2="(B) "+q[2]
    option3="(C) "+q[3]
    option4="(D) "+q[4]
    options=[option1, option2, option3, option4]
    corr=quest[-1]
    result = re.match("[-+]?\d+$", corr)
    options5=q[5::1]
    options5="\n".join(options5)
    options5=re.sub(r"@\w*", "@kinbin247", options5)
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
    payload = {
        message.poll.id: {
            "questions": questions,
            "message_id": message.message_id,
            "chat_id": update.effective_chat.id,
            "answers": 0,
            "explanation": ["join"],
        }
    }
    context.bot_data.update(payload)

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
x=["9e9122c5-fec9-4fa3-8203-e31453326ab7","8793f202-352b-4423-b2be-d02d68d25491","d88a68de-5f14-4246-a604-1fb9f140f92f","b5cd4170-5fc8-4bf6-878c-40d142fcbdb8","36360d4f-9473-40a1-bc08-8a66fe2f6cbf","88aba44e-77c9-4830-92fa-57ea1ae970df","804c4b1c-d500-41a9-9410-3b61bcaf8f8c","479eb12c-5b82-42fb-b1ef-6e807cd5e7a6","c1b65c78-279a-4cc1-b30e-d8e2a57e504e","ebf6e8b6-3b87-4de8-ab63-fe4e667913a3","c220667d-3a6d-4f69-b07a-99286910b67b","9bbb3646-4ae5-4f37-b8d8-9eb218a0e3e5","ac3e51a6-8cdb-46ae-8e3e-6a6054932e5a","ac3e51a6-8cdb-46ae-8e3e-6a6054932e5a","a032d767-7d03-4721-b2f0-19ad27fa17f8","a06491c5-edd1-494d-8216-72a83f02daeb","47d11368-3c9a-4219-85d5-99c0831f79d4","03bd2f20-98f7-4a86-ba93-ff8479bc9ca6","a76d3e6f-732d-4b1f-81ca-41caf70ac60a","cb2987c9-5a72-4fab-846c-6eccb56480af","615d78fc-c095-486f-811d-d76eb291b5ba","4751f8d5-a9cf-4533-afbe-0fd75193c79a","ba2656c8-1e1a-42ed-93b6-10a6e1ab185b","6bf4f46c-15f2-4ad9-bfd4-00fa8ac885a1","f6aef455-b7d8-4f4b-ab11-339066b2b9e2","c3e0a7c8-7dc0-4f74-a766-ea414e1eab79","5089c023-3e81-42a0-9864-0c1f2261b1be","f77dd586-f4df-4ec8-b566-2452c1e6eeef","f5d0586d-4b5c-409b-a333-622326706cf1","66b57e0b-24dc-4d5d-a991-c97fad4c67a9","045f02c3-61f8-40ee-a6d2-e69a4323418e","f9f6c9f3-c480-452d-88cb-ea6458e00ff2","be664831-7767-41d9-964e-275a5d9b97b7","4838183a-c137-43d3-a51a-09a7f6988c3a","cfbcca4b-73f3-4d2c-8386-df454f069ce7","2a0eff85-5773-48f8-b4b0-b1b75bd5c39d","1a6135e9-d426-4470-9b04-3e08c972a866","5bbd8d53-df33-4091-835f-222cb73c183b","7224d020-1c3d-4758-82bf-a5bf60309a82","3083c762-fe35-49b7-93ad-11732f77c68d","b6d5ff2b-f3fc-4e26-b183-9d2e4728e133","2e975c3c-7db9-4443-8f94-616ec8439feb","401ed586-2a5b-469c-8c80-23e9be811a13","70c6b599-328e-4025-b327-008b0677c849","d1f9b4b9-aa46-485e-b4bb-5497a9d2ef73","2223bce8-f561-4412-b1fd-0b9ed0786086","089f0140-8721-4507-8ef8-6995c89594ba","70a6ed02-4bf7-4241-ac57-0b60ad6c32ac","57943c77-17c9-4760-b732-ed8573894f6a","2d5cd576-d940-4fbf-ba51-9a2f1ffb7fb1","fec29594-ee90-4053-aa82-14193d3915fd","d5803512-1d76-4d72-b50c-dca78c3dbdfa","051449b7-955b-4ffa-a055-a0c79fa0d994","a1dcd96d-e0c9-450f-9543-166c766b7c6f","42147c6d-aae4-4a3f-a2e4-5a2805bcf58a","e9b874be-0a9a-4359-9d38-337449e911b1","59756826-bbac-433a-b277-025ee27586e7","00a79672-3189-4aa6-99d3-5542e4163224","598132fe-59aa-491d-a1fc-8dfecf79bcc4","ce20b231-f5ea-42a4-84b5-2d430e983f03","12d161d8-96d1-4916-8e23-7679afef0055","9b862b34-bb46-4973-b76f-82c58ccdbb5f","9e3ce875-3c2b-4ec6-9a15-6f7a87d29850","abf6e14b-6b0b-49e6-aaa6-a730d9b73b31","4d2a617b-21b0-47be-bcf7-0311d17af3e2","ac7bee30-1f52-4d74-bc37-914a0c70c574","bdd6c492-ab36-4762-af80-0e4f134457d8","bdd6c492-ab36-4762-af80-0e4f134457d8","9c11de87-84c7-4d7d-b62e-80c9e96ad20b","9c11de87-84c7-4d7d-b62e-80c9e96ad20b","d86a44d9-71fb-4dcf-a9b8-a4be16670e71","c58d8b9d-9a4c-4fdb-8cc7-ee88478f9eca","4bfd4e6b-fd1c-41e3-b0fc-85b7191d1594","96323a4f-ade7-4c1c-8c55-42813dc199ef","593e8c26-2c14-473f-a9c6-92f9c215817b","ce4d3f27-e94c-4aa0-8663-f0a1a9c56ea0","d42c1193-0e25-46b9-9e8b-7a729eae67bd","8c169087-cbda-47fa-9107-bc9c5923e9b4","ea909bcd-b502-40e7-952b-c381858aa50d","c24ae956-e543-4385-aa44-442a47a67b8c","ca676e93-0a0b-462f-a462-ca50825d405a","49f6209d-246e-44fb-91b1-7f1efd110e32", "fc07a759-24f2-4b6d-a22e-4ee56849e102", "f059ddb0-e8dd-4bd9-9e1d-d9f2ce4be062", "5bd5e0ac-1599-4829-a2c6-2586ef87b1b7", "521ff3c4-d15f-40fb-b542-7bf3c1103917", "f65d6bce-afdd-4224-a27c-1275da209de4", "40df43f1-6740-483a-b8eb-da3d77214f17", "9544372c-e079-45a1-a26a-cd87764de618", "9afce88c-3b27-4290-b346-b82e0cbea66c", "2b613c57-ba05-4147-b445-d835444a2601", "6cb083c8-999d-4045-9a38-d82be38a2da7", "141ac45d-7ccb-4a17-9e08-aca81ec3144d", "fab4fcc9-6fc6-4928-b2cd-72e249c089e1", "27c50312-6c26-4965-b66d-14b9dd1a28eb", "5da63558-2b85-40cf-8d54-523a9f5d473e", "e4914e7f-a459-4a38-ab40-383ae7ec57fb", "4067d2e3-6d26-4e4e-ac51-53173fd752a1", "df9169ae-53a1-41bf-acb8-c6cdab9c992b", "ae776853-ba9b-4dee-8234-daa4b8f786c7", "2c03a50f-1755-4127-ad08-e288f0b4bbb9", "724b4d84-585a-4da4-a992-9fd62c27a4dd", "3023c5ce-6564-469f-aed6-ffb7a53e7a0e", "e06cfa3e-4db4-46ac-bdbd-83d839dc233e", "c8a3d55e-2996-4fc8-a81e-a75142e47d27", "8ffb99fb-240b-403c-a0a0-444963048ea7", "c64873a1-f6b4-47e0-8d5f-185e096a71b8", "6921711a-1d82-4fcb-9f31-77dc3aa4001d", "9035a478-5dcc-49de-a408-00b0d7c148e1", "928d9434-8a90-48ff-852b-6ebb6861b4b5", "9bbdcf7f-d8ad-4920-b7b3-f244e30a833c", "d97dbc63-7bf5-4165-9070-0dd0592ef90b", "d17b3b62-fd87-4afc-ae78-a649856150a1", "9856864e-eeb3-4798-80cc-43185d820dd3", "1ff066c1-d9a6-459b-8545-0bdb15e99a33", "96327a40-51b3-4597-ae01-cdbe9a411ae0", "5349bde1-5f6a-424d-bea9-a13a2a6c2480", "adc8599d-6553-41de-ab59-b1590e52f4a8", "3233439e-5852-4493-8cfd-b9f72ed8bbcd", "b0b217de-5b34-4874-a73d-b2daa7b29235", "f2026ebd-ef7b-40c0-aa2e-9c0dc9dae01e", "836b4c94-01d3-47ba-8fdc-a900a82e35cb","ea909bcd-b502-40e7-952b-c381858aa50d","f65d6bce-afdd-4224-a27c-1275da209de4","06c4ab89-c671-42c5-aa17-51cb6c0a780f", "2a15ea32-67da-4875-873b-c641dab10e83", "778c886f-cff4-4b3e-80a3-5a8652303c69", "352ebd25-95a0-42e4-893c-f45712e95cbb", "9f43dba2-15a6-4191-a4e9-23733b1b1a20", "7d3a9336-35b2-491c-8f6a-3ff896dae7c5", "44d144b5-9101-4603-b48d-45855e4a7bc8", "04d1a7be-c9d1-4d93-8ec4-e7545c2a570a", "7aacf169-7dee-4cb4-8cf9-6a02f738f201", "ea65ca04-54b9-4534-8895-671a88a569d0", "c5ea6139-6652-4d29-ba29-0bde564814fb", "b3427014-d810-44f8-ab0a-c7ab57a93525", "ae0d9ac0-ff55-463e-9ebb-183dc184c328", "a92be6c4-3622-4e5d-b9ee-df611c456ca3", "002664cb-9914-4b8f-86e3-065487423576", "b3427014-d810-44f8-ab0a-c7ab57a93525", "9452ea01-f602-4cc5-bfa4-9c05ad529afe", "e3817b4b-cde0-4bc2-bde6-b4ad21ec0a1c", "7cafc9bb-58bd-4da4-9b6f-92d87cc7538a", "9ae97e18-47e6-483c-a27c-5f8af229f27a", "acb39549-b99b-40d1-a1c3-5fc0e0e1b1fa", "6fdc4a5a-3bd4-4d70-9c2f-46fd3a9ad55c", "ddef2515-9461-437a-a9fc-9f44b20b0da9", "a2a7ba3f-b76f-44f5-ac35-04c5bd89b959", "84bae0a5-5956-40ed-afcc-a89d82d4600c", "7808335c-9085-4de6-9d72-3e94af2d3f50", "3211476e-424e-4ee5-92ae-99c2cdc092b8", "ed6e9e7a-ff15-4b16-9afb-9f51cb71645c", "2e4f9a19-573a-49c2-afa5-233992d8a56b", "93ee3d1e-a123-42ae-921d-82b6783abb09", "88167605-6304-48bc-a298-4e7ae7fe1df6", "a7da5c7c-8e7e-42f9-a0b1-0a5755807c6f", "5d09afe1-3708-4ecd-a57f-dba191eb926d", "4f63dff9-c367-4098-b08b-2bc4299e3ba2", "699aac99-e243-4d75-8bd0-38434cf5046e", "c22382ad-52f3-4e5a-91a0-3bd4480d823a", "2c5fec8e-9c79-45fd-8e07-a00d46036381", "6de0d78f-47ab-4e51-83e3-283fc5f85148", "dea73d4c-0d27-4820-a86c-8bce62bb788e", "a1176603-427a-499c-b8ac-ad0be4948bb1", "68917587-0691-4c6a-8650-49268d2ce73b", "fd34e54a-640d-4c7c-aad5-5d25e83ecd4a", "42528361-c326-48bd-b406-08fb57fb96e3", "f5946552-8087-4c5a-b373-1fcdc79401fe", "76ea5b11-1d29-4d89-ae37-def66db0a371", "b000f5b3-a45e-47dd-9480-ef4aaf8c3911", "dc676d28-a615-484c-b860-a5da8fc786ac", "ddef2515-9461-437a-a9fc-9f44b20b0da9", "969d79ed-42fa-428b-96de-af4429590eab", "d5f55cfa-07de-4a80-b424-8b25b57a53d3", "819c8751-0cc2-4c9a-af8d-9e9afeececd7", "7f9ce538-53cc-463d-9241-046745e16e00", "94757f7c-d43f-42ce-b0d4-e8386031c4f4", "026b7bcf-9bcd-4436-99d0-3758ad987eac", "da4914c4-45b9-4c24-9bfe-4b9bd8c67bbf", "ccfd22f2-c52f-49fe-94d0-bb94c9c0bd4f", "e8d0dded-72ef-4c10-b7b6-7209cbb252f8", "31b62657-f9e0-4a3e-9ed4-7e4cf2fc1bd9", "0bfa141c-8586-4a14-a0b3-0760603d76d2", "79d29af3-42ed-4363-ad79-57084ef60d8c", "d604ea23-f98b-43a2-86c8-08767f5476ef", "d7b0f10c-aa41-4e67-9f97-f4a6cc676bab", "fc2b068d-44d9-4529-85b5-294c2b5420e4", "bf62c6db-0f92-44e1-a5c2-deb6c3f8c72e", "31e016c4-055a-4e06-88cb-19e8272d9b35", "cd4eef43-7135-4a2a-8159-158b7845e863", "efcfe4ef-b36d-4481-b8a5-34f82d40f0f0", "dee56ee8-ef0e-43c0-8f6d-e73f2a40f33a", "d264ae90-d3dd-4092-9c5e-e766870c0c9f", "5e14664f-888e-4a52-a9d8-5214686980eb", "92a895ee-2120-4ba2-becb-ca3a1f98bdca", "7a0afb51-d0f6-4fab-a093-11a0c1939880", "68db1db1-8dfd-42f6-a81c-2d58b9250415", "ea909bcd-b502-40e7-952b-c381858aa50d", "04d1a7be-c9d1-4d93-8ec4-e7545c2a570a", "a92be6c4-3622-4e5d-b9ee-df611c456ca3", "ae0d9ac0-ff55-463e-9ebb-183dc184c328", "9f43dba2-15a6-4191-a4e9-23733b1b1a20", "352ebd25-95a0-42e4-893c-f45712e95cbb", "9452ea01-f602-4cc5-bfa4-9c05ad529afe", "778c886f-cff4-4b3e-80a3-5a8652303c69", "06c4ab89-c671-42c5-aa17-51cb6c0a780f", "2a15ea32-67da-4875-873b-c641dab10e83"]
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

#@run_async
@send_typing_action
def receive_poll(update, context):
    """On receiving polls, reply to it by a closed poll copying the received poll"""
    actual_poll = update.effective_message.poll
    # Only need to set the question and options, since all other parameters don't matter for
    # a closed poll
    #ex="@Soojhboojhbot/n"
    ex =actual_poll.explanation
    if ex is None:
        ex=""
        #ex="👇👇👇 Ask your Doubts here 👇👇👇\n👇👇👇        Only for Math        👇👇👇\nhttps://soojhboojh.xyz/ask-question/"
    else:
        ex=re.sub(r"\@.*?\s", "", ex)
        ex=re.sub(r"\@\w.*", "", ex)
        Ex=str(ex)        #ex=ex
    #update.message.reply_text(ex)
    #update.message.reply_text(ex)
    #ex=re.sub(r"\@.*?\s", "", ex)
    #ex=re.sub(r"\@\w.*", "", ex)
    question= actual_poll.question
    #question=re.sub("\@\w*", "", question)
    question=re.sub("𝗤. ", "", question)
    #question=re.sub(" ■_𝗜𝗺𝗽𝗼𝗿𝘁𝗮𝗻𝘁_𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻_■", "", question)
    q=re.sub("[\[].*?\/.*?[\]] ", "", question)
    q=re.sub("\n{1,}| {1,}", " ", question)
    #q="𝗤. "+qu
    #q=q+"\n\n  ■_𝗜𝗺𝗽𝗼𝗿𝘁𝗮𝗻𝘁_𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻_■"
    options=[o.text for o in actual_poll.options]
    corr = actual_poll.correct_option_id
    print(corr)
    #print(cor)
    cor=str(int(str(corr))+1)
    update.message.reply_text("<pre>"+q+"</pre>",parse_mode=telegram.ParseMode.HTML)
    #print(actual_poll)
    #update.message.reply_text("<pre>"+question+"</pre>",parse_mode=telegram.ParseMode.HTML)
    for r in options:
        update.message.reply_text("<pre>"+r+"</pre>",parse_mode=telegram.ParseMode.HTML)
    update.message.reply_text("<pre>"+options[corr]+" "+str(corr)+"</pre>",parse_mode=telegram.ParseMode.HTML)
    #update.message.reply_text("<pre>"+options[2]+"</pre>",parse_mode=telegram.ParseMode.HTML)
    #update.message.reply_text("<pre>"+options[3]+"</pre>",parse_mode=telegram.ParseMode.HTML)
    #update.message.reply_text("<pre>"+options[4]+"</pre>",parse_mode=telegram.ParseMode.HTML)
    #update.message.reply_text("<pre>"+options[5]+"</pre>",parse_mode=telegram.ParseMode.HTML)
    #update.message.reply_text("<pre>"+options[6]+"</pre>",parse_mode=telegram.ParseMode.HTML)
    #update.message.reply_text("<pre>"+options[7]+"</pre>",parse_mode=telegram.ParseMode.HTML)
    #update.message.reply_text("<pre>"+options[8]+"</pre>",parse_mode=telegram.ParseMode.HTML)
    #update.message.reply_text("<pre>"+options[9]+"</pre>",parse_mode=telegram.ParseMode.HTML)
    #update.message.reply_text("<pre>"+cor+"</pre>",parse_mode=telegram.ParseMode.HTML)
    
    if ex is None:
        update.effective_message.reply_poll(
            question= q,
            options=options,
            # with is_closed true, the poll/quiz is immediately closed
            type=Poll.QUIZ,
            correct_option_id =corr,
            #explanation=Ex,
            is_closed=False,
            is_anonymous=False,
            reply_markup=ReplyKeyboardRemove()
    )
    else:
        update.message.reply_text("<pre>"+Ex+"</pre>",parse_mode=telegram.ParseMode.HTML)
        update.effective_message.reply_poll(
            question= q,
            options=options,
            # with is_closed true, the poll/quiz is immediately closed
            type=Poll.QUIZ,
            correct_option_id =corr,
            explanation=Ex,
            is_closed=False,
            is_anonymous=False,
            reply_markup=ReplyKeyboardRemove()
    )
    #update.message.reply_text("<pre>"+ex+"</pre>",parse_mode=telegram.ParseMode.HTML)








@run_async
@send_typing_action
def help_handler(update, context):
    """Display a help message"""
    update.message.reply_text("Use /quiz, /poll or /preview to test this " "bot." )
    update.message.reply_text("created by Mohit Sharma" )
    update.message.reply_text("send me a POLL" )
    update.message.reply_text(" I CAN CREATE.\n\n30 voting poll. \n             &\n OCR thing compcompletely shut down." )


def main():
    bot_token=os.environ.get("BOT_TOKEN", "")
    updater = Updater(bot_token,use_context=True)
    dp = updater.dispatcher
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
    updater.idle()
    
if __name__ == '__main__':
    main()
