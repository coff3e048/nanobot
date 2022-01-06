import os
import psutil
import platform
import nextcord
import sysconfig
from os import getenv
import discord
from nextcord.ext import commands
from console import console
from env_var import env


class botManagement(commands.Cog):
    def __init__(self, bot: commands.Bot):
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

    @bmg.group()
    async def clientexit(self, ctx):
        message = "Goodbye!"
        try:
            await ctx.reply(message)
        except:
            await ctx.author.send(message)

    @commands.command(name="sysinfo")
    async def client_sysinfo(self, ctx: commands.Context):
        # https://cog-creators.github.io/discord-embed-sandbox/
        embed = discord.Embed(
            title="Instance information",
            color=discord.Colour.purple()
        ).set_thumbnail(
            url=self.bot.user.avatar.url
        ).add_field(
            name="Name", value=f"`{env.botname}`", inline=True
        ).add_field(
            name="Discord User", value=f"{self.bot.user.mention}", inline=True
        ).add_field(
            name="Python Version", value=f"`{platform.python_implementation()} {platform.python_version()}`", inline=False
        ).add_field(
            name="Nextcord Version", value=f"`{nextcord.__version__}`", inline=True
        ).add_field(
            name="OS", value=f"`{sysconfig.get_platform()} {platform.release()}`", inline=False
        )
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(botManagement(bot))
