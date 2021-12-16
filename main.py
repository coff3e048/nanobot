import time
# Log the amount of time it takes to start the bot
start_time = time.time()
import discord, logging, os, asyncio
from art import text2art
from nextcord.ext import commands
from console import console, print
from dotenv import load_dotenv
from os import getenv

console.log(f"os.name tells us that this system is {os.name}")


class env():
    load_dotenv()
    # Environment Variable checking
    nextcordlogenv = getenv('NEXTCORDLOGGING')
    if nextcordlogenv == 'True':
        console.botinfo(f"Nextcord Logfile Enabled")
        # I'm worried this logfile could get really big, so I would probably not use this yet.
        logger = logging.getLogger('nextcord')
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(filename='nextcord.log', encoding='utf-8', mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)
    else:
        console.log(f"Nextcord API Logfile Disabled")

    # Cosmetic name of the bot instance
    botname = getenv('NAME')
    if botname == None:
        botname = "nanobot"
        console.warn(f"No name set, Defaulting to '{botname}'")

    # Bot prefix
    prefix = getenv('PREFIX')
    if prefix == None:
        prefix = "!!"
        console.warn(f"No prefix set, Defaulting to '{prefix}'")

    # Github source page
    sourcepage = getenv('SOURCEPAGE')
    if sourcepage == None:
        sourcepage = "https://github.com/pascal48/nanobot"
        console.warn(f"No sourcepage set, Defaulting to '{sourcepage}'")

    # Bot token ( https://discord.com/developers/docs )
    token = getenv('TOKEN')
    if token == None:
        console.err(f"No token added, Exiting...")
        exit()

# There are 4 levels of logging. 
# ANONYMOUS, MINIMAL, BASIC, FULL, and FULL-FILE
# ----------------------------
# ANONYMOUS: No message type (server, dm), no user, and no command
# MINIMAL  : Logging server (excluding DM), but no user and only command
# BASIC    : Logs server / DM, user, and commands but no strings and no files
# FULL     : Logs all message types, users, commands + strings used, but not into a file.
#   - FILE : Logs whatever full has but into a file
# (FULL isnt a thing yet)

    loglevel = getenv('LOGLEVEL')
    if loglevel == None:
      loglevel = 'BASIC'
      console.warn(f"Logging level not set, defaulting to '{loglevel}'")
      

    status = getenv('BOTSTATUS')
    if status == None:
        status = prefix
        console.warn(f"No custom status set. Defaulting to the prefix: {prefix}")



intents = discord.Intents.default()
intents.members = True

console.botinfo(f"Starting {env.botname}")


bot = commands.Bot(
    command_prefix=env.prefix,
    case_insensitive=True,
    allowed_mentions=discord.AllowedMentions(
        users=False,         # Whether to ping individual user @mentions
        everyone=False,      # Whether to ping @everyone or @here mentions
        roles=False,         # Whether to ping role @mentions
        replied_user=False,  # Whether to ping on replies to messages
    ),
)



class botinfo():
  
    author = "coff3e"
    name = env.botname
    version = "DEV-12152021"



def cogservice():
    if os.path.exists("service.txt"):
        console.botinfo("Found service.txt")
        fs = "service.txt"
        service = open(fs, 'r')
        cog_file = service.read()
        cogsenabled = cog_file.split()
        service.close()
        for cogs in cogsenabled:
            try:
                cog_start_time = time.time()
                bot.load_extension(cogs)
                cog_end_time = time.time()
                if "testing" in cogs:
                  console.warn(f"WARNING! TESTING COG {cog} LOADING")
                console.botinfo(f"loading {cogs.replace('.','/')} ({round((cog_end_time - cog_start_time) * 1000)}ms)")
            except Exception as e:
                console.error(f"loading {cogs.replace('.','/')} failed ({e})")
    else:
      console.error(f"service.txt doesn't exist. Exiting.")
      exit()

    
@bot.event
async def on_ready():
# nanobot startup ascii art
    console.nanostyle(f"\n{text2art(botinfo.name,'random')}")
    if "DEV" in botinfo.version:
        print(f"[white]\n{botinfo.version}[/]")
        print(f"[bold red]!!!DEV VERSION!!!\n!!!UNSTABLE, EXPECT MANY BUGS!!![/]")
        print(f"[red]Report bugs to: https://github.com/pascal48/nanobot[/]")
    else:
        print(f"[white]\n{botinfo.version}[/]")

# did the bot login to the discord API? 
    print("\n----------------------------------------")
    print(f'[magenta]Logged in as [/]{bot.user} ({bot.user.id})')
    print(f'[dim magenta]Prefix: {env.prefix}[/]')
    print("----------------------------------------\n")

# printing list of joined guilds and its data
    console.botinfo(f"Joined guilds:")
    for guilds in bot.guilds:
        try:
            console.print(f'{[guilds]}')
        except Exception:
            console.error('Couldnt print guilds.')

    cogservice()

# printing the time it took to start the bot
    end_time = time.time()
    console.log(f"Took {round((end_time - start_time) * 1000)}ms to start-up")

# set the bot status and then screw off
    try:
        await bot.change_presence(activity=discord.Game(name=env.status))
        console.botinfo(f"Set bot status as '[white]{env.status}[/]'")
    except Exception as e:
        console.error(f"Setting bot status failed.\n{e}")

# Loading TOKEN from .env
bot.run(env.token)