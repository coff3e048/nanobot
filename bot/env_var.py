import json
import logging
import os
from console import console
from os import getenv

# Valid environment variables:
# 
# NEXTCORDLOG
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
    # Cosmetic name of the bot instance
    nextcordlog = getenv('NEXTCORDLOG', False)
    if nextcordlog:
        logger = logging.getLogger('nextcord')
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(filename='log/nextcord.log', encoding='utf-8', mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)

    botname = getenv('BOTNAME', "nanobot")

    # Bot prefix
    prefix = getenv('PREFIX', '!!')

    # Github source page
    sourcepage = getenv('SOURCEPAGE', 'https://github.com/get-coff3e/nanobot')
    webdomain = getenv('WEBDOMAIN', 'nanobot.byteburns.us')

    userid = getenv('BOTID')

    # Default bot invite (could be another link)
    #botinvite = getenv('INVITE', f"https://discord.com/oauth2/{bot.userid}&scope=bot")

    # Setting bot token
    token = getenv('TOKEN')
    if token == None:
        console.error(f"Invalid or missing token in environment, Please input your token.\n\t\t\tYou can find your Discord bot token at https://discord.com/developer")
        token = str(input('>> '))
    # Instance log level
    # Log levels:
    # 
    # NONE
    # BASIC
    # MORE
    # VERBOSE
    loglevel = getenv('LOGLEVEL', 'NONE')


    # Default Discord status.
    activitytype = getenv('ACTIVITYTYPE', 'listening')
    botactivity = getenv('STATUS', f'{prefix}')

    # Bot version
    _versionjson = json.load(open('bot/version.json'))
    version = _versionjson['botversion']
