import asyncio
import os
import logging
from env_var import env
from console import console, print
from nextcord.ext import commands
import discord
from art import text2art
import time
# Log the amount of time it takes to start the bot
start_time = time.time()
basic_cogs = ["basecmd","botmgr","pkgmgr","errorhandler"]

console.log(f"os.name tells us that this system is {os.name}")
if os.name != "posix":
    console.warn(f"{os.name} ISNT TESTED. USE AT YOUR OWN RISK.")

intents = discord.Intents.default()
intents.members = True

console.botlog(f"Starting {env.botname}")

# Bot params + info
bot = commands.Bot(
    command_prefix=env.prefix,
    case_insensitive=True,
    allowed_mentions=discord.AllowedMentions(
        users=True,         # Whether to ping individual user @mentions
        everyone=False,      # Whether to ping @everyone or @here mentions
        roles=False,         # Whether to ping role @mentions
        replied_user=True,  # Whether to ping on replies to messages
    ),
)


class botinfo():

    author = "coff3e"
    name = env.botname
    version = "DEV-12/28/2021"


def cogservice():
    if os.path.exists("config/service.txt"):
        console.botlog("Found service.txt")
        service = open('service.txt', 'r')
        cog_file = service.read()
        cogsenabled = cog_file.split()
        service.close()
        for cogs in cogsenabled:
            try:
                cog_start_time = time.time()
                bot.load_extension(cogs)
                cog_end_time = time.time()
                if "testing" in cogs:
                    console.warn(f"TESTING COG {cogs} LOADING")
                console.botlog(
                    f"loading {cogs.replace('.','/')} ({round((cog_end_time - cog_start_time) * 1000)}ms)")
            except Exception as e:
                console.error(f"loading {cogs.replace('.','/')} failed ({e})")
    else:
        console.error(f"service.txt was't found. Loading basic cogs.")
        for cogs in basic_cogs:
            try:
                cog_start_time = time.time()
                bot.load_extension(cogs)
                cog_end_time = time.time()
                console.botlog(
                    f"loading {cogs.replace('.','/')} ({round((cog_end_time - cog_start_time) * 1000)}ms)")
            except Exception as e:
                console.error(f"loading {cogs.replace('.','/')} failed ({e})")

@bot.event
async def on_ready():
# nanobot startup ascii art
    console.nanostyle(f"\n{text2art(botinfo.name,'random')}")
    if "DEV" in botinfo.version:
        print(f"[red]\n{botinfo.version}[/]")
        print(f"[bold red]!!!DEV VERSION!!![/]\n")
        print(f"[red]Report bugs to: https://github.com/pascal48/nanobot[/]")
    else:
        print(f"[white]\n{botinfo.version}[/]")

# Discord API info
    print("\n----------------------------------------")
    print(f'[magenta]Logged in as [/]{bot.user} ({bot.user.id})')
    print(f'[dim magenta]Prefix: {env.prefix}[/]')
    print("----------------------------------------\n")

# printing list of joined guilds and its data
    console.botlog(f"Joined guilds:")
    for guilds in bot.guilds:
        try:
            console.print(f'{[guilds]}')
        except Exception:
            console.error("Couldn't print guilds.")
# load cogs
    cogservice()

# printing the time it took to start the bot
    end_time = time.time()
    console.log(f"Took {round((end_time - start_time) * 1000)}ms to start-up")

# set the bot status and then screw off
    try:
        await bot.change_presence(activity=discord.Game(name=env.status))
        console.botlog(f"Set bot status as '[white]{env.status}[/]'")
    except Exception as e:
        console.error(f"Setting bot status failed.\n{e}")


# Loading TOKEN from .env
try: 
    bot.run(env.token)
except Exception as e:
    console.error(e)
