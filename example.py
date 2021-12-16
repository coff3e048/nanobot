import time, psutil, os
import discord
from nextcord.ext import commands
from dotenv import load_dotenv

from os import getenv
load_dotenv()


class Base(commands.Cog):
    """A couple of simple commands."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    # Commands only the bot owner can use
    

    
    @commands.command(name="ping")
    @commands.cooldown(1, 7, commands.BucketType.guild)
    async def ping(self, ctx: commands.Context):
      """Get the bot's current websocket & API latency."""
      start_time = time.time()
      message = await ctx.send("pinging")
      end_time = time.time()
      await message.edit(f"Pong!: {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms") # It's now self.bot.latency


    @commands.command(name="avatar", aliases=["pfp","a"])
    async def get_avatar(self, ctx: commands.Context, member: discord.Member = None):
      if member == None:
        member = ctx.author
      memberAvatar = member.avatar.url
      avaEmbed = discord.Embed(title = f"{member.name}'s Avatar")
      avaEmbed.set_image(url = memberAvatar)
      await ctx.reply(embed = avaEmbed)


    @commands.command(name="ascii")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ascii(self, ctx: commands.Context, *, text: str = "Hello World!"):
    # the way this works is insanely bad, dont keep this PLEASE.
      textart = text2art(text,'random')
      file = f'ascii-{ctx.author.id}.txt'
      if len(textart) > 2000:
        if os.path.exists(file):
          os.remove(file)
          pass
        f = open(file, 'x')
        f.write(textart)
        fr = open(file, 'r')
        await ctx.reply(file=discord.File(file))
        f.close()
        os.remove(file)
      else:
        await ctx.reply(f"```{textart}```")
        

    @commands.command(name="insult")
    async def insult(self, ctx: commands.Context, member: discord.Member = None):
      insults = insult_list.list
      if member == None:
        await ctx.reply(f"{ctx.author.mention} {random.choice(insults)}")
      elif member == {bot.user.id}:
        await ctx.reply(f"{ctx.author.mention} I'm not going to insult myself you absolute baboon")
      else:
        await ctx.reply(f"{member.mention} {random.choice(insults)}")
          


def setup(bot: commands.Bot):
    bot.add_cog(Base(bot))