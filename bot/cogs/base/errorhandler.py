import discord
from console import console
from discord import Colour
from nextcord.ext import commands


class ErrorHandler(commands.Cog):
    """A cog for global error handling."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def whatserver():
        try:
            server = ctx.guild.name
        except:
            server = "Direct Message"
        return server

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError, response: str = None, reaction: str = None):
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
        elif isinstance(error, commands.NotOwner):
            reaction = '😳'
        else:
            response = f"Something went very wrong.\n```{error}```"
            reaction = '🔥'

        if response != None:
            await ctx.reply(embed=discord.Embed(
                title="Command Error",
                description=response,
                colour=Colour.red()
            ))
        if reaction != None:
            await ctx.message.add_reaction(reaction)

        # Log the error in the terminal interface
        try:
            server = ctx.guild.name
        except:
            server = "Direct Message"
        console.error(
            f'({server}) {ctx.author} used {ctx.command} and failed with: {error}')

    @commands.Cog.listener()
    async def on_command(self, ctx: commands.Context):
        try:
            server = ctx.guild.name
        except:
            server = "Direct Message"
        console.log(f'({server}) {ctx.author} used {ctx.command}')


def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))
