import cowsay
import discord
import typing
from nextcord.ext import commands

class csay(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

  #>>> cowsay.char_names
  #['beavis', 'cheese', 'daemon', 'cow', 'dragon', 'ghostbusters', 'kitty', 'meow', 'milk', 'pig', 'stegosaurus', 'stimpy', 'trex', 'turkey', 'turtle', 'tux']

    @commands.command(name="cowsay")
    async def _cowsay(self, ctx, *, text: str):
        await ctx.reply(f"```{cowsay.get_output_string('cow',text)}```")
    
def setup(bot: commands.Bot):
    bot.add_cog(csay(bot))