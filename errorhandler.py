import datetime
import discord
from console import console
from discord import Colour
from nextcord.ext import commands
#from main import env

class ErrorHandler(commands.Cog):
    """A cog for global error handling."""
    def __init__(self, bot: commands.Bot):
      self.bot = bot


# There are 4 levels of logging. 
# ANONYMOUS, MINIMAL, BASIC, FULL, and FULL-FILE
# ----------------------------
# ANONYMOUS: No message type (server, dm), no user, and no command
# MINIMAL  : Logging server (excluding DM), but no user and only command
# BASIC    : Logs server / DM, user, and commands but no strings and no files
# FULL     : Logs all message types, users, commands + strings used, but not into a file.
#   - FILE : Logs whatever full has but into a file
# (FULL isnt a thing yet)

# Defaults for ANONYMOUS level

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError, response: str = None):
        """A global error handler cog."""
        if isinstance(error, commands.CommandNotFound):
            reaction = '❓'
        elif isinstance(error, commands.CommandOnCooldown):
            reaction = '❄'
        elif isinstance(error, commands.MissingPermissions):
            response = f"You do not have the required permissions to run this command.\n```{error}```"
            reaction = '🚫'
        elif isinstance(error, commands.UserInputError):
            response = f"User input error. Enter command arguments. \n```{error}```"
            reaction = '❕'
        elif isinstance(error, commands.MissingRequiredArgument):
            response = f"Missing a required argument: {error.param}\n```{error}```"
            reaction = '🗣️'
        elif isinstance(error, commands.NotOwner):
            response = None
            reaction = '😳'
        else:
            response = f"Something went very wrong.\n```{error}```"

        
        if response == None:
            pass
        else:
            errorembed = discord.Embed(title=f"Command Error", description=response, colour=Colour.red())
            await ctx.reply(embed=errorembed, delete_after=15)
        await ctx.message.add_reaction(reaction)

        # Log the error in the terminal interface
        try:
            server = ctx.guild.name
        except:
            server = "Direct Message"
        console.error(f'({server}) {ctx.author} used {ctx.command} and failed with: {error}')


    @commands.Cog.listener()
    async def on_command(self, ctx: commands.Context):
        try:
            server = ctx.guild.name
        except:
            server = "Direct Message"
        console.log(f'({server}) {ctx.author} used {ctx.command}')



def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))
