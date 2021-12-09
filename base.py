import time, psutil, os
import discord
from nextcord.ext import commands



# loaded pretty much just for the invite command
from dotenv import load_dotenv
from os import getenv
load_dotenv()


class baseCommands(commands.Cog):
    """A couple of simple commands."""
    
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Commands only the bot owner can use
    @commands.command(name="shutdown")
    @commands.is_owner()
    async def shutdown(self, ctx: commands.Context):
      await ctx.reply("Exiting...")
      exit()

    @commands.command(name="setstatus")
    @commands.is_owner()  
    async def setstatus(self, ctx: commands.Context, *, text: str):
      """Set the bot's status."""
      await self.bot.change_presence(activity=discord.Game(name=text))


    # Super basic commands
    @commands.command(name="hello")
    async def hello_world(self, ctx: commands.Context):
      await ctx.reply("Hello, world!")

    @commands.command(name="invite")
    async def invite(self, ctx: commands.Context):
      inviteurl = getenv('INVITE')
      await ctx.author.send(f"Please note. This bot is in its very early stages of development. There will be bugs and possibly vulnerabilities.\n\nUse at your own risk\n {inviteurl}")

    @commands.command(name="source")
    async def license(self, ctx: commands.Context):
      await ctx.send("nanobot utilizes the GNU General Public License v3 in its source code, and is fully open source. Contributions are welcome to bring it up to it's full functionality like its redbot predecesor \n\ngithub: <https://github.com/pascal48/nanobot>")

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
      """Get the bot's current websocket & API latency."""
      start_time = time.time()
      message = await ctx.send("Sending ping...", delete_after=2)
      end_time = time.time()
      await ctx.reply(f"Pong!: {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms") # It's now self.bot.latency

    @commands.command(name="uptime")
    async def uptime(self, ctx: commands.Context):
      p = psutil.Process(os.getpid())
      givetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(p.create_time()))
      await ctx.reply(f"```Up since:\n{givetime}```")


    @commands.command(name="say")
    async def say(self, ctx: commands.Context, *, text: str):
      await ctx.send(text)



def setup(bot: commands.Bot):
    bot.add_cog(baseCommands(bot))
