import time, random
import discord
from nextcord.ext import commands


class funCommands(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
      self.bot = bot

    @commands.command(name="choose")
    async def choose(self, ctx: commands.Context, *, text: str):
      a = [str(x) for x in text.split()]
      chooselist=[]
      for word in a:
        chooselist.append(word)
      numopts = len(chooselist)
      randnum = random.randint(0, numopts)
      await ctx.reply(chooselist[randnum])
      

    @commands.command(name="8ball")
    async def eightball(self, ctx: commands.Context, *, text: str):  
        responses = ["It is certain", "Outlook good", "You may rely on it", "Ask again later", "Concentrate and ask again", "Reply hazy, try again", "My reply is no", "My sources say no" ]
        numofresponses = len(responses)
        randnum = random.randint(0,numofresponses)
        await ctx.reply(f":8ball: {responses[randnum]}")
      

def setup(bot: commands.Bot):
    bot.add_cog(funCommands(bot))
