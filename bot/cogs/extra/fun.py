import random
import asyncio
import os
import discord
import numpy.random
from nextcord.ext import commands
from art import text2art


class Fun(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="roll")
    async def roll(self, ctx, first: int = 1, second: int = 100):
        await ctx.reply(f"{random.randint(first,second)} *({first} - **{second}**)*")

    @commands.command(name="choose")
    async def choose(self, ctx: commands.Context, *, text: str = None):
        if text:
            await ctx.reply(random.choice(text.split()))
        else:
            await ctx.reply(f"You've given me nothing to chose between.")

    @commands.command(name="8ball")
    async def eightball(self, ctx: commands.Context):
        responses = [
            "It is certain",
            "Outlook good",
            "You may rely on it",
            "Ask again later",
            "Concentrate and ask again",
            "Reply hazy, try again",
            "My reply is no",
            "My sources say no"
        ]
        msg = await ctx.reply(':8ball: *Thinking*')
        choice = numpy.random.choice(responses, 1, p=[0.15, 0.15, 0.15, 0.05, 0.05, 0.15, 0.15, 0.15])
        await asyncio.sleep(1)
        await msg.edit(':8ball: '+"...".join(choice))

    @commands.command(name="ascii")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def ascii(self, ctx: commands.Context, *, text: str = "Hello World!"):
        textart = text2art(text, 'random')
        file = f'ascii-{ctx.author.id}.txt'
        try:
            await ctx.reply(f"```{textart}```")
        except:
            data = io.BytesIO(textart)
            await ctx.reply(file=discord.File(data, file))



def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
