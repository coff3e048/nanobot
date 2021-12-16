import time, psutil, os
import discord
from nextcord.ext import commands


class botManagement(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group()
    @commands.is_owner()
    async def botmgr(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.reply("No invoked subcommand")

    @botmgr.group()
    async def dump(sef, ctx, file: str = None):
      

def setup(bot: commands.Bot):
    bot.add_cog(botManagement(bot))
