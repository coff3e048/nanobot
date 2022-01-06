import yt_dlp
import os
import subprocess
import discord
import asyncio
from nextcord.ext import commands
from dotenv import load_dotenv
from env_var import env


class ytdlcmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ytdl")
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

        ytdlpath = "'.www/temp/%(id)s.%(ext)s'"
        usage = "[p]ytdl 'https://youtube.com/...'' video / audio (default: video)"

        if query == None:
            await ctx.reply(f"No YouTube URL found.\n```{usage}```")
        else:
            if convert == 'video':
                media_format = 'mp4'
                opts = f' --max-filesize 300M -f 18/5/36 --no-playlist --recode-video {media_format} --break-on-existing --no-exec -o {ytdlpath}'
            elif convert == 'audio':
                media_format = 'mp3'
                opts = f' --max-filesize 300M -f 18/5/36 --no-playlist -x --audio-format {media_format} --break-on-existing --no-exec -o {ytdlpath}'
            elif convert == 'audio-opus':
                media_format = 'opus'
                opts = f' --max-filesize 300M -f 18/5/36 --no-playlist -x --audio-format {media_format} --break-on-existing --no-exec -o {ytdlpath}'
            else:
                await ctx.reply(f"Invalid usage.\n```{usage}```")

            vidfile = f'{video_id}.{media_format}'
            firstmsg = await ctx.reply(f"Downloading <{query}>...")

        # And here lies the major problem.
            try:
                child = await asyncio.create_subprocess_shell(
                    f"yt-dlp {opts} {query}",
                    stderr=asyncio.subprocess.PIPE,
                    stdout=asyncio.subprocess.PIPE
                )
                stdout, stderr = await child.communicate()
            except Exception as e:
                await ctx.reply(f"```{e}```")

            if child.returncode == 0:
                try:
                    await ctx.reply(file=discord.File(f".www/temp/{vidfile}"))
                except:
                    await ctx.reply(f"<{query}> is too big to upload to Discord. If it's not here, it's probably too big for us too. \n\nhttp://{env.webdomain}/temp/{vidfile}")

                await firstmsg.delete()


def setup(bot: commands.Bot):
    bot.add_cog(ytdlcmd(bot))
