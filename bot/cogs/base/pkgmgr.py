import os
import aiohttp
import aiofiles.os
from os import getenv
import discord
from nextcord.ext import commands
from console import console


class CogManager(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    @commands.group(name="cog", aliases=["pkg", "c"])
    @commands.is_owner()
    async def cog(self, ctx):
        if ctx.invoked_subcommand == None:
            await ctx.reply(f"{subcommand} is not a valid command.")

    @cog.group(name="list")
    async def c_list(self, ctx):
        await ctx.reply(f'```{self.bot.cogs}```')

    @cog.group(name="load")
    async def load(self, ctx, *, cogs: str = None):
        for cogs in cogs.split():
            try:
                self.bot.load_extension(cogs)
                await ctx.reply(f"```{cogs} loaded.```")
            except:
                pass

    @cog.group(name="unload")
    async def unload(self, ctx, *, cogs: str = None):
        for cogs in cogs.split():
            try:
                self.bot.unload_extension(cogs)
                await ctx.reply(f"```{cogs} unloaded.```")
            except:
                pass

    @cog.group(name="reload")
    async def reload(self, ctx, *, cogs: str = None):
        for cogs in cogs.split():
            try:
                self.bot.reload_extension(cogs)
            except commands.ExtensionNotLoaded:
                self.bot.load_extension(cogs)
            await ctx.reply(f"```{cogs} reloaded.```")

    @cog.group(name="install")
    async def install(self, ctx, repo: str = None, *, cogs: str = None):
        async with self.session.get(URL, headers={}) as response:
            if response.status == 200:
                data = await response.read()
                filename = URL.split('/')
                with open(URL[-1], 'w') as f:
                    f.write(data)
                    f.close()
            else:
                await ctx.reply(f"```URL ({URL}) returned {response.status}```")

    @cog.group(name="uninstall")
    async def uninstall(self, ctx, *, cogs: str = None):
        await ctx.reply("This functionality will come soon!")


def setup(bot: commands.Bot):
    bot.add_cog(CogManager(bot))
