import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import subprocess
import asyncio
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime, timedelta

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') # set these in the env file
GUILD = os.getenv('DISCORD_GUILD')
BOT_SCRIPT_LOCATION = '/home/username/Documents/AI/diffusion/ComfyUI/YOUPUTBOTHERE.py'
folder_path = '/home/username/Documents/AI/diffusion/ComfyUI/output/'
allowed_channel_id = 0000000000000000000
exempt_users = [0000000000000000000, 0000000000000000000]

intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.guild_messages = True
intents.guilds = True

client = commands.Bot(command_prefix='!', intents=intents)

latest_images = []

class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            latest_images.append(event.src_path)

event_handler = ImageHandler()
observer = Observer()
observer.schedule(event_handler, path=folder_path, recursive=False)
observer.start()

user_last_message_time = {}
COOLDOWN_DURATION = 180  # 3 minutes

@commands.cooldown(1, COOLDOWN_DURATION, commands.BucketType.user)
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
    channel_id = 0000000000000000000  
    channel = client.get_channel(channel_id)
    
    if channel:
        await channel.send("Bot is now online!")

@commands.cooldown(1, COOLDOWN_DURATION, commands.BucketType.user)
@client.event
async def on_message(message):
    global observer
    
    if message.author == client.user:
        return

    # Check if the message was sent in the allowed channel
    if message.channel.id != allowed_channel_id:
        return

    print(f"Last message sender ID: {message.author.id}")
    
    if message.author.id in exempt_users:
        pass
    else:
        if message.author.id in user_last_message_time:
            last_message_time = user_last_message_time[message.author.id]
            time_remaining = timedelta(seconds=COOLDOWN_DURATION) - (datetime.now() - last_message_time)
            
            if time_remaining > timedelta(0):
                await message.channel.send(f"You are still in timeout. Time remaining: {time_remaining}")
                return

    if message.content.startswith('!gen_image'):
        _, _, args = message.content.partition(' ')
 
        user_last_message_time[message.author.id] = datetime.now()

        script_path = '/home/username/Documents/AI/diffusion/ComfyUI/bot_api.py'
        command = f'python {script_path} "a safe-for-work image, pg-13, {args}"'
        
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        await message.channel.send(f"{result.stdout}")
        
        while len(latest_images) < 4:
            await asyncio.sleep(1)
            
        selected_images = latest_images[:4]

        # Move images to a folder with timestamp and the last user's name
        timestamp = datetime.now().strftime('%Y-%m-%d-%H%M%S')
        user_folder = f'{timestamp}-{message.author.name}'
        destination_folder = os.path.join(folder_path, user_folder)
        os.makedirs(destination_folder, exist_ok=True)

        image_files = []
        for image in selected_images:
            image_name = os.path.basename(image)
            destination_path = os.path.join(destination_folder, image_name)
            os.rename(image, destination_path)
            image_files.append(discord.File(destination_path))

        await message.channel.send(files=image_files)
        
        observer.stop()
        observer.join()

client.run(TOKEN)
