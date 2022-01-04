import json
from console import console, print
from os import getenv

class loaded():
    cogs = []

class unloaded():
    cogs = []

class env():
    # Cosmetic name of the bot instance
    botname = getenv('BOTNAME', "nanobot")

    # Bot prefix
    prefix = getenv('PREFIX', '!!')

    # Github source page
    sourcepage = getenv('SOURCEPAGE', 'https://github.com/pascal48/nanobot')

    # Getting the bot's user ID
    userid = getenv('BOTID')

    # Default bot invite (could be another link)
    botinvite = getenv('INVITE', f"https://discord.com/oauth2/{userid}&scope=bot")

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
