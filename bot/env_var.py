import json
import logging
import os
from console import console
from os import getenv 

# Valid environment variables:
#
# BOTNAME
# PREFIX
# SOURCEPAGE
# USERID
# TOKEN (required)
# LOGLEVEL (w.i.p)
# ACTIVITYTYPE ('Playing', 'Listening')
# BOTACTIVITY
# BOTVERSION


class env():

    updatemsg = getenv('UPDATEMSG', True)

    # Cosmetic name of the bot instance
    botname = getenv('BOTNAME', "nanobot")

    # Bot prefix
    prefix = getenv('PREFIX', '!!')

    # Github source page
    sourcepage = getenv('SOURCEPAGE', 'https://github.com/get-coff3e/nanobot')
    webdomain = getenv('WEBDOMAIN', 'nanobot.byteburns.us')

    userid = getenv('BOTID')

    # Default bot invite (could be another link)
    # botinvite = getenv('INVITE', "f"https://discord.com/oauth2/{bot.userid}&scope=bot)

    # Setting bot token
    token = getenv('TOKEN')
    if not token:
        console.error(f"Invalid or missing token in environment, Please input your token.\n\t\t\tYou can find your Discord bot token at https://discord.com/developer")
        token = str(input('>> '))

    # Instance log level
    # Log levels:
    # -------------------------------------------------------------------------
    # NONE      (0)      (Server and author are hidden, command is logged)
    # BASIC     (1)      (Server and command are shown)
    # MORE      (2)      (Server, author, and command + contents are shown)
    # VERBOSE   (3)      (Nextcord logging + everything that MORE has)
    lvl = ['NONE', 'BASIC', 'EXTRA', 'VERBOSE']
    loglevel = getenv('LOGLEVEL', 'EXTRA')
    loglevel = lvl.index(loglevel)

    # Default Discord status.
    statustype = getenv('ACTIVITYTYPE', 'listening')
    botstatus = getenv('STATUS', f'{prefix}')

    # Discord API Intents settings
    intents_members = getenv('INTENTS_MEMBERS', True)
    intents_guilds = getenv('INTENTS_GUILDS', True)

    # Bot version
    _versionjson = json.load(open('bot/version.json'))
    version = _versionjson['botversion']
    ver_branch = _versionjson['gitbranch']
