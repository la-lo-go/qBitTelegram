import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telegram.ext import ContextTypes

import client


def create_keyboard(data: dict, type="") -> InlineKeyboardMarkup:
    keyboard = []
    if type != "":
        type = f'[{type}]'
    
    for key, value in data.items():
        key = str(key) # make sure that the key is not a number
        keyboard.append([InlineKeyboardButton(value, callback_data=type+key)])
        
    return InlineKeyboardMarkup(keyboard)

async def button_torrent(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    await query.answer()
    
    text = data_from_CQ(query.data, type="TORRENT")

    await query.edit_message_text(text=f"Selected torrent: {text}")
    
async def button_category(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    await query.answer()
    
    text = data_from_CQ(query, type="CATEGORY")

    await query.edit_message_text(text=f"Selected category: {text}")
    
async def button_category_download(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    await query.answer()
    
    text = data_from_CQ(query, type="DOWNLOAD")
    
    await client.download_magnet_when_category_selected(query, text, update)

async def button_general(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    await query.answer()
    await query.edit_message_text(text=f"Selected option: {query.data}")

def data_from_CQ(query: CallbackQuery, type) -> str:
    """Get the data from the callback query of the button"""
    data = query.data.replace(f'[{type}]', '', 1)
    logging.info(f'{query.from_user.username} - Buttom pressed [{type}]: {data}')
    return data