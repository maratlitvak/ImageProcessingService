import os
import polybot.bot

if __name__ == '__main__':
    TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
    TELEGRAM_APP_URL = os.environ['TELEGRAM_APP_URL']
    polybot.bot .ImageProcessingBot(TELEGRAM_TOKEN, TELEGRAM_APP_URL)


