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
    @commands.command(name="shutdown", aliases=["exit", "quit"])
    @commands.is_owner()
    async def shutdown(self, ctx: commands.Context):
      await ctx.reply("Exiting...")
      self.bot.change_presence(activity=discord.Game(name="Shutting down..."))
      exit()

    @commands.command(name="set")
    @commands.is_owner()  
    async def set(self, ctx):
        await ctx.reply("Set not a working command yet")



    # Super basic commands
    @commands.command(name="hello")
    async def hello_world(self, ctx: commands.Context):
      await ctx.reply("Hello, world!")


    @commands.command(name="invite")
    async def invite(self, ctx: commands.Context):
      inviteurl = getenv('INVITE')
      await ctx.author.send(f"Please note. This bot is in its very early stages of development. There will be bugs and possibly vulnerabilities.\n\nUse at your own risk\n{inviteurl}")


    @commands.command(name="source", aliases=["license"])
    async def license(self, ctx: commands.Context):
      gitpage = getenv('SOURCEPAGE')
      if gitpage == None:
        gitpage = "https://github.com/pascal48/nanobot"
      await ctx.reply(f"nanobot is released under the GNU General Public License (GPL v3), making it fully open source. Contributions are welcome to bring it up to it's full functionality like its redbot predecesor \n\ngithub: <{gitpage}>")


    @commands.command(name="ping")
    @commands.cooldown(1, 3, commands.BucketType.guild)
    async def ping(self, ctx: commands.Context):
      """Get the bot's current websocket & API latency."""
      start_time = time.time()
      message = await ctx.send("pinging")
      end_time = time.time()
      await message.edit(f"```Pong!: {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms```")


    @commands.command(name="uptime", alises=["up"])
    async def uptime(self, ctx: commands.Context):
      p = psutil.Process(os.getpid())
      givetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(p.create_time()))
      await ctx.reply(f"```Up since:\n{givetime}```")


    @commands.command(name="avatar", aliases=["pfp","a"])
    async def get_avatar(self, ctx, member: discord.Member = None):
      if member == None:
        member = ctx.author
      memberAvatar = member.avatar.url
      avaEmbed = discord.Embed(title = f"{member.name}'s Avatar")
      avaEmbed.set_image(url = memberAvatar)
      await ctx.reply(embed = avaEmbed)





def setup(bot: commands.Bot):
    bot.add_cog(Base(bot))
