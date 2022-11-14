from telethon import TelegramClient, events

client = TelegramClient('session_name', "12345", "123456789")

@client.on(events.NewMessage)
async def my_event_handler(event):
    user_id = event.message.from_id.user_id
    
    # the \u200b is a unicode which is not visible on Telegram clients and makes the invisible tagging possible
    await client.send_message("group_name", f"Hidden tagging {user_id}[\u200b](tg://user?id={user_id})")

client.start()
client.run_until_disconnected()