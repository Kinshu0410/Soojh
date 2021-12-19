from pymongo import MongoClient
from telegram import Update, ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup, ReplyKeyboardRemove, ParseMode
from telegram.ext import CallbackContext
import random
import string
import requests

client=MongoClient('mongodb+srv://Kinshu04101:Qwert123@cluster0.ckcyx.mongodb.net/test?retryWrites=true&w=majority')
quizlists = client.QuizList.quizlist
'''
{
    "quiz_name":"Quiz Name",
    "quiz_id":"Unique ID",
}
'''

photos = client.User_Photos.photos
'''
{
    "chat_id":123456789,

    "photo_url":"https://i.imgur.com/...",

    "deletehash":"..."
}
'''


async def save_results(collection_name,update:Update,context:CallbackContext):
    if quizlists.find_one({"quizname":collection_name}) is None:
        unique_id = id_generator()
        quizlists.insert_one({
            "quizid":unique_id,
            "quizname":collection_name
        })
    else:
        unique_id = quizlists.find_one({"quizname":collection_name})["quizid"]
        keyboard = [
                [
                    InlineKeyboardButton("Play Quiz", callback_data='3',url="https://telegram.me/Soojhboojh_01bot?start=Play"+unique_id),
                    InlineKeyboardButton("Result", callback_data='2',url="https://quizresults.cf/"+unique_id),],[
        #],[
        InlineKeyboardButton("Play in Group", callback_data='1',url="https://telegram.me/Soojhboojh_01bot?startgroup=Share"+unique_id),
                ],
            ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=update.message.chat.id,text='<b>'+collection_name+'</b>', reply_markup=reply_markup,parse_mode=ParseMode.HTML)
    unique_url=(f"https://quizresults.cf/{unique_id}")
    return unique_url
    
# function to generate random string containing letter of length n
def id_generator(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

async def save_photos(collection_name,update:Update,context:CallbackContext):
    db = client.get_database("Results")
    results_coll = db.quizresults

    update.message.reply_text("Saving photos, please wait ...")
    quiz_results = results_coll.find({'quizname':collection_name})

    for result in quiz_results:
        user_id = result['userid']

        if photos.find_one({"chat_id":user_id}) is not None:
            continue 

        try:                
            data = generate_imgur_link(user_id,context)
            photos.insert_one({
                "chat_id":user_id,
                "imgur_id":data['id'],
                "photo_url":data['link'],
                "deletehash":data['deletehash']
            })
        except Exception as e:
            print(e)
            continue

    update.message.reply_text("Photos saved successfully")
                  
def generate_imgur_link(chat_id,context:CallbackContext):
    photo_file_id = context.bot.get_user_profile_photos(chat_id,limit=1).photos[0][-1].file_id
    photo_url = context.bot.get_file(photo_file_id).file_path
    url = "https://api.imgur.com/3/image"
    payload={'image': photo_url}
    headers = {'Authorization': 'Client-ID 78c294224667a7a'}

    response = requests.request("POST", url,headers=headers, data=payload).json()
    imgur_link = response['data']['link']
    delete_hash = response['data']['deletehash']
    imgur_id = response['data']['id']

    return {"link":imgur_link,"deletehash":delete_hash,"id":imgur_id}

async def save_user_photo(chat_id,context:CallbackContext):
    if photos.find_one({"chat_id":chat_id}) is None:
        data = generate_imgur_link(chat_id,context)
        photos.insert_one({
            "chat_id":chat_id,
            "imgur_id":data['id'],
            "photo_url":data['link'],
            "deletehash":data['deletehash']
        })
