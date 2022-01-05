import time
# Log the amount of time it takes to start the bot
start_time = time.time()
import asyncio, aiohttp
import psutil
import platform
import os
import sys
import logging
import json
import discord
from rich import print
from console import console
from nextcord.ext import commands
from env_var import env
from art import text2art


osinfo = platform.system()
console.system(f"System: {platform.uname()}")
if osinfo != "Linux":
    console.warn(f"{osinfo} ISN'T TESTED. USE AT YOUR OWN RISK.")


intents = discord.Intents.default()
intents.members = True

console.botlog(
    f"Starting {env.botname}"
)

# Bot params + info
bot = commands.Bot(
    command_prefix=env.prefix,
    case_insensitive=True,
    help_command=None,
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
    version = env.version
    sourcepage = env.sourcepage


def cogservice(filepath):
    if os.path.exists(filepath):
        console.log(f"Found {filepath}")
        service = open(filepath, 'r')
        cogsenabled = service.read().split()
        service.close()
        for cogs in cogsenabled:
            try:
                cog_start_time = time.time()
                console.log(f"loading {cogs}")

                bot.load_extension(cogs)
                cog_end_time = time.time()
                console.botlog(f"loaded {cogs} ({round((cog_end_time - cog_start_time) * 1000)}ms)")
            except Exception as e:
                console.error(f"loading {cogs} failed:\n({e})")
    else:
        console.error(f"{filepath} was't found. Loading basic cogs.")
        for cogs in basic_cogs:
            try:
                cog_start_time = time.time()
                bot.load_extension(cogs)
                cog_end_time = time.time()
                console.botlog(f"loading {cogs.replace('.','/')} ({round((cog_end_time - cog_start_time) * 1000)}ms)")
            except Exception as e:
                console.error(f"loading {cogs.replace('.','/')} failed ({e})")

@bot.event
async def on_ready():
# nanobot startup ascii art
    console.nanostyle(
      text2art(botinfo.name,'random')
      )
    if "DEV" in botinfo.version:
        print(f"[red]\n{botinfo.version}[/]")
        print(f"[bold red]! ! !   DEV VERSION   ! ! ![/]\n")
        print(f"[red]Report bugs to: {botinfo.sourcepage}[/]")
    else:
        print(f"[white]\n{botinfo.version}[/]")

# Discord API info
    print("\n----------------------------------------")
    print(f'[magenta]Logged in as [/][underline]{bot.user}[/] ({bot.user.id})')
    print(f'[magenta]Prefix: {env.prefix}[/]')
    print("----------------------------------------\n")

# printing list of joined guilds and its data
    #console.botlog(f"Joined guilds:")
    for guilds in bot.guilds:
        try:
            #console.print(f'{[guilds]}')
            pass
        except Exception as e:
            console.error(e)
# load cogs
    cogservice('config/service.txt')

# printing the time it took to start the bot
    end_time = time.time()
    console.log(
        f"Took {round((end_time - start_time) * 1000)}ms to start-up"
    )

# set the bot status and then screw off
    try:
        await bot.change_presence(
                                  activity=discord.Game(
                                  name=env.status)
                                )
        console.botlog(f"Set bot status as '[white]{env.status}[/]'")
    except Exception as e:
        console.error(f"Setting bot status failed.\n{e}")


# Loading TOKEN from .env
try: 
    bot.run(env.token)
except Exception as e:
    console.error(e)
    exit()
