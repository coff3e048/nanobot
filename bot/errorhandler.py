import discord
import os
import nextcord
from env_var import env
from console import console
from discord import Color
from nextcord.ext import commands


def envlogger(self, ctx):
    global command
    global server
    global author
    loglevel = env.loglevel
    # NONE Level
    server = "Somewhere"
    author = "Someone"
    command = ctx.command
    # BASIC, command is already set. Only server is needed
    if loglevel > 0:
        try:
            server = ctx.guild.name
        except:
            server = "Direct Message"
    # MORE, command is now the whole message and author is shown
    if loglevel >= 2:
        author = ctx.author
        command = ctx.command
    # This one could be dangerous, as it also writes a log onto the filesystem.
    if loglevel >= 3:
        command = ctx.message.content


class ErrorHandler(commands.Cog):
    """A cog for global error handling."""


    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError, response = None, reaction = None):
        """A global error handler cog."""
        if isinstance(error, commands.CommandNotFound):
            reaction = '❓'
        elif isinstance(error, commands.CommandOnCooldown):
            reaction = '❄'
        elif isinstance(error, commands.MissingPermissions):
            response = f"You do not have the required permissions to run this command.\n```{error}```"
            reaction = '🚫'
        elif isinstance(error, commands.UserInputError):
            response = f"```{error}```"
            reaction = '❕'
        elif isinstance(error, commands.MissingRequiredArgument):
            response = f"Missing a required argument: {error.param}\n```{error}```"
        elif isinstance(error, commands.NotOwner):
            reaction = '😳'
        else:
            response = f"```{error}```"

        if response != None:
            await ctx.reply(embed=discord.Embed(
                description=response,
                color=Color.red()
            ), 
            delete_after=30)
        elif reaction != None:
            await ctx.message.add_reaction(reaction)

        # Log the error in the terminal interface
        envlogger(self, ctx)
        console.error(
            f'({server}) {author} used {command} and raised an error: [red]{error}[/]')


    @commands.Cog.listener()
    async def on_command(self, ctx: commands.Context):
        envlogger(self, ctx)
        console.botlog(f'({server}) {author} used {command}')


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        envlogger(self)
        console.botlog(f'Joined guild {server}')


    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        envlogger(self)
        console.botlog(f'Left guild {server}')


def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))
