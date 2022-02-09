import os
import psutil
import platform
import nextcord
import sysconfig
import discord
from nextcord.ext import commands
from console import console
from env_var import env


class botManagement(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='dump')
    @commands.is_owner()
    async def dump(self, ctx: commands.Context, file: str = None):
        try:
            await ctx.reply(file=discord.File(file))
        except Exception as e:
            await ctx.reply(f'```{e}```')
        else:
            await ctx.author.send(file=discord.File(file))

    @commands.command(name='sysinfo')
    async def client_sysinfo(self, ctx: commands.Context, full: str):
        botavatar = self.bot.user.avatar.url
        botuser = self.bot.user
        pyversion_imp = platform.python_implementation()
        pyversion = platform.python_version()
        nxtcord_ver = nextcord.__version__
        osplatform = sysconfig.get_platform()
        osplatform_rel = platform.release()
        # https://cog-creators.github.io/discord-embed-sandbox/
        embed = discord.Embed(
            title='Instance information',
            color=self.bot.user.accent_color
        )
        embed.set_thumbnail(
            url=botavatar
        )
        embed.add_field(
            name='Name', value=f'`{env.botname}`', inline=True
        )
        embed.add_field(
            name='Discord User', value=f'{botuser}\n{botuser.mention}', inline=True
        )
        embed.add_field(
            name='Python Version', value=f'`{pyversion_imp} {pyversion}`', inline=False
        )
        embed.add_field(
            name='Nextcord Version', value=f'`{nxtcord_ver}`', inline=True
        )
        embed.add_field(
            name='OS', value=f'`{osplatform} {osplatform_rel}`', inline=False
        )
        await ctx.reply(embed=embed)

    @commands.group(name='bmg')
    @commands.is_owner()
    async def bmg(self, ctx: commands.Context):
        if ctx.invoked_subcommand == None:
            await ctx.reply('No invoked subcommand')

    @bmg.group()
    async def guilds(self, ctx: commands.Context):
        guildlist = bot.guilds
        try:
            await ctx.reply(f'{guildlist}')
        except Exception as e:
            await ctx.reply(f'Error: ```{e}```')

    @bmg.group(name='exit', aliases=['quit', 'bye', 'shutdown', 'stop'])
    async def quit(self, ctx: commands.Context, timeset: int = None):
        if timeset != None:
            message = f'Stopping in {timeset} seconds.'
            await ctx.reply(message)
            await asyncio.sleep(timeset)
        message = 'Goodbye!'
        try:
            await ctx.reply(message)
        except:
            await ctx.author.send(message)
        exit()

    @bmg.group(name='command', aliases=['c'])
    async def cmdmgmt(self, ctx: commands.Context, cmd: str):
        await ctx.reply('...')


def setup(bot: commands.Bot):
    bot.add_cog(botManagement(bot))
