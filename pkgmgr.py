import time, psutil, os
import discord
from nextcord.ext import commands
from console import console
from dotenv import load_dotenv

from os import getenv
load_dotenv()


class cogManagement(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group()
    @commands.is_owner()
    async def cog(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.reply("not a subcommand, bozo")

    @cog.command()
    async def dump(self, ctx, *, cog: str):
        try:
            await ctx.reply(file=discord.File(cog))
        except Exception as e:
            await ctx.reply(f"{e}")
    
    @cog.command()
    async def list(self, ctx):
        try:  
            fs = "service.txt"
            list = open(fs, 'r')
            await ctx.reply(f"```{list.read()}```")
            list.close()
        except Exception as e:
            await ctx.reply(f"{e}")


    @cog.command()
    async def load(self, ctx, *, text: str):
        split_text = text.split()
        msg = await ctx.reply(f"Attempting to load cog(s): ```{split_text}```")
        try:
            for cogs in split_text:
              self.bot.load_extension(cogs)
              console.botinfo(f"loading {cogs}")
              await msg.edit(f"```{split_text}``` loaded.")
        except Exception as e:
            await msg.edit(f"Cog loading failed.\n```{e}```")
            console.error(f"Failed loading {cogs} ({e})")

    @cog.command()
    async def unload(self, ctx, *, text: str):
        split_text = text.split()
        msg = await ctx.reply(f"Attempting to unload cog(s): ```{split_text}```")
        try:
            for cogs in split_text:
              self.bot.unload_extension(cogs)
              console.botinfo(f"unloading {cogs}")
              await msg.edit(f"```{split_text}``` unloaded.")
        except Exception as e:
            await msg.edit(f"Cog unloading failed.\n```{e}```")
            console.error(f"Failed loading {cogs} ({e})")
        
    @cog.command()
    async def reload(self, ctx, *, text: str):
      split_text = text.split()
      msg = await ctx.reply(f"Attempting to reload cog(s): ```{split_text}```")
      try:
          for cogs in split_text:
              self.bot.reload_extension(cogs)
              console.botinfo(f"reloading {cogs}")
              await msg.edit(f"```{split_text}``` reloaded.")
      except Exception as e:
        await msg.edit(f"Cog reloading failed.\n```{e}```")
        console.error(f"Failed reloading {cogs} ({e})")

def setup(bot: commands.Bot):
    bot.add_cog(cogManagement(bot))