from instagrapi import Client
from dotenv import load_dotenv
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import json


load_dotenv()
# Google Sheets settings
SHEET_ID = '1eTxDe5y7OdMU2sUNQJlyBve5MMxczBycGQNyK1u_mdo'
SHEET_NAME = 'daily_count_sheet'
RANGE_NAME = 'A2:B2'  # Assuming your keys and values are in columns A and B



def upload_reel(daily_count):
    # Authenticate with Instagram
    client = Client()
    client.login(username=os.getenv("IG_USERNAME"), password=os.getenv("IG_PASSWORD"))

    # Upload the reel
    reel_path = "video/whatareyoudoing.mp4"
    caption = f"Day {daily_count}: What are you doing\n\n#ITZY #itzy #lia #midzy #yuna #ryujin #yeji #chaeryeong #borntobe #itzylia #itzyyuna #itzyyeji #itzyryujin #itzychaeryeong"
    media = client.clip_upload(reel_path, caption=caption)

    # # Add the uploaded reel to the story
    # client.photo_upload_to_story(
    #     media.thumbnail_url,
    #     links=[f"https://www.instagram.com/p/{media.code}/"]
    # )


# Authenticate with the Google Sheets API
# Get the service account JSON from an environment variable
service_account_info = json.loads(os.environ['GOOGLE_APPLICATION_CREDENTIALS_JSON'])

creds = Credentials.from_service_account_info(service_account_info)
service = build('sheets', 'v4', credentials=creds)

# Function to read the daily count
def read_daily_count():
    result = service.spreadsheets().values().get(spreadsheetId=SHEET_ID,
                                                  range=RANGE_NAME).execute()
    values = result.get('values', [])

    # Find the daily_count value
    if not values:
        return 1  # Default value if not found or list is empty
    if values[0][0] == 'DAILY_COUNT':
        return int(values[0][1])
    return 1

# Function to update the daily count
def update_daily_count(count):
    value_range_body = {
        "values": [
            ['DAILY_COUNT', count]
        ]
    }
    service.spreadsheets().values().update(
        spreadsheetId=SHEET_ID,
        range='A2:B2',  # Specify the exact cells for daily_count
        valueInputOption='RAW',
        body=value_range_body
    ).execute()

def main():
    # Read the current daily count from a file
    daily_count = read_daily_count()

    # Increment the daily count
    daily_count += 1

    # Update the file with the new daily count
    update_daily_count(daily_count)

    # Upload the reel to Instagram
    upload_reel(daily_count)

if __name__ == "__main__":
    main()