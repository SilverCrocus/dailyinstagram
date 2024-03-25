from instagrapi import Client
from dotenv import load_dotenv
import os


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

def read_daily_count():
    count = os.getenv('DAILY_COUNT')
    if count is None:
        count = 1
    else:
        count = int(count)
    return count

def update_daily_count(count):
    # Update the DAILY_COUNT environment variable in the runtime
    os.environ['DAILY_COUNT'] = str(count)
    
    # Read the existing contents of the .env file
    with open('.env', 'r') as f:
        lines = f.readlines()
    
    # Update the DAILY_COUNT variable in the lines
    updated_lines = []
    for line in lines:
        if line.startswith('DAILY_COUNT='):
            updated_lines.append(f'DAILY_COUNT={count}\n')
        else:
            updated_lines.append(line)
    
    # Write the updated contents back to the .env file
    with open('.env', 'w') as f:
        f.writelines(updated_lines)

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