import cowsay
import discord
import typing
from nextcord.ext import commands

class csay(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

  #cowsay.char_names
  #['beavis', 'cheese', 'daemon', 'cow', 'dragon', 'ghostbusters', 'kitty', 'meow', 'milk', 'pig', 'stegosaurus', 'stimpy', 'trex', 'turkey', 'turtle', 'tux']


    @commands.group(name="say")
    async def say(self, ctx: commands.Context, saytype: str = "cow", *, text: str = "Hello world!"):
        try:
            await ctx.reply(f"```{cowsay.get_output_string(saytype,text)}```")
        except Exception as e:
            await ctx.reply(f"```{e}```")
      

def setup(bot: commands.Bot):
    bot.add_cog(csay(bot))