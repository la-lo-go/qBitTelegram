import logging
import os
from telegram.ext import ApplicationBuilder
import qbittorrentapi
from handlers import add_handlers
from client import QBT_CLIENT


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')  # clear console
    
    # Qbittorrent
    try:
        QBT_CLIENT.auth_log_in()
        logging.info('Qbittorrent connection successful')
    except qbittorrentapi.LoginFailed as e:
        logging.error('Qbittorrent connection failed' + str(e))


    # Telegram
    try:
        bot = ApplicationBuilder().token(os.getenv('TELEGRAM_TOKEN')).build()
        logging.info('Telegram connection successful')
    except Exception as e:
        logging.error('Telegram connection failed: ' + str(e))

    add_handlers(bot)
    bot.run_polling()
