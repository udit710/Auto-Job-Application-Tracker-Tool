
import ast
import os
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import datetime
import config

def update_sheet(genData, link):

    # Define the scope
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    # Set up credentials
    creds = Credentials.from_service_account_file('credentials.json', scopes=scopes)
    client = gspread.authorize(creds)

    # Open the Google Sheet
    sheet = client.open_by_key(os.getenv('SHEET_ID'))

    # process the data
    genData = ast.literal_eval(genData)
    df = pd.DataFrame(sheet.worksheet("Sheet3").get_all_records())
    data = {
        "No":len(df)+1,
        "Role":genData["Role"],
        "Company":genData["Company"],
        "Skills":genData["Skills"],
        "Platform":genData["Platform"],
        "Link":link,
        "Applied": datetime.datetime.now().strftime("%d/%m/%y"),
        "Follow":"", 
        "Response?":""
        }

    # print(data)
    
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)

    # Update the Google Sheet
    sheet.worksheet("Sheet3").update([df.columns.values.tolist()] + df.values.tolist())