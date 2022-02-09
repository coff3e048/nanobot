import time
import psutil
import os
import discord
import random
import asyncio
from nextcord.ext import commands
from env_var import env


class Base(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="invite")
    async def invite(self, ctx: commands.Context):
        """Invite the bot to your server!"""
        await ctx.author.send(f"Please note. This bot is in its very early stages of development. There will be bugs and possibly vulnerabilities.\n\nUse at your own risk\n{inviteurl}")

    @commands.command(name="source", aliases=["license"])
    async def license(self, ctx: commands.Context, dm: str = True):
        """Bot license and source code page"""
        embed = discord.Embed(
            title=f"nanobot",
            url=f"https://github.com/pascal48/nanobot",
            description=f"nanobot is a small project of mine to practice Python as well as build a unique working Discord bot.\n\nI'm an amateur at Python, so contributions are 100% welcome!\n*(use the link in the title)*",
            colour=discord.Colour.purple()
        )
        embed.set_thumbnail(
            url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flogos-download.com%2Fwp-content%2Fuploads%2F2016%2F10%2FPython_logo_icon.png&f=1&nofb=1"
        )
        embed.set_footer(
            text="nanobot's source code is publicly licensed under the GNU Affero General Public License (AGPL v3)!"
        )
        if dm:
            await ctx.author.send(embed=embed)
        else:
            await ctx.reply(embed=embed)

    @commands.command(name="ping")
    @commands.cooldown(1, 2, commands.BucketType.guild)
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket & API latency."""
        start_time = time.time()
        listof_responses = ['your mom', 'my balls', 'deez nuts', 'aaaaaaaaa', 'steve balmer',
                            'developers', 'not discord', 'where is my son', 'fasdiniaosdfaisdf']
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
            "%Y-%m-%d %H:%M:%S",
            time.localtime(p.create_time())
        )
        await ctx.reply(f"```Up since:\n{givetime}```")

    @commands.command(name="avatar", aliases=["pfp", "a"])
    async def get_avatar(self, ctx: commands.Context, member: discord.Member = None):
        if member is None:
            member = ctx.author

        avatarurl = member.avatar.url
        avatarEmbed = discord.Embed(
            title=f"{member.name}'s avatar",
            url=avatarurl,
            color=member.color
        )
        avatarEmbed.set_image(
            url=avatarurl
        )
        try:
            await ctx.reply(embed=avatarEmbed)
        except:
            await ctx.author.send(embed=avatarEmbed)

    @commands.command(name="say", aliases=["hello"])
    @commands.is_owner()
    async def botsay(self, ctx, text: str = "Hello World!"):
        """Scream to the world!"""
        try:
            await ctx.send(text)
        except:
            await ctx.author.send(text)


def setup(bot: commands.Bot):
    bot.add_cog(Base(bot))
