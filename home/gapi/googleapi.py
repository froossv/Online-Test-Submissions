import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/drive']

def getService(serviceName):
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle','rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if  creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(os.path.join(os.path.dirname(os.path.abspath(__file__)),'credentials.json'), SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return build(serviceName,'v3',credentials=creds)