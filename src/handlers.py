from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, CallbackQueryHandler, CommandHandler, filters
import logging

import keyboard
import client


def add_handlers(bot):
    # Comands
    bot.add_handler(CommandHandler('start', start))
    bot.add_handler(CommandHandler('torrents', client.show_all_torrents))
    bot.add_handler(CommandHandler('torrents_downloading', client.show_downloading_torrents))
    bot.add_handler(CommandHandler('categories', client.show_categories))
    bot.add_handler(CommandHandler('full_report', client.full_report))

    # CallbacksQueryHandlers Buttons
    bot.add_handler(CallbackQueryHandler(keyboard.button_torrent, pattern=r'^\[TORRENT\](.*)'))
    bot.add_handler(CallbackQueryHandler(keyboard.button_category, pattern=r'^\[CATEGORY\](.*)'))
    bot.add_handler(CallbackQueryHandler(keyboard.button_category_download, pattern=r'^\[DOWNLOAD\](.*)'))
    bot.add_handler(CallbackQueryHandler(keyboard.button_general))
    
    # Teext mesagges
    bot.add_handler(MessageHandler(filters.TEXT, manage_text))
    
def start_handlers():
    return [
        CommandHandler('start', start),
        MessageHandler(None, start),
    ]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ## Create a text explaining the bot
    text = "Welcome to the QbitTelegram Bot!\n\n"
    text += "You can use the following commands:\n"
    text += "/torrents - Show all torrents\n"
    text += "/torrents_downloading - Show downloading torrents\n"
    text += "/categories - Show all categories\n"
    text += "/full_report - Show full report of the status of the torrents\n"

    # print the username
    user = update.effective_user.username
    if not is_admin(user):
        kick(context, update.effective_chat.id)
        
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text
    )

async def manage_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text
    username = update.effective_user.username
    
    if(is_admin(username)):
        if(is_magnet(message_text)):
            await client.manage_magnet(update)
        else:
            # Echo the message
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=message_text
            )
    else:
        print("NOT AN ADMIN")
        await kick(context, update.effective_chat.id)
    
def is_admin(user_name : str) -> bool:
    return user_name in client.ADMINS

def is_magnet(message: str) -> bool:
    return message.startswith('magnet:?xt=')

async def kick(context: ContextTypes.DEFAULT_TYPE, user_id: str) -> None:
    await context.bot.send_message(
            chat_id=user_id,
            text=f'You are not authorized to use this bot'
        )
    
    # Block the user
    await context.bot.kick_chat_member(
        chat_id=user_id,
        user_id=user_id
    )

