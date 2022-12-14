# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START apps_script_api_quickstart]
"""
Shows basic usage of the Apps Script API.
Call the Apps Script API to create a new script project, upload a file to the
project, and log the script's URL to the user.
"""
from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import errors
from googleapiclient.discovery import build

# If modifying these scopes, delete the file gform.json.
SCOPES = ['https://www.googleapis.com/auth/script.projects','https://www.googleapis.com/auth/documents','https://www.googleapis.com/auth/drive',"https://www.googleapis.com/auth/forms"]



def main_run(x):
    """Calls the Apps Script API.
    """
    creds = None
    
    # The file gform.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    
    script_id='AKfycbzhOMgs5TL0pmDEoh-aZAv6PobvzqNVloFwoHHVGC-bh3KSvFq65RTuT3JtyunEFTP8'
    script_id='AKfycbzRUw4Wi3LBDT9RdStszy5KOCCH0-TZy8n3jeJr_LI'
    if os.path.exists('gform.json'):
        creds = Credentials.from_authorized_user_file('gform.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('gform.json', 'w') as token:
            token.write(creds.to_json())#

    if True:
        service = build('script', 'v1', credentials=creds)

        # Call the Apps Script API
        # Create a new project
        #request = {'title': 'My Script'}
        #response = service.projects().create(body=request).execute()
        request = {"function": x}

        # Upload two files to the project
        
        response = service.scripts().run(
            body=request,
            scriptId=script_id).execute()
        return response
        #request = {"function": "getFoldersUnderRoot"}
        
    


def main4(x):
    """Calls the Apps Script API.
    """
    SAMPLE_MANIFEST = '''
{
  "timeZone": "Asia/Kolkata",
  "dependencies": {},
  "exceptionLogging": "STACKDRIVER",
  "runtimeVersion": "V8",
  "oauthScopes": [
"https://www.googleapis.com/auth/spreadsheets.readonly",
"https://apps-apis.google.com/a/feeds",
"https://www.googleapis.com/auth/drive.readonly",
"https://www.googleapis.com/auth/forms"
],
  "executionApi": {
    "access": "ANYONE"
  }
}
'''.strip()
    creds = None
    SAMPLE_CODE = x.strip()
    # The file gform.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    script_id='1R1SA2KXo8TGZF1gacM7dnRn6iii1cRx8-L5hfEi-aUxuycnRQ6OvECTm'
    if os.path.exists('gform.json'):
        creds = Credentials.from_authorized_user_file('gform.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('gform.json', 'w') as token:
            token.write(creds.to_json())#

    if True:
        service = build('script', 'v1', credentials=creds)

        # Call the Apps Script API
        # Create a new project
        request = {'title': 'Test1'}
        #response = service.projects().create(body=request).execute()
        

        # Upload two files to the project
        request = {
            'files': [{
                'name': 'hello',
                'type': 'SERVER_JS',
                'source': SAMPLE_CODE
            }, {
                'name': 'appsscript',
                'type': 'JSON',
                'source': SAMPLE_MANIFEST
            }]
        }
        response = service.projects().updateContent(
            body=request,
            scriptId=script_id).execute()
        return ('https://script.google.com/d/' + script_id + '/edit')
        #request = {"function": "getFoldersUnderRoot"}
        
    