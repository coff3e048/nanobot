import os
import psutil
from os import getenv
import discord
import nextcord
from nextcord.ext import commands
from console import console
from env_var import env


class botManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="dump")
    @commands.is_owner()
    async def dump(self, ctx: commands.Context, file: str = None):
        try:
            await ctx.reply(file=discord.File(file))
        except Exception as e:
            await ctx.reply(f"```{e}```")


    @commands.group(name="bmg")
    @commands.is_owner()
    async def bmg(self, ctx: commands.Context):
        if ctx.invoked_subcommand is None:
            await ctx.reply("No invoked subcommand")

    @bmg.group()
    async def guilds(self, ctx: commands.Context):
        guildlist = []
        for guilds in bot.guilds:
            guildlist.append(guilds)
        try:
            await ctx.reply(f'{guildlist}')
        except Exception as e:
            await ctx.reply(f"Error: ```{e}```")

    @bmg.group()
    async def findusers(self, ctx: commands.Context):
        userlist = []
        for users in bot.users:
            userlist.append(users)
        try:
            await ctx.reply(f'```{userlist}```')
        except Exception as e:
            await ctx.reply(f"Error: ```{e}```")


    @commands.command(name="sysinfo")
    async def client_sysinfo(self, ctx: commands.Context):
    # https://cog-creators.github.io/discord-embed-sandbox/
        embed=discord.Embed(
            title="Instance information",
            color=discord.Colour.magenta()
        ).add_field(
            name="Name", value=env.botname, inline=True
        ).add_field(
            name="Discord User", value=bot.user.mention, inline=True
        ).add_field(
            name="Python Version", value=platform.architecture(), inline=False
        ).add_field(
            name="Nextcord Version", value=f"{nextcord.version_info} {nextcord.__version__}"
        ).add_field(
            name="OS", value=platform.system(), inline=True
        ).add_field(
            name="Version", value=platform.version(), inline=True
        )
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(botManagement(bot))
