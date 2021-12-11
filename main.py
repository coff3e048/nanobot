import time, logging, datetime
from cogmgmt import cogService
from art import text2art

#Log the amount of time it takes to start the bot
start_time = time.time()

import discord
from nextcord.ext import commands
from colorama import Fore, Style # Foreground colors are like Fore.COLOR, Background is Back.COLOR
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

    #https://stackoverflow.com/questions/63324508/print-the-time-a-command-was-used-into-terminal-discord-py-rewrite


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
_version_ = "DEV-12102021"

cogsenabled = cogService.cogsenabled
def cogservice():
  try: 
    for cogs in cogsenabled:
      print(f"{Fore.YELLOW}loading {cogs}{Style.RESET_ALL}")
      bot.load_extension(cogs)
  except Exception as e:
    print(f"{Fore.RED}Could not load enabled cogs")
    print(" - {}".format(e))
    # Kill the process to avoid constant reloads
    exit()
    
@bot.event
async def on_ready():
    textart = text2art("nanobot")
    print(f"{Fore.MAGENTA}{textart}{Style.RESET_ALL}")
    print(f"VERSION: {_version_}")

    print(f'\n{Fore.GREEN}Logged in as {bot.user} \n{Style.DIM}User ID: {bot.user.id}{Style.RESET_ALL}')
    cogservice()

    guilddata = bot.guilds
    print(f"\n{Style.DIM}Joined guilds:{Style.RESET_ALL}")
    for guilds in guilddata:
      try:
        print([guilds])
      except:
        print(guilddata)

    end_time = time.time()
    print(f"{Style.DIM}\nTook {round((end_time - start_time) * 1000)}ms to startup{Style.RESET_ALL}\n")
    
    await bot.change_presence(activity=discord.Game(name="シ"))
    
@commands.Cog.listener()
async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
  x = datetime.datetime.now()
  xtime = x.strftime("%X")
  server = ctx.guild.name
  user = ctx.author
  command = ctx.command
  print(f'{xtime}{Fore.RED} | ERRO: ({server}) {user} used {command} and failed with {error}{Style.RESET_ALL}')

@commands.Cog.listener()
async def on_command(ctx):
  x = datetime.datetime.now()
  xtime = x.strftime("%X")
  server = ctx.guild.name
  user = ctx.author
  command = ctx.command
  print(f'{xtime}{Style.DIM} | INFO: ({server}) {user} used {command}{Style.RESET_ALL}')


# Loading TOKEN from .env
token = getenv('TOKEN')
bot.run(token)

#https://tutorial.vcokltfre.dev/
# cool thing ^
