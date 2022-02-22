import time
print("Importing modules")
start_time = time.time()    # Log the amount of time it takes to start the bot + import needed Python modules

import asyncio
from aiohttp import request
from art import text2art
from nextcord.ext import commands
from console import console
from rich import print, inspect
from env_var import env
import discord
import json
import logging
import sys
import os
import platform
import psutil
# from IMPORTANT.keep_alive import keep_alive


author = "coff3e"
name = env.botname
version = env.version
sourcepage = env.sourcepage
prefix = env.prefix
statustype = env.statustype
ver_branch = env.ver_branch


# OS info + check
console.system(f"System:\t")
inspect(platform.uname())
osplatform = platform.system()
if osplatform != "Linux":
    console.warn(
        f"{osplatform.upper()} ISN'T TESTED. USE AT YOUR OWN RISK."
    )


# Bot profile status type (playing..., watching..., listening...)
if statustype == 'playing':
    statustype = discord.ActivityType.playing
elif statustype == 'watching':
    statustype = discord.ActivityType.watching
elif statustype == 'listening':
    statustype = discord.ActivityType.listening

# Discord API Intents
intents = discord.Intents.all()
intents.members = env.intents_members
intents.guilds = env.intents_guilds
activity = discord.Activity(name=env.botstatus, type=statustype)


console.log(f"Starting nanobot ({name})")
connect_start_time = time.time()


# Bot params + info
bot = commands.Bot(
    command_prefix=prefix,
    case_insensitive=True,  # Be able to take any letter case
    intents=intents,
    help_command=None,      # Custom help command
    activity=activity,
    allowed_mentions=discord.AllowedMentions(
        users=True,         # Whether to ping individual user @mentions
        everyone=False,      # Whether to ping @everyone or @here mentions
        roles=False,         # Whether to ping role @mentions
        replied_user=True,  # Whether to ping on replies to messages
    ),
)


# Convenience function, find a safer way than using sys
def returnln(returns=1):
    for x in range(returns):
        sys.stdout.write("\033[F")  # Return back to previous line
        sys.stdout.write("\033[K")  # Flush the line


# Time-to-process calculation
def timed(_end_time, _start_time, x): return round((_end_time - _start_time) * x)


async def botupdate(URL: str = f"https://raw.githubusercontent.com/get-coff3e/nanobot/{ver_branch}/bot/version.json"):
    async with request("GET", URL, headers={}) as response:
        # if the updatemsg environment variable is unchaged or set to true, we run this.
        if env.updatemsg:
            console.log("Connecting to GitHub to check for updates...")
            if response.status == 200:
                data = await response.json(content_type=None)
                # grab .JSON data from GitHub
                newversion = data["botversion"]
                returnln()
                if newversion != version and "DEV" not in env.version:
                    console.notice(
                        f"Newest nanobot version on GitHub doesn't match the one installed. It may be outdated, please consider updating.\n\t\t\tQueried URL:\t\t{URL}\n\t\t\tCurrent Instance:\t{version}\n\t\t\tLatest Update:\t\t{newversion}\n\t\t\tBranch: {ver_branch}\n\t\t\tIf you would like to disable this functionality, set [bold orange]UPDATEMSG[/] to False in your environment")
            else:
                returnln()
                print(
                    f"Problem reaching GitHub. HTTP Response: {response.status}")


def default_cogservice(filepath):
    console.error(
        f"'{filepath}' wasn't found. Create the file with basic cogs? (Y/n)")
    i = input('>> ')
    if 'y' in i:
        basic_cogs = [
            'errorhandler',
            'botmgr',
            'help',
            'cogs.testing.admin',
            'cogs.base.basecmd',
            'cogs.base.pkgmgr'
        ]
        return basic_cogs


def cogservice(filepath: str ='config/autoload.json'):
    # These cogs are fallback cogs, in the event that no service file is present the bot will instead load these.
    console.log(f"Finding {filepath}")
    returnln()
    # filepath is defined in the function call
    if os.path.exists(filepath):
        autoload = json.load(open(filepath))
        console.success(f"Found {filepath}")
        cogsenabled = autoload['cogs']
    else:
        # Ask if the user wants to create a service file with the basic fallback cogs
        cogsenabled = default_cogservice(filepath)
    for cogs in cogsenabled:
        # Start loading cogs
        try:
            cog_start_time = time.time()
            console.log(f"loading {cogs}")
            bot.load_extension(cogs)
            cog_end_time = time.time()
            returnln()
            console.success(
                f"loaded {cogs} (took {timed(cog_end_time,cog_start_time,1000)}ms)")
        except Exception as e:
            cog_end_time = time.time()
            returnln()
            console.error(
                f"loading {cogs} failed:\n({e} (took {timed(cog_end_time,cog_start_time,1000)}ms)")


@bot.event
async def on_ready():
    connect_end_time = time.time()
    returnln()
    console.success(f'Connected to Discord API! (took {timed(connect_end_time,connect_start_time,1000)}ms)\n')
    # nanobot startup ascii art
    console.nanostyle(
        text2art(name, 'rnd-small')
    )

    print(f"\n\tVersion: {version}")
    print(f"\tBranch: {ver_branch}")
    if "DEV" in version:
        print(f"[bold red]\t! ! !   UNSTABLE DEV VERSION   ! ! ![/]")
        print(f"[bold underline red]\tNOT RECOMMENDED FOR PRODUCTION USE[/]")
        print(f"[red]\tReport any bugs to: {sourcepage}[/]")

# Discord API User info + prefix
    print("\n\t----------------------------------------")
    print(f'\t[magenta]Logged in as [/][underline]{bot.user}[/] ({bot.user.id})')
    print(f"\t[magenta]Generic Invite[/]: https://discord.com/oauth2/{bot.user.id}&scope=bot")
    print(f'\t[magenta]Prefix[/]: {prefix}')
    print("\t----------------------------------------\n")

# printing list of guilds the bot is joined into
    console.botlog("Joined guilds:")
    servers = bot.guilds
    count = []
    if len(servers):
        for guilds in servers:
            try:
                count.append(guilds)
                print(f'\t\t\t{len(count)} -\t{guilds}\t\t(ID: {guilds.id})')
            except Exception as e:
                console.error(e)
        console.botlog(f'Total joined guilds: {len(servers)}')
    else:
        console.botlog(f"Not joined into any guilds. Invite the bot using: https://discord.com/oauth2/{bot.user.id}&scope=bot")

    if intents.members:
        users = bot.users
# Uncomment these lines below to print out all users the bot sees. Otherwise, it will only show you how many there are.
        # console.botlog(f"Found users:")
        # count = []
        # for member in users:
        #    try:
        #        count.append(member)
        #        print(f'\t\t\t\t{len(count)} -\t{member}')
        #   except Exception as e:
        #       console.error(e)
        console.botlog(f"Total unique users: {len(users)}")

# load cogs from cogservice function
    cogservice()

# print the time it took to start the bot
    end_time = time.time()
    console.log(f"Took {timed(end_time,start_time,1000)}ms ({timed(end_time,start_time,1)}s) to start-up")

    await botupdate()


if __name__ == "__main__":
    # Loading TOKEN from .env
    console.botlog("Attempting to connect to Discord API")
    try:
        bot.run(env.token)
    except Exception as e:
        returnln()
        console.error(e)
