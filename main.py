import time, os, logging, json
from cogmgmt import cogService

#Log the amount of time it takes to start the bot
start_time = time.time()

import discord
from nextcord.ext import commands
from colorama import Fore, Back, Style # Foreground colors are like Fore.COLOR
from dotenv import load_dotenv
from os import getenv
load_dotenv()

intents = discord.Intents.default()
intents.members = True

print("Starting...")

logenv = getenv('LOGGING')
if logenv == 'True':
    print("Logfile Enabled.")
    # I'm worried this logfile could get really big, so I would probably not use this yet.
    logger = logging.getLogger('nextcord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='nextcord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
else:
    # If LOGGING is anything other than True, disable it.
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

_author_ = "coff3e"
_version_ = "DEV-mmddyyyy"

def cogservice():
  try: 
    for cogs in cogService.cogsenabled:
      print(f"{Fore.YELLOW}loading {cogs}")
      bot.load_extension(cogs)
  except Exception as e:
    print(f"{Fore.RED}Could not load enabled cogs")
    print(" - {}".format(e))
    # Kill the process to avoid constant reloads
    exit()
    

@bot.event
async def on_ready():
    cogservice()

    print(
      f'\n{Fore.GREEN}Logged in as {bot.user} \n{Style.DIM}User ID: {bot.user.id}{Style.RESET_ALL}'
      )
    
    guildfetch = await bot.fetch_guilds(limit=150).flatten()
    
    guildlist = (
      f"\n{Style.DIM}Joined guilds:\n{Style.RESET_ALL}" + str(guildfetch)
      )
    print(guildlist)

    end_time = time.time()
    print(
      f"{Style.DIM}\nTook {round((end_time - start_time) * 1000)}ms to startup{Style.RESET_ALL}"
      )
    
    await bot.change_presence(activity=discord.Game(name="シ"))
    

# Loading TOKEN from .env
token = getenv('TOKEN')
bot.run(token)

#https://tutorial.vcokltfre.dev/
# cool thing ^
