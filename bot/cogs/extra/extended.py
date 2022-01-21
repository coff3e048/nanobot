import aiohttp
import cowsay
import re
import discord
from nextcord.ext import commands


class Extended(commands.Cog):
    """Search YouTube for videos."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.group(name="cowsay")
    async def say(self, ctx: commands.Context, saytype: str = "cow", *, text: str = "Hello world!"):
        if saytype in cowsay.char_names:
            try:
                await ctx.reply(f"```{cowsay.get_output_string(saytype,text)}```")
            except Exception as e:
                await ctx.reply(f"```{e}```")
        else:
            await ctx.reply(f"Valid characters: ```{cowsay.char_names}```")


def setup(bot: commands.Bot):
    bot.add_cog(Extended(bot))
