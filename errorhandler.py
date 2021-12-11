import colorama

import discord
from discord import Colour
from nextcord.ext import commands


class ErrorHandler(commands.Cog):
    """A cog for global error handling."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """A global error handler cog."""

        if isinstance(error, commands.CommandNotFound):
            message = f"This command doesn't exist. Try another\n ```{error}```"
        elif isinstance(error, commands.CommandOnCooldown):
            message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds.\n```error: {error}```"
        elif isinstance(error, commands.MissingPermissions):
            message = f"You do not have the required permissions to run this command.\n ```error: {error}```"
        elif isinstance(error, commands.UserInputError):
            message = f"User input error. Enter command arguments. \n ```error: {error}```"
        elif isinstance(error, commands.MissingRequiredArgument):
            message = f"Missing a required argument: {error.param}\n ```error: {error}```"
        elif isinstance(error, commands.NotOwner):
            message = f"Only the bot owner can use this command.\n ```error: {error}```"
        else:
            message = f"Something went wrong trying to use this command.\n ```error: {error}```"

        embed = discord.Embed(title=f"Command Error", description=message, colour=Colour.red())
        await ctx.reply(embed=embed)
        print(f"")
#       await ctx.message.delete(delay=5)

def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))
