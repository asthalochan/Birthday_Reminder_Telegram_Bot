import threading
from datetime import datetime
import time
import sqlite3
import asyncio
from aiogram import Bot
from telegram.ext import *
import re

conn=sqlite3.connect("database.db",check_same_thread=False)
cursor = conn.cursor()


current_name = None
current_date = None
with open('bot_token.txt', 'r') as file:
        bot_token = file.read()



async def start_commmand(update, context):
    await update.message.reply_text("Hey there! If you'd like to set up a new reminder, just type /new. I'm here to help!")
    
async def dev_commmand(update, context):
    await update.message.reply_text(" Bot developed by Asthalochan  "
                                    " Contact: mohantaastha@gmail.com "
                                    " Copyright (c) 2023 Asthalochan ")
    
async def new_reminder(update, context):
    await update.message.reply_text('Whose birthday should I help you remind?')
    return 1


async def get_name(update,context):
    global current_name
    current_name = update.message.text
    await update.message.reply_text('When is the birthday? \nPlease give me the date in the format DD-MM ?')
    return 2


async def get_date(update,context):
    global current_date
    global cursor
    
    current_date = update.message.text
    #check date format
    def is_valid_date_format(date_string):
        pattern = r'^\d{2}-\d{2}$'
        if re.match(pattern, date_string):
            day, month = map(int, date_string.split('-'))
            if 1 <= month <= 12:
                if month in [4, 6, 9, 11] and 1 <= day <= 30:
                    return True
                elif month == 2 and 1 <= day <= 29:
                    return True
                elif month != 2 and 1 <= day <= 31:
                    return True
        return False
    
    while True:
        if is_valid_date_format(current_date):
            user_id = update.message.from_user.id 
        
            cursor.execute("SELECT * FROM user WHERE id = ?",(user_id,))
            
            if not cursor.fetchone():
                cursor.execute("INSERT INTO user (id) VALUES (?)",(user_id,))
                
            cursor.execute("INSERT INTO birthday_reminder (user_id, name, date, reminded) VALUES(?, ?, ?, ?)",(user_id, current_name, current_date,0 ))

            conn.commit()
            await update.message.reply_text("sure i will remined you.....")
            break
        else:
            await update.message.reply_text("Invalid date format ! Format should be  DD-MM (eg.- if the  b'date is 4th janauary than type- 04-01)")
            await update.message.reply_text("Type /start  To start over again ! ")
            break
    
    
    return ConversationHandler.END

async def cancel(update, context):
    await update.message.reply_text("Reminder conversation canceled.")
    return ConversationHandler.END
    

#reminder
def do_reminders():
    while True:
        current_date = datetime.now().strftime('%d-%m')
        
        cursor.execute("SELECT * FROM birthday_reminder WHERE strftime(date) = ? AND reminded = 0", (current_date,))
                      
        
        rows = cursor.fetchall()
        for row in rows:
            row_id = row[0]
            name = row[2]
            user_id = row[4]
            
            #msg sending
            async def send_telegram_message(bot_token, user_id, message):
                bot = Bot(token=bot_token)
                await bot.send_message(chat_id=user_id, text=message)
                

            async def main():
                
                target_user_id = user_id
                message = f"It's {name}'s birthday today!"
                
                await send_telegram_message(bot_token, target_user_id, message)

            asyncio.run(main())

            
            cursor.execute("UPDATE birthday_reminder SET reminded = 1 WHERE id = ? ",(row_id,))
            
            
            conn.commit()
        time.sleep(10)
        
    
        
            


conv_handler = ConversationHandler(
        entry_points=[CommandHandler("new", new_reminder)],
        states= {
            1:[MessageHandler(filters.TEXT, get_name)],
            2:[MessageHandler(filters.TEXT, get_date)]
            },
        
        fallbacks=[CommandHandler("cancel",cancel)]
        )





#####------run function------------------#########

application = Application.builder().token(bot_token).build()

    # Commands
    #start
    
application.add_handler(CommandHandler('start', start_commmand))
application.add_handler(CommandHandler('dev', dev_commmand))
application.add_handler(conv_handler)

threading.Thread(target = do_reminders).start()
 
    # Run bot
application.run_polling(1.0)

