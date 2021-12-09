import time, os, logging

#Log the amount of time it takes to start the bot
start_time = time.time()

import discord
from nextcord.ext import commands
from colorama import Fore, Back, Style
from dotenv import load_dotenv
from os import getenv
load_dotenv()

intents = discord.Intents.default()
intents.members = True

print("Starting...")

logenv = getenv('LOGGING')
if logenv == 'True':
    print("Logfile Enabled.")
    logger = logging.getLogger('nextcord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='nextcord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
else:
    print("Logfile Disabled.")

prefix = getenv('PREFIX')

bot = commands.Bot(
    command_prefix=prefix,
        allowed_mentions=discord.AllowedMentions(
        users=False,         # Whether to ping individual user @mentions
        everyone=False,      # Whether to ping @everyone or @here mentions
        roles=False,         # Whether to ping role @mentions
        replied_user=False,  # Whether to ping on replies to messages
    ),
)

bot.load_extension("base")
bot.load_extension("fun")
bot.load_extension("snipe")
bot.load_extension("errorhandler")
bot.load_extension("youtube")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} \n(ID: {bot.user.id})')
    

    guilds = await bot.fetch_guilds(limit=150).flatten()
    print(f"{Style.DIM}Joined guilds:\n{Style.RESET_ALL}" + str(guilds) + "\n")
    print(guilds)

    end_time = time.time()
    print(f"{Style.DIM}\nTook {round((end_time - start_time) * 1000)}ms to startup{Style.RESET_ALL}")
    

# Loading TOKEN from .env
token = getenv('TOKEN')
bot.run(token)

#https://tutorial.vcokltfre.dev/
# cool thing ^
