import os
import qbittorrentapi
import json
import re
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import ContextTypes

import keyboard
from models.Message import Message
from models.Torrent import Torrent


load_dotenv()


QBT_CLIENT = qbittorrentapi.Client(
        host=os.getenv('QBIT_HOST'),
        port=os.getenv('QBIT_PORT'),
        username=os.getenv('QBIT_USERAME'),
        password=os.getenv('QBIT_PASS'),
    )

ADMINS = json.loads(str(os.getenv('ADMINS')))

# DICTIONARY TO STORE THE LAST MESSAGE OF THE USERS
# USING THE USER ID AS KEY
MESSAGES = {}
    
async def show_all_torrents(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Get all torrents torrents and show them in a keyboard dialog"""
    
    torrents_info = QBT_CLIENT.torrents_info()
    await show_torrents(update, torrents_info)
        
async def show_downloading_torrents(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Get downloading torrents and show them in a keyboard dialog"""
    
    torrents_info = QBT_CLIENT.torrents_info()
    
    # Filter the torrents that are not downloading (independently of the state)
    torrents_info_downloading = filter(lambda torrent: torrent['amount_left'] > 0, torrents_info)
    await show_torrents(update, torrents_info_downloading)
    
async def show_torrents(update: Update, torrents_info) -> None:
    """Create the keyboard object with the torrent hash as key and name as value"""
    torrents_data = {torrent['hash']: format_name(torrent['name']) for torrent in torrents_info}
    reply_markup = keyboard.create_keyboard(torrents_data, type="TORRENT")
    
    if len(torrents_data) == 0:
        await update.message.reply_text("No torrents found")
    else:
        await update.message.reply_text("Select an torrent:", reply_markup=reply_markup)
    
    
async def show_categories(update: Update, download_torrent=False) -> None:
    categories = QBT_CLIENT.torrents_categories()
    categories_data = {key: value['savePath'] for key, value in categories.items()}
    
    # If the download_torrent flag is set to True then the download 
    # of the last torrent sent to the server will be initialized
    type = "DOWNLOAD" if download_torrent else "CATEGORY"
    
    reply_markup = keyboard.create_keyboard(categories_data, type=type)
    
    await update.message.reply_text("Select a category:", reply_markup=reply_markup)
    
async def manage_magnet(update: Update):
    await update.message.reply_text('Magnet link detected')
    torrentObj = Torrent(update.message.text)
    MESSAGES[update.effective_chat.id] = Message("TORRENT", torrentObj)
    await show_categories(update, True)
    
async def download_magnet_when_category_selected(callBackQuery, category:str, update: Update):
    torrent = MESSAGES[update.effective_chat.id].data
    torrent.category = category
    QBT_CLIENT.torrents_add(urls=torrent.magnet, category=category)
    
    await callBackQuery.edit_message_text(f'Torrent added to category {category}')
    

def format_name(name, max_length=50):
    """
        removes the content between parentheses and square brackets 
        and returns the first max_length characters
    """
    clean_name = re.sub(r'\([^()]*\)|\[[^][]*\]', '', name).strip()
    
    return clean_name[:max_length] + '...' if len(clean_name) > max_length else clean_name

    