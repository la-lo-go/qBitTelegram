import os
import re

import qbittorrentapi
from telegram import Update, constants
from telegram.ext import ContextTypes

import keyboard
from models.Message import Message
from models.Torrent import Torrent
from utils.State import append_emoji_to_state


QBT_CLIENT = qbittorrentapi.Client(
        host=os.getenv('QBIT_HOST'),
        port=os.getenv('QBIT_PORT'),
        username=os.getenv('QBIT_USERAME'),
        password=os.getenv('QBIT_PASS'),
    )

ADMINS = os.getenv('ADMINS').split(',')

# DICTIONARY TO STORE THE LAST MESSAGE OF THE USERS
# USING THE USER ID AS KEY
MESSAGES = {}
    
async def show_all_torrents(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Get all torrents torrents and show them in a keyboard dialog"""
    
    torrents_info = QBT_CLIENT.torrents_info()
    await show_torrents_info(update, torrents_info)
        
async def show_downloading_torrents(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Get downloading torrents and show them in a keyboard dialog"""
    
    torrents_info = QBT_CLIENT.torrents_info()
    
    # Filter the torrents that are not downloading (independently of the state)
    torrents_info_downloading = filter(lambda torrent: torrent['progress'] < 1, torrents_info)
    await show_torrents_info(update, torrents_info_downloading)
    
async def show_torrents_info(update: Update, torrents_info) -> None:
    """Create the keyboard object with the torrent hash as key and name as value"""
    torrents_data = {torrent['hash']: format_name(torrent) for torrent in torrents_info}
    reply_markup = keyboard.create_keyboard(torrents_data, type="TORRENT")
    
    if len(torrents_data) == 0:
        await update.message.reply_text("No torrents found")
    else:
        await update.message.reply_text("Select an torrent:", reply_markup=reply_markup)
    
async def show_categories(update: Update, download_torrent=False) -> None:
    """Show all the categories whith their path."""
    categories = QBT_CLIENT.torrents_categories()
    categories_data = {key: value['savePath'] for key, value in categories.items()}
    
    # If the download_torrent flag is set to True then the download 
    # of the last torrent sent to the server will be initialized
    type = "DOWNLOAD" if download_torrent else "CATEGORY"
    
    reply_markup = keyboard.create_keyboard(categories_data, type=type)
    
    await update.message.reply_text("Select a category:", reply_markup=reply_markup)
    
async def full_report(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show a full report of the status of the torrents"""
    torrents_info = QBT_CLIENT.torrents_info(sort='added_on', reverse=True)
    text = ""
    for torrent in torrents_info:
        text += format_torrent_full_report(torrent)
    await update.message.reply_text(text, parse_mode=constants.ParseMode.HTML)
    
async def manage_magnet(update: Update) -> None:
    """
    Trigged when a new magnet link is received it updates the
    MESSAGES dictionary with the data and the user id. 
    At the end it shows all the categories.
    """
    await update.message.reply_text('Magnet link detected')
    torrentObj = Torrent(update.message.text)
    MESSAGES[update.effective_chat.id] = Message("TORRENT", torrentObj)
    await show_categories(update, True)
    
async def download_magnet_when_category_selected(callBackQuery, category:str, update: Update) -> None:
    """Download the torrent when a category is selected after sending the magnet"""
    torrent = MESSAGES[update.effective_chat.id].data
    torrent.category = category
    QBT_CLIENT.torrents_add(urls=torrent.magnet, category=category)
    
    await callBackQuery.edit_message_text(f'Torrent added to category {category}')
    

def format_name(torrent, max_length=30) -> str:
    """
    Removes the content between parentheses and square brackets,
    returns the first max_length characters and the porcentage
    """
    clean_name = re.sub(r'\([^()]*\)|\[[^][]*\]', '', torrent['name']).strip()
    
    clean_name = clean_name[:max_length] + '...' if len(clean_name) > max_length else clean_name
    
    porcentage = round(torrent['progress']*100, 1)
    
    #TODO: add the status message with a emoji
    
    return f'{clean_name} - {porcentage}%'

def format_torrent_full_report(torrent) -> str:
    """Format the torrent info to show it in the full report""" 
    progress = torrent["progress"]*100

    torrent_report = '<b>'+format_name(torrent, 70)+'</b>'
    torrent_report += f' - {append_emoji_to_state(torrent["state"])}'
    torrent_report += f' - {progress}%'
    
    if progress != 100:
        torrent_report += f' - Remaining: {seconds_to_human_readable(torrent["eta"])}'
    
    torrent_report += f' - Ratio: {torrent["ratio"]:.2f}\n\n'
    
    return torrent_report

def seconds_to_human_readable(seconds) -> str:
    """Convert seconds to human readable format"""
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    
    if days > 0:
        return f'{days}d {hours}h {minutes}m {seconds}s'
    elif hours > 0:
        return f'{hours}h {minutes}m {seconds}s'
    elif minutes > 0:
        return f'{minutes}m {seconds}s'
    else:
        return f'{seconds}s'

    