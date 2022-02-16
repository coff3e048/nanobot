import os
#import aiohttp
from os import getenv
import discord
from nextcord.ext import commands
from console import console


class CogManager(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #async def get_cog(self, ctx):


    @commands.group(name="cog", aliases=["pkg", "c"])
    @commands.is_owner()
    async def cog(self, ctx: commands.Context, subcommand: str = 'list', cog: str = None):
        if not ctx.invoked_subcommand:
            await ctx.reply(f"{subcommand} is not a valid command.")
        coglist = []
        for cogs in self.bot.cogs:
            coglist.append(cogs)
        try:
            await ctx.reply(f"```{coglist}```")
        except Exception as e:
            await ctx.reply(f"{e}")

    @cog.group(name="list")
    async def list(self, ctx: commands.Context):
        coglist = []
        for cogs in self.bot.cogs:
            cogslist.append(cogs)
        try:
            await ctx.reply(f"```{coglist}```")
        except Exception as e:
            await ctx.reply(f"{e}")

    @cog.group(name="load")
    async def load(self, ctx: commands.Context, *, cogs: str = None):
        split_text = cogs.split()
        for cogs in split_text:
            try:
                self.bot.load_extension(cogs)
                await ctx.reply(f"{cogs} loaded.")
            except Exception as e:
                await ctx.reply(e)
            
    @cog.group(name="unload")
    async def unload(self, ctx: commands.Context, *, cogs: str = None):
        split_text = cogs.split()
        for cogs in split_text:
            try:
                self.bot.unload_extension(cogs)
                await ctx.reply(f"{cogs} unloaded.")
            except Exception as e:
                await ctx.reply(e)

    @cog.group(name="reload")
    async def reload(self, ctx: commands.Context, *, cogs: str = None):
        split_text = cogs.split()
        for cogs in split_text:
            try:
                self.bot.reload_extension(cogs)
                await ctx.reply(f"{cogs} reloaded.")
            except:
                self.bot.load_extension(cogs)

    @cog.group(name="install")
    async def install(self, ctx: commands.Context, repo: str = None, *, cogs: str = None):
        await ctx.reply("This functionality will come soon!")

    @cog.group(name="uninstall")
    async def uninstall(self, ctx: commands.Context, *, cogs: str = None):
        await ctx.reply("This functionality will come soon!")

def setup(bot: commands.Bot):
    bot.add_cog(CogManager(bot))
