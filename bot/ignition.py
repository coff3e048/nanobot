import time
# Log the amount of time it takes to start the bot
start_time = time.time()
import aiohttp
import asyncio
from art import text2art
from env_var import env
from nextcord.ext import commands
from console import console
from rich import print
import discord
import json
import logging
import sys
import os
import platform
import psutil


console.system(f"System: {platform.uname()}")
osplatform = platform.system()
if osplatform != "Linux":
    console.warn(f"{osplatform} ISN'T TESTED. USE AT YOUR OWN RISK.")


intents = discord.Intents.default()
intents.members = True

console.log(
    f"Starting nanobot ({env.botname})"
)

# Bot params + info
bot = commands.Bot(
    command_prefix=env.prefix,
    case_insensitive=True,
    intents=intents,
    # help_command=None,
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
                console.success(
                    f"loaded {cogs} ({round((cog_end_time - cog_start_time) * 1000)}ms)")
            except Exception as e:
                console.error(f"loading {cogs} failed:\n({e})")
    else:
        console.error(f"{filepath} was't found. Loading basic cogs.")
        for cogs in basic_cogs:
            try:
                cog_start_time = time.time()
                bot.load_extension(cogs)
                cog_end_time = time.time()
                console.success(
                    f"loading {cogs.replace('.','/')} ({round((cog_end_time - cog_start_time) * 1000)}ms)")
            except Exception as e:
                console.error(f"loading {cogs.replace('.','/')} failed ({e})")



@bot.event
async def on_ready():
    console.success('Connection made!\n')
    # nanobot startup ascii art
    console.nanostyle(
        text2art(botinfo.name, 'random')
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
    console.botlog("Joined guilds:")
    num = 0
    joinedguilds = bot.guilds
    if len(joinedguilds) > 1:
        for guilds in joinedguilds:
            try:
                num = num + 1
                print(f'{num} - {guilds}')
            except Exception as e:
                console.error(e)
        console.botlog(f'Total joined guilds: {len(joinedguilds)}')
    else:
        console.botlog(f"Not joined into any guilds. Invite the bot using ...")
        

    if intents.members:
        users = bot.users
        #try:
        #    print(users)
        #except Exception as e:
        #    console.error(e)
        console.botlog(f"Total unique users found: {len(users)}")

# load cogs from cogservice function
    cogservice('config/service.txt')

# printing the time it took to start the bot
    end_time = time.time()
    console.log(
        f"Took {round((end_time - start_time) * 1000)}ms to start-up"
    )

# set the bot status and then run as normal
    try:
        await bot.change_presence(
            activity=discord.Game(
                name=env.status
                )
            )
        console.success(f"Set bot status as '[white]{env.status}[/]'")
    except Exception as e:
        console.error(f"Setting bot status failed.\n{e}")


# Loading TOKEN from .env
try:
    console.botlog("Attempting to connect to Discord API...")
    bot.run(env.token)
except Exception as e:
    console.error(e)
    exit()
