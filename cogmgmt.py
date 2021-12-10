import time, psutil, os, json
import discord
from nextcord.ext import commands
from dotenv import load_dotenv

from os import getenv
load_dotenv()

class cogService:
      cogsenabled = [ 
      "base",
      "errorhandler",
      "extended",
      "fun",
#     "cogs.snipe",
#     "cogs.youtube" 
      ]


class cogManagement(commands.Cog):
    """Search YouTube for videos."""

    def __init__(self, bot):
      self.bot = bot


def setup(bot: commands.Bot):
    bot.add_cog(cogManagement(bot))