import time
import psutil
import os
import discord
import random
import asyncio
from nextcord.ext import commands
from dotenv import load_dotenv
from os import getenv
load_dotenv()


class Base(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Super basic commands
    @commands.command(name="hello")
    async def hello_world(self, ctx: commands.Context):
        """Scream to the world!"""
        await ctx.reply("Hello, world!")

    @commands.command(name="invite")
    async def invite(self, ctx: commands.Context):
        """Invite the bot to your server!"""
        inviteurl = getenv('INVITE')
        await ctx.author.send(f"Please note. This bot is in its very early stages of development. There will be bugs and possibly vulnerabilities.\n\nUse at your own risk\n{inviteurl}")

    @commands.command(name="source", aliases=["license"])
    async def license(self, ctx: commands.Context, dm: str = True):
        """Bot license and source code page"""
        embed = discord.Embed(
            title=f"nanobot",
            url=f"https://github.com/pascal48/nanobot",
            description=f"nanobot is a small project of mine to practice Python as well as build a unique working Discord bot.\n\nI'm an amateur at Python, so contributions are 100% welcome!\n*(use the link in the title)*",
            colour=discord.Colour.purple()
        ).set_thumbnail(
            url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flogos-download.com%2Fwp-content%2Fuploads%2F2016%2F10%2FPython_logo_icon.png&f=1&nofb=1"
        ).set_footer(
            text="nanobot's source code is proudly licensed under the GNU Affero General Public License (AGPL v3)!"
        )
        if dm:
            await ctx.author.send(embed=embed)
        else:
            await ctx.reply(embed=embed)

    @commands.command(name="ping")
    @commands.cooldown(1, 3, commands.BucketType.guild)
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket & API latency."""
        start_time = time.time()
        listof_responses = ['your mom', 'my balls', 'deez nuts', 'aaaaaaaaa']
        msg = await ctx.send(f"`pinging {random.choice(listof_responses)}`")
        end_time = time.time()
        await msg.edit(embed=discord.Embed(
            title="pong!",
            colour=discord.Colour.purple())
            .add_field(
            name="Bot", value=f"`{round(self.bot.latency * 1000)}ms`", inline=True)
            .add_field(
            name="Discord API", value=f"`{round((end_time - start_time) * 1000)}ms`", inline=True)
        )

    @commands.command(name="uptime", alises=["up"])
    async def uptime(self, ctx: commands.Context):
        """Get the bot's uptime"""
        p = psutil.Process(os.getpid())
        givetime = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime(p.create_time()))
        await ctx.reply(f"```Up since:\n{givetime}```")


def setup(bot: commands.Bot):
    bot.add_cog(Base(bot))
