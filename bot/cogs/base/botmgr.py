import os
from os import getenv
import discord
from nextcord.ext import commands
from console import console
from env_var import loaded


class botManagement(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command(name="dump")
    @commands.is_owner()
    async def dump(self, ctx, file: str = None):
        try:
            await ctx.reply(file=discord.File(file))
        except Exception as e:
            await ctx.reply(f"```{e}```")

    @commands.group()
    @commands.is_owner()
    async def bmg(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.reply("No invoked subcommand")

    @bmg.group()
    async def exec(self, ctx, *, text: str):
        cmd = os.system(text, stdout=subprocess.PIPE)
        await ctx.reply(cmd.stdout.read())

    @bmg.group()
    async def guilds(self, ctx):
        guildlist = []
        for guilds in bot.guilds:
            guildlist.append(guilds)
        try:
            await ctx.reply(f'{guildlist}')
        except:
            await ctx.reply("Couldn't print guilds.")


def setup(bot: commands.Bot):
    bot.add_cog(botManagement(bot))
