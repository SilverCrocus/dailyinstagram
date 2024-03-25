from instagrapi import Client
from dotenv import load_dotenv
import os
import requests

load_dotenv()

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

# Load environment variables from Render
DAILY_COUNT = os.getenv('DAILY_COUNT')
RENDER_API_KEY = os.getenv('RENDER_API_KEY')
RENDER_SERVICE_ID = os.getenv('RENDER_SERVICE_ID')

def read_daily_count():
    if DAILY_COUNT is None:
        count = 1
    else:
        count = int(DAILY_COUNT)
    return count

def update_daily_count(count):
    # Update the DAILY_COUNT environment variable on Render
    url = f'https://api.render.com/v1/services/{RENDER_SERVICE_ID}/env-vars'
    headers = {
        'Authorization': f'Bearer {RENDER_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'envVars': [
            {
                'key': 'DAILY_COUNT',
                'value': str(count)
            }
        ]
    }
    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 200:
        print('DAILY_COUNT environment variable updated on Render')
    else:
        print('Failed to update DAILY_COUNT environment variable on Render')

def main():
    # Read the current daily count
    daily_count = read_daily_count()

    # Increment the daily count
    daily_count += 1

    # Update the daily count on Render
    update_daily_count(daily_count)

    try:
        # Upload the reel to Instagram
        upload_reel(daily_count)

    except Exception as e:
        print(f'An error occurred: {str(e)}')
        # Handle the exception or log the error
        # ...

if __name__ == "__main__":
    main()