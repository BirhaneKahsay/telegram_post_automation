# Social Media Post Automation

An automated solution to post images with captions to Telegram and Facebook. This project allows you to schedule and automate content posting across multiple social media platforms.

## Overview

This automation tool:
- ✅ Posts random images from a local folder to Telegram groups
- ✅ Posts random images to Facebook pages
- ✅ Reads captions from a text file
- ✅ Logs all posts with timestamps
- ✅ Supports environment-based configuration
- ✅ Can be scheduled using cron jobs (APScheduler)

## Project Structure

```
automation/
├── main.py              # Main posting functions for Telegram and Facebook
├── config.py            # Configuration settings (loads from .env)
├── helper.py            # Helper functions for captions, bot instance, and credentials
├── captions/
│   └── caption.txt      # Text file containing captions to be posted
├── images/              # Folder containing images to post
├── post_log.txt         # Log file tracking all posts made
└── README.md            # This file
```

## Features

### Telegram Integration
- Sends images with captions to a Telegram group
- Uses the python-telegram-bot library
- Async support for non-blocking operations

### Facebook Integration
- Posts images with captions to a Facebook page
- Uses Facebook Graph API
- HTTP-based integration with error handling

### Logging
- Maintains a `post_log.txt` file with timestamps
- Logs image name, caption, and posting time for each post

### Scheduling (Optional)
- Uses APScheduler for cron-based scheduling
- Can be configured to post at specific times daily

## Setup & Installation

### Prerequisites
- Python 3.8+
- `.env` file with credentials

### Installation Steps

1. **Clone/Download the project**
   ```bash
   cd automation
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install python-telegram-bot
   pip install requests
   pip install apscheduler
   pip install pydantic-settings
   ```

3. **Create a `.env` file** in the project root with your credentials:
   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   TELEGRAM_CHAT_ID=your_telegram_group_id
   FACEBOOK_PAGE_ID=your_facebook_page_id
   FACEBOOK_PAGE_ACCESS_TOKEN=your_facebook_access_token
   ```

4. **Prepare your content**
   - Add images to the `images/` folder
   - Add captions to `captions/caption.txt`

## Usage

### Manual Posting

**Post to Telegram:**
```bash
python main.py
```

This will pick a random image and caption, then post to Telegram.

**Post to Facebook:**
Modify `main.py` to call `asyncio.run(post_on_facebook())` instead.

### Scheduled Posting

Uncomment the scheduler section in `main.py` to enable automatic posting:

```python
if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(post_to_telegram, 'cron', hour=22, minute=0)
    print("Telegram file-based poster started...")
    scheduler.start()
```

This will post daily at 22:00 (10 PM).

## Configuration Details

### config.py
Defines the settings using Pydantic BaseSettings:
- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
- `TELEGRAM_CHAT_ID`: Target Telegram group ID
- `FACEBOOK_PAGE_ID`: Your Facebook page ID
- `FACEBOOK_PAGE_ACCESS_TOKEN`: Facebook page access token

### helper.py Functions

- `get_bot_group_id()`: Retrieves the Telegram chat ID from config
- `load_captions(file_path)`: Loads captions from the specified file
- `get_bot()`: Returns a configured Telegram Bot instance
- `get_facebook_credentials()`: Returns Facebook credentials

## How It Works

1. **Image Selection**: Randomly selects an image from the `images/` folder
2. **Caption Loading**: Reads a caption from `captions/caption.txt`
3. **Posting**: Posts the image with caption to selected platform(s)
4. **Logging**: Records the post details with timestamp to `post_log.txt`

## Credentials & Security

- All credentials are stored in a `.env` file (not version controlled)
- The `.env` file should be added to `.gitignore`
- Never commit your tokens or access keys to version control

### How to Get Credentials

**Telegram Bot Token:**
- Chat with BotFather on Telegram
- Create a new bot and copy the token

**Telegram Chat/Group ID:**
- Add the bot to your group
- Get the group ID from the environment variable

**Facebook Credentials:**
- Go to Facebook Developers
- Create an app and get the Page Access Token
- Get your Page ID from your Facebook page settings

## Logging

All posts are logged to `post_log.txt` with the format:
```
2026-06-22 15:30:45.123456 | Posted: image_name.jpg | Caption: Your caption here
```

## Error Handling

- Checks if images folder is empty
- Checks if captions file exists
- Validates HTTP responses from Facebook API
- Handles Telegram async operations gracefully

## Future Enhancements

- Add support for multiple caption types
- Database integration for caption management
- Web dashboard for scheduling
- Support for other platforms (Instagram, Twitter)
- Image optimization before posting
- Advanced scheduling rules

## License

This project is provided as-is for personal use.

## Support

For issues or questions, refer to the inline code comments and the helper functions documentation.
