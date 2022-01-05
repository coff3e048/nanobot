import json
import logging
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
# LOGLEVEL
# BOTSTATUS
# BOTVERSION
# DOCKER

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
    sourcepage = getenv('SOURCEPAGE', 'https://github.com/pascal48/nanobot')

    # Getting the bot's user ID
    userid = getenv('BOTID')

    # Default bot invite (could be another link)
    #botinvite = getenv('INVITE', f"https://discord.com/oauth2/{bot.userid}&scope=bot")

    # Setting bot token
    token = getenv('TOKEN')
    if token == None:
        console.error(f"No token added, Exiting...")
        exit()

    # Instance log level
    loglevel = getenv('LOGLEVEL', 'BASIC')

    # Default Discord status.
    status = getenv('BOTSTATUS', prefix)

    # Bot version
    _versionjson = json.load(
        open('bot/version.json')
    )
    version = _versionjson['botversion']

    docker = getenv('DOCKER', False)
