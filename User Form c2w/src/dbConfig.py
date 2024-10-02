from google.cloud import firestore
import json
#firestore database configuration
credentials_path ='USER INFO FORM APPLICATION/setup/user-form-c2w-cb700-firebase-adminsdk-vhztl-7416670186.json'
with open(credentials_path) as json_file:
    credentials_info = json.load(json_file)
db = firestore.Client.from_service_account_info(credentials_info)