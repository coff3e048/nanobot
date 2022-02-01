import os
from os import getenv
import discord
from nextcord.ext import commands
from console import console


class CogManager(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command(name="cog", aliases=["pkg"])
    @commands.is_owner()
    async def cog(self, ctx: commands.Context, subcommand: str = 'list', cog: str = None):
        subcommands = ['list', 'load', 'unload', 'reload']
        if subcommand in subcommands:
            if subcommand is 'list':
                coglist = str(self.bot.cogs).replace('[', '').replace(']', '').replace(
                    "'", "").replace(",", "\n").replace(" ", "")
                try:
                    await ctx.reply(f"```{coglist}```")
                except Exception as e:
                    await ctx.reply(f"{e}")
            else:
                split_text = cog.split()
                try:
                    for cogs in split_text:
                        if subcommand is 'load':
                            self.bot.load_extension(cogs)
                        elif subcommand is 'unload':
                            self.bot.unload_extension(cogs)
                        elif subcommand is 'reload':
                            self.bot.reload_extension(cogs)
                        elif subcommand is 'download':
                            await ctx.reply('Coming soon!')
                    await ctx.reply(f"```{split_text}``` {subcommand}ed.")
                except Exception as e:
                    await ctx.reply(f"Cog {subcommand} failed.\n```{e}```")
                    console.error(f"Failed loading {cogs} ({e})")
        else:
            await ctx.reply(f"`{subcommand}`is not a valid subcommand.")


def setup(bot: commands.Bot):
    bot.add_cog(CogManager(bot))
