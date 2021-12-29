# nanobot
nanobot is a small experimental discord bot aimed at simplicity and modularity.

right now, nanobot has only been tested on Linux distributions. 
compatability with other operating systems are likely, but not guaraunteed 

# Running & Dependencies
## Running
Running the bot is as simple as python main.py, but requires secret environment variables.

Heres an example:

```
TOKEN='bunchoflettersandwhatnot'
PREFIX='!!'
# Bot invite
INVITE='https://discord.com/oauth2/***'
# Source code page
SOURCEPAGE='https://github.com/pascal48/nanobot'
```
Note that only TOKEN is really required, while the rest have built-in defaults.

### Dependencies
`python3 -m pip install -r requirements.txt`

requirements.txt contains a list of dependencies that are required to run nanobot, just run this and you'll be ok :)

Goals

- Create moderation commands (ban, mute, etc.)
- Create guild-specific data (custom prefix, RSS, etc)
- More "fun" commands
- Slash commands?
