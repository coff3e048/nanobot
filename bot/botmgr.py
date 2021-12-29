import os
import subprocess
import discord
from nextcord.ext import commands


class botManagement(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Commands only the bot owner can use

    @commands.command(name="set")
    @commands.is_owner()
    async def _set(self, ctx):
        await ctx.reply("Set not a working command yet")

    @commands.command(name="dump")
    @commands.is_owner()
    async def dump(self, ctx):
        try:
            await ctx.reply(file=discord.File(cog))
        except Exception as e:
            await ctx.reply(f"{e}")

    @commands.group()
    @commands.is_owner()
    async def bmg(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.reply("No invoked subcommand")

    @bmg.group(name="shutdown", aliases=["exit", "quit"])
    @commands.is_owner()
    async def shutdown(self, ctx: commands.Context):
        await ctx.reply("Exiting...")
        await self.bot.change_presence(activity=discord.Game(name="Shutting down..."))
        exit()

    @bmg.group(name="exec")
    async def exec(self, ctx, *, text: str):
        cmd = os.system(text, stdout=subprocess.PIPE)
        await ctx.reply(cmd.stdout.read())

    @bmg.group(name="guilds")
    async def bmg_listguilds(self, ctx):
        guilds_list = []
        for guilds in self.bot.guilds:
            guilds_list.append(guilds)
        try:
            await ctx.reply(f'{guildlist}')
        except:
            await ctx.reply("Couldn't print guilds.")


def setup(bot: commands.Bot):
    bot.add_cog(botManagement(bot))
