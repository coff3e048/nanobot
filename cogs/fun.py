import time, random, asyncio, cowsay, os
import discord
from .insultfile import insult_list
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
      if text == None:
        await ctx.reply(f"You've given me nothing to chose between.")
      else:
        await ctx.reply(random.choice(text.split()))

    @commands.command(name="8ball")
    async def eightball(self, ctx: commands.Context, *, text: str):  
        responses = ["It is certain", "Outlook good", "You may rely on it", "Ask again later", "Concentrate and ask again", "Reply hazy, try again", "My reply is no", "My sources say no" ]
        message = await ctx.reply(':8ball: *Thinking...*')
        await asyncio.sleep(1)
        await message.edit(f':8ball: {(random.choice(responses))}')

    @commands.command(name="ascii")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def ascii(self, ctx: commands.Context, *, text: str = "Hello World!"):
    # the way this works is insanely bad, dont keep this PLEASE.
      textart = text2art(text,'random')
      file = f'ascii-{ctx.author.id}.txt'
      if len(textart) > 2000:
        if os.path.exists(file):
          os.remove(file)
        else:

          f = open(file, 'x')
          f.write(str(textart))
          f.close()

          fr = open(file, 'r')
          await ctx.reply(file=discord.File(file))
          f.close()
          fr.close()
          os.remove(file)
      else:
        await ctx.reply(f"```{textart}```")
        
    @commands.command(name="insult")
    async def insult(self, ctx, member: discord.Member = None):
      insults = insult_list.list
      if member == None:
        await ctx.reply(f"{ctx.author.mention} {random.choice(insults)}")
      #elif member == self.bot.user.id:
        #await ctx.reply(f"{ctx.author.mention} I'm not stupid, why would I insult myself?")
      else:
        await ctx.reply(f"{member.mention} {random.choice(insults)}")
          

def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
