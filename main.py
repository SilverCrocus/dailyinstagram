from instagrapi import Client
from dotenv import load_dotenv
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import json
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ColorClip

load_dotenv()
# Google Sheets settings
SHEET_ID = '1eTxDe5y7OdMU2sUNQJlyBve5MMxczBycGQNyK1u_mdo'
SHEET_NAME = 'daily_count_sheet'
RANGE_NAME = 'A3:B3'  # Assuming your keys and values are in columns A and B

# Authenticate with the Google Sheets API
# Get the service account JSON from an environment variable
service_account_info = json.loads(os.getenv('GOOGLE_APPLICATION_CREDENTIALS_JSON'))

creds = Credentials.from_service_account_info(service_account_info)
service = build('sheets', 'v4', credentials=creds)

def add_text_to_video(video_path, text, output_path):
    # Load the video
    clip = VideoFileClip(video_path)
    
    # Create a text clip
    txt_clip = TextClip(text, fontsize=70, color='white', font='Arial-Bold', align='West')
    
    # Calculate text size and position
    txt_w, txt_h = txt_clip.size
    padding = 20  # Space around text
    pos_x = clip.size[0] / 4 - txt_w / 2  # Middle of the left half of the video
    pos_y = 3 * clip.size[1] / 4 - txt_h / 2  # Middle of the bottom half of the video
    
    # Create a semi-transparent background
    bg_clip = ColorClip(size=(txt_w + 20, txt_h + 20), color=(0,0,0,128), ismask=False)  # Width + 20px padding, Height + 20px padding
    
    # Set the position of background and text
    bg_clip = bg_clip.set_position((pos_x - 10, pos_y - 10)).set_duration(clip.duration)
    txt_clip = txt_clip.set_position((pos_x, pos_y)).set_duration(clip.duration)
    
    # Overlay text on a semi-transparent background on the original video
    video = CompositeVideoClip([clip, bg_clip, txt_clip], size=clip.size)
    
    # Write the result to a file
    video.write_videofile(output_path, codec='libx264', audio_codec='aac')

def upload_reel(daily_count):
    # Authenticate with Instagram
    client = Client()
    client.login(username=os.getenv("IG_USERNAME"), password=os.getenv("IG_PASSWORD"))
    # Path to the original video
    reel_path = "video/whatareyoudoing.mp4"
    # Path for the output video with text
    output_path = "video/whatareyoudoing_with_text.mp4"
    # Add text to the video
    caption_text = f"Day {daily_count}"
    add_text_to_video(reel_path, caption_text, output_path)
    # Updated caption for the post
    caption = f"Day {daily_count}: What are you doing\n\n#ITZY #itzy #lia #midzy #yuna #ryujin #yeji #chaeryeong #borntobe #itzylia #itzyyuna #itzyyeji #itzyryujin #itzychaeryeong"
    # Upload the edited video
    media = client.clip_upload(output_path, caption=caption)

def read_daily_count():
    result = service.spreadsheets().values().get(spreadsheetId=SHEET_ID,
                                                  range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        return 1  # Default value if not found or list is empty
    if values[0][0] == 'DAILY_COUNT':
        return int(values[0][1])
    return 1

def update_daily_count(count):
    value_range_body = {
        "values": [
            ['DAILY_COUNT', count]
        ]
    }
    service.spreadsheets().values().update(
        spreadsheetId=SHEET_ID,
        range='A3:B3',  # Specify the exact cells for daily count
        valueInputOption='RAW',
        body=value_range_body
    ).execute()

def main():
    # Read the current daily count
    daily_count = read_daily_count()
    # Increment the daily count
    daily_count += 1
    # Update the sheet with the new daily count
    update_daily_count(daily_count)
    # Upload the reel to Instagram
    upload_reel(daily_count)

if __name__ == "__main__":
    main()
