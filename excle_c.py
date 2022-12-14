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

# [START sheets_quickstart]
from __future__ import print_function
import  re as reaaa
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/documents']

# '15yw6CLCsqhaU97cyg_l-GWf_Np-njLfr/ The ID and range of a sample spreadsheet.
 



def main(y):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    SAMPLE_SPREADSHEET_ID =y
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('responce.json'):
        creds = Credentials.from_authorized_user_file('responce.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets_responce.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('responce.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)
        
        
        sheet = service.spreadsheets()
        res=sheet.get(spreadsheetId=SAMPLE_SPREADSHEET_ID).execute()
        SAMPLE_RANGE_NAME = 'B:C'#+int(res.sheets.properties.gridProperties.columnCount)
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])
        service = build('drive', 'v3', credentials=creds)
        req = service.files().get(fileId=SAMPLE_SPREADSHEET_ID).execute()
        
        if not values:
            print('No data found.')
            return
        li=[]
        data=[]
        #print((values))
        for i in range(1,len(values)):
            li.append([int(reaaa.sub(" / \d{,}","",values[i][0])),i])
        li.sort(reverse=True)
        data.append(values[0])
        for x in range(len(li)):
            data.append(values[li[x][1]])
        return data,reaaa.sub("\'|\!.*","",req.get('name', None))
        #for row in values:
#            # Print columns A and E, which correspond to indices 0 and 4.
#            print('%s, %s' % (row[0], row[4]))
    except HttpError as err:
        print(err)


    
# [END sheets_quickstart]