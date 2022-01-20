import aiohttp
import cowsay
import re
import discord
import base64
from nextcord.ext import commands


class Encode(commands.Cog):
    """Search YouTube for videos."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="encode")
    

def setup(bot: commands.Bot):
    bot.add_cog(Encode(bot))
