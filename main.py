import os
import random
import asyncio
import datetime
from urllib import response
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
from helper import get_bot_group_id, load_captions, get_bot, get_facebook_credentials


from helper import get_bot_group_id

caption_file = "captions/caption.txt"
images_folder = "images/"

async def post_to_telegram():
    # Get the bot group id
    group_id = await get_bot_group_id()
    

    # Load captions from the text file
    captions = load_captions(file_path=caption_file)

    if not captions:
        print("No captions found in the file.")
    if not os.listdir(images_folder):
        print("No images found. Skipping post.")
        return
    
    image = random.choice(os.listdir(images_folder))
    image_path = os.path.join(images_folder, image)

    with open(image_path, "rb") as photo:
        bot = get_bot()
        await bot.send_photo(chat_id=group_id, photo=photo, caption=captions)

    log_message = f"{datetime.datetime.now()} | Posted: {image} | Caption: {captions}\n"
    with open("post_log.txt", "a", encoding="utf-8") as log:
        log.write(log_message)



# if __name__ == "__main__":
#     scheduler = BlockingScheduler()
#     scheduler.add_job(post_to_telegram, 'cron', hour=22, minute=0)
#     print("Telegram file-based poster started...")
#     scheduler.start()

async def post_on_facebook():
    captions = load_captions(file_path=caption_file)
    FACEBOOK_PAGE_ID, FACEBOOK_PAGE_ACCESS_TOKEN = get_facebook_credentials()

    if not captions:
        print("No captions found in the file.")
    if not os.listdir(images_folder):
        print("No images found. Skipping post.")
        return
    
    image = random.choice(os.listdir(images_folder))
    image_path = os.path.join(images_folder, image)


    url = f"https://graph.facebook.com/{FACEBOOK_PAGE_ID}/photos"

    data = {
        "caption": captions,
        "access_token": FACEBOOK_PAGE_ACCESS_TOKEN
    }

    try:
        with open(image_path, "rb") as photo:
            files = {
                "source": photo
            }
            response = requests.post(url, data=data, files=files)
            response.raise_for_status()

            print(response.json())

            if response.status_code == 200:
                print("Photo posted successfully on Facebook.")
    except requests.HTTPError as e:
        print(f"Error posting to Facebook: {e.response.text}")
        return

if __name__ == "__main__":
    asyncio.run(post_to_telegram())