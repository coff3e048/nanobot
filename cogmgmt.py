import time, psutil, os, json
import discord
from nextcord.ext import commands
from dotenv import load_dotenv

from os import getenv
load_dotenv()

class cogService:
      cogsenabled = [ 
      "cogmgmt",
      "base",
      "errorhandler",
      "extended",
      "fun",
      "cogs.youtube"
      ]

class cogManagement(commands.Cog):

    def __init__(self, bot: commands.Bot):
      self.bot = bot


    @commands.group()
    async def cog(self, ctx: commands.Bot):
      if ctx.invoked_subcommand is None:
        await ctx.reply('Invalid query. Try again')

    @cog.command(pass_context=True)
    async def load(self, ctx: commands.Bot, cog: str):
      await bot.load_extension(cog)
      cogsenabled.append(cog)
        
    @cog.command(pass_context=True)
    async def unload(self, ctx: commands.Bot, cog: str):
      await bot.unload_extension(cog)
      cogsenabled.remove(cog)

    @cog.command(pass_context=True)
    async def reload(self, ctx: commands.Bot, cog: str):
      await bot.reload_extension(cog)
        
    @cog.command(pass_context=True)
    async def list (self, ctx):
      await ctx.reply(f"Enabled cogs: {cogsenabled}")


def setup(bot: commands.Bot):
  bot.add_cog(cogManagement(bot))