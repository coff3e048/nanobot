import os
from os import getenv
import discord
from nextcord.ext import commands
from console import console


class cogManagement(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="cog", aliases=["pkg"])
    @commands.is_owner()
    async def cog(self, ctx: commands.Context, subcommand: str = 'list', cog: str = None):
        subcommands = ['list', 'load', 'unload', 'reload']
        if subcommand in subcommands:
            if subcommand == 'list':
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
                        if subcommand == 'load':
                            self.bot.load_extension(cogs)
                            env_var.append(cogs)
                        elif subcommand == 'unload':
                            self.bot.unload_extension(cogs)
                            env_var.remove(cogs)
                        elif subcommand == 'reload':
                            self.bot.reload_extension(cogs)
                        elif subcommand == 'download':
                            await ctx.reply('Coming soon!')
                    await ctx.reply(f"```{split_text}``` {subcommand}ed.")
                except Exception as e:
                    await ctx.reply(f"Cog {subcommand} failed.\n```{e}```")
                    console.error(f"Failed loading {cogs} ({e})")
        else:
            await ctx.reply(f"`{subcommand}`is not a valid subcommand.")


def setup(bot: commands.Bot):
    bot.add_cog(cogManagement(bot))
