import time, random, asyncio, cowsay
import discord
from nextcord.ext import commands
from art import text2art


class Fun(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
      self.bot = bot

    @commands.command(name="roll")
    async def roll(self, ctx, first: int = 1, second: int = 25):
      await ctx.reply(f"{random.randint(first,second)}")

    @commands.command(name="choose")
    async def choose(self, ctx: commands.Context, *, text: str = None):
      if text == None:
        await ctx.reply(f"You've given me nothing to chose between.")
      else:
        await ctx.reply(random.choice(text.split()))

    @commands.command(name="8ball")
    async def eightball(self, ctx: commands.Context, *, text: str = None):  
        responses = ["It is certain", "Outlook good", "You may rely on it", "Ask again later", "Concentrate and ask again", "Reply hazy, try again", "My reply is no", "My sources say no" ]
        message = await ctx.reply(':8ball: *Rolling...*')
        await asyncio.sleep(1)
        await message.edit(f':8ball: {(random.choice(responses))}')

    @commands.command(name="ascii")
    async def ascii(self, ctx: commands.Context, *,text: str = "Hello World!"):
      textart = text2art(text,"random")
      await ctx.reply(f"```{textart}```")


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
