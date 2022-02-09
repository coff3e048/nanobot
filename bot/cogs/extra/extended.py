import aiohttp
import cowsay
import re
import discord
import io
from nextcord.ext import commands


class Extended(commands.Cog):
    """Search YouTube for videos."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(name="cowsay")
    async def say(self, ctx: commands.Context, saytype: str = "cow", *, text: str = "Hello world!"):
        cowoutput = cowsay.get_output_string(saytype, text)
        if saytype in cowsay.char_names:
            try:
                await ctx.reply(f"```{cowoutput}```")
            except:
                data = io.BytesIO(cowoutput)
                await ctx.reply(file=discord.File(data, f'cowsay-{ctx.author.id}.txt'))
        else:
            await ctx.reply(f"Valid characters: ```{cowsay.char_names}```")


def setup(bot: commands.Bot):
    bot.add_cog(Extended(bot))
