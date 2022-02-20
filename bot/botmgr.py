import os
import psutil
import aiohttp
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

    @commands.command(name='exit', aliases=['quit', 'bye', 'shutdown', 'stop'])
    @commands.is_owner()
    async def quit(self, ctx: commands.Context, timeset: int = None):
        if timeset:
            await ctx.reply(f'Stopping in {timeset} seconds.')
            await asyncio.sleep(timeset)
        message = 'Goodbye!'
        try:
            await ctx.reply(message)
        except:
            await ctx.author.send(message)
        await self.bot.close()

    @commands.command(name='download', aliases=['dl'])
    @commands.is_owner()
    async def botdl(self, ctx: commands.Context, URL: str = None, name: str = None):
        async with self.session.get(URL, headers={}) as response:
            if response.status == 200:
                path = 'dl'
                data = await response.read()
                filename = URL.split('/')
                with open(f"{path}/{URL[-1]}", 'w') as f:
                    f.write(data)
                    f.close()
            else:
                await ctx.reply(f"```Response from URL returned {response.status}```")

    @commands.command(name='dump')
    @commands.is_owner()
    async def dump(self, ctx: commands.Context, file: str = None):
        try:
            await ctx.reply(file=discord.File(file))
        except Exception as e:
            await ctx.reply(f'```{e}```')

    @commands.command(name='sysinfo')
    async def client_sysinfo(self, ctx: commands.Context):
        # https://cog-creators.github.io/discord-embed-sandbox/
        embed = discord.Embed(
            title='Instance Information',
            color=discord.Color.purple()
        )
        embed.set_thumbnail(
            url=self.bot.user.avatar.url
        )
        embed.add_field(
            name='Name', value=f'`{env.botname}`', inline=True
        )
        embed.add_field(
            name='Discord User', value=f'{self.bot.user}\n{self.bot.user.mention}', inline=True
        )
        embed.add_field(
            name='Python Version', value=f'`{platform.python_implementation()} {platform.python_version()}`', inline=False
        )
        embed.add_field(
            name='Nextcord Version', value=f'`{nextcord.__version__}`', inline=True
        )
        embed.add_field(
            name='OS', value=f'`{sysconfig.get_platform()} {platform.release()}`', inline=False
        )
        await ctx.reply(embed=embed)

    @commands.group(name='bmg')
    @commands.is_owner()
    async def bmg(self, ctx: commands.Context):
        if not ctx.invoked_subcommand:
            await ctx.reply('No invoked subcommand')

    @bmg.group()
    async def guilds(self, ctx: commands.Context):
        guildlist = bot.guilds
        await ctx.reply(f'{guildlist}')

    @bmg.group(name='exec', aliases=['exe'])
    async def cmdmgmt(self, ctx: commands.Context, *, cmd: str):
        subprocesspipe = asyncio.subprocess.PIPE
        child = await asyncio.create_subprocess_shell(
            cmd,
            stderr=subprocesspipe,
            stdout=subprocesspipe
        )
        await ctx.reply(f"```{stdout}```")


def setup(bot: commands.Bot):
    bot.add_cog(botManagement(bot))
