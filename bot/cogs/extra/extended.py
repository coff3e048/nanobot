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

    @commands.command(name="cowsay")
    async def _cow_say(self, ctx, saytype: str = "cow", *, text: str = "Hello world!"):
        cowoutput = cowsay.get_output_string(saytype, text)
        if saytype in cowsay.char_names:
            try:
                await ctx.reply(f"```{cowoutput}```")
            except:
                data = io.BytesIO(cowoutput)
                await ctx.reply(file=discord.File(data, f'cowsay-{ctx.author.id}.txt'))
        else:
            char = ""
            for characters in char_names:
                char.append(characters)
            await ctx.reply(discord.Embed(
                title='Valid Characters',
                description=char
            ))


def setup(bot: commands.Bot):
    bot.add_cog(Extended(bot))
