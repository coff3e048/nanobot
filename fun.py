import time, random, asyncio, cowsay
import discord
from nextcord.ext import commands


class fun(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
      self.bot = bot

    @commands.command(name="roll")
    async def roll(self, ctx:commands.Context, first: int, second: int):
      await ctx.reply(f"{random.randint(first,second)}")

    @commands.command(name="choose")
    async def choose(self, ctx: commands.Context, *, text: str):
      await ctx.reply(random.choice(text.split()))

    @commands.command(name="8ball")
    async def eightball(self, ctx: commands.Context, *, text: str):  
        responses = ["It is certain", "Outlook good", "You may rely on it", "Ask again later", "Concentrate and ask again", "Reply hazy, try again", "My reply is no", "My sources say no" ]
        message = await ctx.reply(':8ball: *Rolling...*')
        await asyncio.sleep(1)
        await message.edit(f':8ball: {(random.choice(responses))}')


def setup(bot: commands.Bot):
    bot.add_cog(fun(bot))
