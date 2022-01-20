import yt_dlp
import os
import subprocess
import discord
import asyncio
import aiofiles.os
from nextcord.ext import commands
from env_var import env


class ytdlcmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ytdl", alias=["youtubedl"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def yt_dl(self, ctx, query: str = None, convert: str = "video"):

        # Example video(s): http://www.youtube.com/watch?v=BaW_jenozKc
        #                   http://www.youtube.com/watch?v=jNQXAC9IVRw
        #                   https://youtu.be/khK_afMwAdA
        #
        # Btw, this script is incredibly garbage and doesn't work very well. When a user tries to use [p]ytdl, the whole bot will stop and wait until the download / upload is finished.

        with yt_dlp.YoutubeDL() as ydl:
            info_dict = ydl.extract_info(query, download=False)
            video_id = info_dict.get("id", None)

        dlpath = "'.www/temp/%(id)s.%(ext)s'"
        usage = f"{env.prefix}ytdl 'https://youtube.com/...' video / audio (default: video)"

        if query == None:
            await ctx.reply(f"No YouTube URL found.\n```{usage}```")
        else:
            if convert == 'video':
                media_format = 'webm'
                opts = f'--recode-video {media_format}'
            elif convert == 'audio':
                media_format = 'mp3'
                opts = f'-x --audio-format {media_format}'
            elif convert == 'opus':
                media_format = 'opus'
                opts = f'-x --audio-format {media_format}'
            else:
                await ctx.reply(f"Invalid usage.\n```{usage}```")

        # And here lies the major problem.
            try:
                subprocesspipe = asyncio.subprocess.PIPE
                child = await asyncio.create_subprocess_shell(
                    f"./bin/yt-dlp --max-filesize 300M -f 22/18/5/36 --no-playlist {opts} --break-on-existing --no-exec -o {dlpath} {query}",
                    stderr=subprocesspipe,
                    stdout=subprocesspipe
                )
                msg = await ctx.reply(f"Downloading <{query}>...")
                stdout, stderr = await child.communicate()
            except Exception as e:
                await msg.edit(f"```{e}```")

            exitcode = child.returncode
            vidfile = f"{video_id}.{media_format}"
            deletemsg = await msg.delete()

            if exitcode == 0:
                try:
                    await ctx.reply(file=discord.File(f"temp/{vidfile}"))
                    deletemsg
                    await asyncio.sleep(14400)
                    await aiof.os.remove(f"temp/{vidfile}")
                except Exception as e:
                    await ctx.reply(f"```{e}``` http://{env.webdomain}/temp/{vidfile}")
                    deletemsg
            else:
                await msg.reply(f"Something went wrong. ```{exitcode}```")

                


def setup(bot: commands.Bot):
    bot.add_cog(ytdlcmd(bot))
