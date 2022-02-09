import aiohttp
import cowsay
import re
import discord
import base64
from nextcord.ext import commands


class textencode(commands.Cog):
    """Search YouTube for videos."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(name="encode")
    async def txtencode(self, ctx: commands.Context):
        if ctx.invoked_subcommand is None:
            await ctx.reply('No invoked subcommand')

    @encode.group()
    async def encode_txtb64(self, ctx: commands.Context, text: str):
        string_bytes = text.encode('ascii')
        base64_bytes = base64.b64encode(string_bytes)
        base64_string = base64_bytes.decode("ascii")
        await ctx.reply(f"{base64_string}")

    @commands.group(name="decode")
    async def txtdecode(self, ctx: commands.Context):
        if ctx.invoked_subcommand is None:
            await ctx.reply('No invoked subcommand')

    @encode.group(name="base64")
    async def decode_txtb64(self, ctx: commands.Context, text: str):
        string_bytes = text.encode('ascii')
        base64_bytes = base64.b64encode(string_bytes)
        base64_string = base64_bytes.decode("ascii")
        await ctx.reply(f"{base64_string}")


def setup(bot: commands.Bot):
    bot.add_cog(textencode(bot))
