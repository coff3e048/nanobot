from discord.ext import commands


class ErrorHandler(commands.Cog):
    """A cog for global error handling."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """A global error handler cog."""

        if isinstance(error, commands.CommandNotFound):
            message = "This command doesn't exist, or is broken."
        elif isinstance(error, commands.CommandOnCooldown):
            message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds.\n```error: CommandOnCooldown```"
        elif isinstance(error, commands.MissingPermissions):
            message = "You do not have the required permissions to run this command.\n```error: MissingPermissions```"
        elif isinstance(error, commands.UserInputError):
            message = "User input error. Check for typos?\n```error: UserInputError```"
        elif isinstance(error, commands.MissingRequiredArgument):
            message = f"Missing a required argument: {error.param}\n```error: MissingRequiredArgument```"
        elif isinstance(error, commands.NotOwner):
            message = "Only the bot owner can use this command\n```error: NotOwner```"
        elif isinstance(error, commands.CommandInvokeError):
            message = f"Something has gone wrong on the backend.\n```error: CommandInvokeError```"
        else:
            message = "Something went wrong trying to use this command.\n**HINT**: It might not exist, or it's just broken"

        await ctx.send(message)
#       await ctx.message.delete(delay=5)

def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))
