import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'credentia.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#upload_date_time = datetime.datetime(2022, 2, 16, 22, 56, 0).isoformat() + '.000Z'
def yootube(anime):
    request_body = {
        'snippet': {
            'categoryI': 19,
            'title': 'Upload',
            'description': 'kiendly subscribe my yourbe channal \nWe upload Anime...',
            'tags': ['Travel', 'video test', 'Travel Tips']
        },
        'status': {
            'privacyStatus': 'private',
            #'publishAt': upload_date_time,
            'selfDeclaredMadeForKids': False, 
        },
        'notifySubscribers': False
    }
    
    mediaFile = MediaFileUpload(anime)
    
    response_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()
    

#service.thumbnails().set(
#    videoId=response_upload.get('id'),
#    media_body=MediaFileUpload('thumbnail.png')
#).execute()