import time, psutil, os, json
import discord
from nextcord.ext import commands
from dotenv import load_dotenv

from os import getenv
load_dotenv()

  #https://www.geeksforgeeks.org/os-module-python-examples/
  #https://www.w3schools.com/python/python_file_open.asp

class cogManagement(commands.Cog):

    def __init__(self, bot: commands.Bot):
      self.bot = bot

    @commands.group()
    async def cog(self, ctx):
      if ctx.invoked_subcommand is None:
        await ctx.reply('Invalid cog command passed')

    @cog.command()
    async def list(self, ctx):
      fs = "service.txt"
      service = open(fs, 'r')
      text = service.read()
      await ctx.reply(f"```{text}```")
      service.close()

    @cog.command()
    async def load(self, ctx, *, text: str):
      split_text = text.split()
      msg = await ctx.reply(f"Attempting to load cog(s): {split_text}")
      try:
        for cogs in split_text:
          self.bot.load_extension(cogs)
        await msg.edit(f"{split_text} loaded.")
      except Exception as e:
        await msg.edit(f"Cog loading failed.\n```{e}```")

    @cog.command()
    async def unload(self, ctx, *, text: str):
      split_text = text.split()
      msg = await ctx.reply(f"Attempting to unload cog(s): {split_text}")
      try:
        for cogs in split_text:
          self.bot.unload_extension(cogs)
        await msg.edit(f"{split_text} unloaded.")
      except Exception as e:
        await msg.edit(f"Cog unloading failed.\n```{e}```")
      
    @cog.command()
    async def reload(self, ctx, *, text: str):
      split_text = text.split()
      msg = await ctx.reply(f"Attempting to reload cog(s): {split_text}")
      try:
        for cogs in split_text:
          self.bot.reload_extension(cogs)
        await msg.edit(f"{split_text} reloaded.")
      except Exception as e:
        await msg.edit(f"Cog unloading failed.\n```{e}```")

def setup(bot: commands.Bot):
    bot.add_cog(cogManagement(bot))