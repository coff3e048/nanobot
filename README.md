# nanobot

nanobot is a small but (soon to be) feature rich general purpose Discord bot written in Python. This bot is not considered usable or stable at the moment, so contributions are welcome 

## Running
Running the bot is as simple as `python main.py`

Running this bot requires an `.env` file
Heres an example:
```
TOKEN='bunchoflettersandwhatnot
PREFIX='!!'
# Bot invite
INVITE='https://discord.com/oauth2/***
# Source code page
SOURCEPAGE='https://github.com/pascal48/nanobot'
```
The bot will not run without these, in the future 'INVITE' and 'SOURCEPAGE' will be optional.

## Dependencies

`python3 -m pip install -U nextcord psutil python-dotenv colorama`

are dependencies that are required to run nanobot in its current state.

# Goals

- Create moderation commands (ban, mute, etc.)
- Create guild-specific data (custom prefix, RSS, etc)
- More "fun" commands
- Slash commands?
- Sort cogs into folders 
