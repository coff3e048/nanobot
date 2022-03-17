# NOTE: Project is currently dormant. Don't expect any often changes

# nanobot
nanobot is a Discord bot utilizing the [nextcord](https://github.com/nextcord/nextcord) python API.

nanobot's focus is on user customizability, modularity, and more importantly: keeping it nano (small)


#### Disclaimer:
nanobot is a personal project to practice Python and learn more about it in the process. I do not consider this a stable bot, but contributions and suggestions are very welcome. 


# Running & Dependencies
## Running
Running the bot requires only Python 3 and ffmpeg (for youtube-dl command)
```
python3 bot/main.py
```

The only required environment variable is the API Token as `TOKEN`. the rest have defaults and do not necessarily need to be set but you may check `.env.example` 

Compatability outside of Linux is being built up, but it's not garaunteed.


## Dependencies
For manually installing dependencies, run 
```
pip install -r requirements.txt
```
in the directory where nanobot is located

You may need to install gcc and g++ for installing nextcord.


## nanobot is in a very early stage, so these dependencies will change very often.


