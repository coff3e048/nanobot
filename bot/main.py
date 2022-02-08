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
    console.warn(f"{osplatform.capitalize()} ISN'T TESTED. USE AT YOUR OWN RISK.")

if env.activitytype == 'playing':
    activitytype = discord.ActivityType.playing
elif env.activitytype == 'watching':
    activitytype = discord.ActivityType.watching
elif env.activitytype == 'listening':
    activitytype = discord.ActivityType.listening


intents = discord.Intents.default()
intents.members = True
intents.guilds = True
activity = discord.Activity(name=env.botactivity, type=activitytype)

console.log(
    f"Starting nanobot ({env.botname})"
)


# Bot params + info
bot = commands.Bot(
    command_prefix=env.prefix,
    case_insensitive=True,
    intents=intents,
    help_command=None,
    activity=activity,
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
        with open(filepath, 'r') as service:
            cogsenabled = service.read().split()
    else:
        console.error(f"{filepath} was't found. Loading basic cogs.")
        cogsenabled = basic_cogs
    service.close()
    for cogs in cogsenabled:
        try:
            cog_start_time = time.time()
            console.log(f"loading cog {cogs}")
            bot.load_extension(cogs)
            cog_end_time = time.time()
            console.success(
                f"loaded {cogs} ({round((cog_end_time - cog_start_time) * 1000)}ms)")
        except Exception as e:
            console.error(f"loading cog {cogs} failed:\n({e})")

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

# Discord API User info + prefix
    print("\n----------------------------------------")
    print()
    print(f'[magenta]Logged in as [/][underline]{bot.user}[/] ({bot.user.id})')
    print(f'[magenta]Prefix: {env.prefix}[/]')
    print()
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
# Uncomment these lines below to print out all users the bot sees. Otherwise, it will only show you how many there are.
        #console.botlog(f"Found users:")
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
        f"Took {round((end_time - start_time) * 1000)}ms ({round((end_time - start_time) * 1)}s) to start-up"
    )

if __name__ == "__main__":
    # Loading TOKEN from .env
    console.botlog("Attempting to connect to Discord API...")
    try:
        bot.run(env.token)
    except Exception as e:
        console.error(e)
        exit()
