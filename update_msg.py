import sqlite3
import asyncio
from aiogram import Bot
from telegram.ext import *

with open('bot_token.txt', 'r') as file:
        bot_token = file.read()
print(bot_token)
# Connect to the SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Execute the SELECT query to fetch all IDs from the user table
cursor.execute("SELECT * FROM user")
print("execution sucessfully done")
all_ids = cursor.fetchall()

# Print all IDs
for row in all_ids:
    rowid = row[0]
    
    async def send_telegram_message(bot_token, user_id, message):
                bot = Bot(token=bot_token)
                await bot.send_message(chat_id=user_id, text=message)
                

    async def main():
        
        target_user_id = rowid
        message = "📢 Update:🔥 \nWe have made some improvements to our system. \nWrong Enter date problem fixed, \nPlease check out the latest features!"
        
        await send_telegram_message(bot_token, target_user_id, message)

    asyncio.run(main())

# Close the database connection
conn.close()
