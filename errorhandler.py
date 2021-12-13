import colorama, datetime

import discord
from discord import Colour
from nextcord.ext import commands
from colorama import Fore, Back, Style


class ErrorHandler(commands.Cog):
    """A cog for global error handling."""

    def __init__(self, bot: commands.Bot):
      self.bot = bot


    @commands.Cog.listener()
    async def on_command(self, ctx):
      x = datetime.datetime.now()
      xtime = x.strftime("%X")
      try:
        server = ctx.guild.name
      except:
        server = "Direct Message"
      user = ctx.author
      command = ctx.command
      print(f'{xtime}{Style.DIM} | INFO: ({server}) {user} used {command}{Style.RESET_ALL}')


    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """A global error handler cog."""

        if isinstance(error, commands.CommandNotFound):
            reaction = '❔'
        elif isinstance(error, commands.CommandOnCooldown):
            reaction = '❄'
            reply = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds.\n```error: {error}```"
        elif isinstance(error, commands.MissingPermissions):
            reaction = '🚫'
            reply = f"You do not have the required permissions to run this command.\n ```error: {error}```"
        elif isinstance(error, commands.UserInputError):
            reaction = '❕'
            reply = f"User input error. Enter command arguments. \n ```error: {error}```"
        elif isinstance(error, commands.MissingRequiredArgument):
            reaction = '❓'
            reply = f"Missing a required argument: {error.param}\n ```error: {error}```"
        elif isinstance(error, commands.NotOwner):
            reaction = '😳'
            reply = f"Only the bot owner can use this command.\n ```error: {error}```"
        else:
            reply = f"Something went wrong trying to use this command.\n ```error: {error}```"

        embed = discord.Embed(title="Command Error", description=reply, colour=Colour.red())
        errorreply = await ctx.reply(embed=embed, delete_after=10)
        await ctx.message.add_reaction(reaction)

        x = datetime.datetime.now()
        xtime = x.strftime("%X")
        try:
          server = ctx.guild.name
        except:
          server = "Direct Message"
        user = ctx.author
        command = ctx.command
        print(f'{xtime}{Fore.RED} | ERRO: ({server}) {user} used {command} but failed with {error}{Style.RESET_ALL}')

def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))
