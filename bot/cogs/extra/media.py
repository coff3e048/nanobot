import yt_dlp
import os
import subprocess
import discord
import asyncio
import re
import aiohttp
import aiofiles.os
from nextcord.ext import commands
from env_var import env


class mediastuff(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    async def _youtube_results(self, query: str):
        try:
            headers = {"user-agent": "nanobot/3.0"}
            async with self.session.get(
                "https://www.youtube.com/results", params={"search_query": query}, headers=headers
            ) as r:
                result = await r.text()
            yt_find = re.findall(r"{\"videoId\":\"(.{11})", result)
            url_list = []
            for track in yt_find:
                url = f"https://www.youtube.com/watch?v={track}"
                if url not in url_list:
                    url_list.append(url)
        except Exception as e:
            url_list = [f"Something went terribly wrong! [{e}]"]
        return url_list

    @commands.command(name="youtube", alias=["yt"])
    async def youtube(self, ctx, *, query: str):
        """Search on Youtube."""
        result = await self._youtube_results(query)
        if result:
            await ctx.reply(result[0])
        else:
            await ctx.reply("Nothing found. Try again later.")

    @commands.command(name="ytdl", alias=["youtubedl", "ydl"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def ytdl(self, ctx, query: str = None, convert: str = "video"):

        # Example video(s): http://www.youtube.com/watch?v=BaW_jenozKc
        #                   http://www.youtube.com/watch?v=jNQXAC9IVRw
        #                   https://youtu.be/khK_afMwAdA

        dlpath = "'temp/%(id)s.%(ext)s'"
        usage = f"{env.prefix}ytdl 'https://youtube.com/...' video / audio (default: video)"
        if not query:
            await ctx.reply(f"No YouTube URL found.\n```{usage}```")
        else:
            # User download format options, 'video' is the default.
            # Video formats:
            video_cv = ['video', 'webm']
            audio_cv = ['audio', 'opus']
            if convert == video_cv[0] or convert == 'mp4':
                media_format = 'mp4'
                opts = f'--recode-video {media_format}'
            elif convert in video_cv:
                media_format = convert
                opts = f'--recode-video {media_format}'
            # Audio formats:
            elif convert == audio_cv[0] or convert == 'mp3':
                media_format = 'mp3'
                opts = f'-x --audio-format {media_format}'
            elif convert in audio_cv:
                media_format = convert
                opts = f'-x --audio-format {media_format}'
            else:
                await ctx.reply(f"Invalid usage.\n```{usage}```")

            msg = await ctx.reply(f"Downloading <{query}>...")
            if not os.path.exists('temp'):
                os.mkdir('temp')

            # Extract video info for the ID.
            with yt_dlp.YoutubeDL() as ydl:
                info_dict = ydl.extract_info(query, download=False)
                video_id = info_dict.get("id", None)
            # Run yt-dlp to download the video & convert if needed
            # a pretty unsafe way of doing it, but yt_dlp doesn't support asyncio (and i also dont know async multiprocessing)
            try:
                subprocesspipe = asyncio.subprocess.PIPE
                child = await asyncio.create_subprocess_shell(
                    f"python3 -m yt_dlp --max-filesize 350M -f 22/18/5/36 --no-playlist {opts} --break-on-existing --no-exec -o {dlpath} {query}",
                    stderr=subprocesspipe,
                    stdout=subprocesspipe
                )
                stdout, stderr = await child.communicate()
            except Exception as e:
                await msg.edit(f"```{e}```")
            # Grab the exit code to know if yt-dlp succeeded or not
            exitcode = child.returncode
            vidfile = f"{video_id}.{media_format}"
            tmplocation = f"temp/{vidfile}"
            await msg.delete()          # Delete original download msg
            # If yt-dlp ran successfully and the file exists, upload it.
            try:
                if exitcode == 0 and os.path.exists(tmplocation):
                    await ctx.reply(file=discord.File(tmplocation))
                    await asyncio.sleep(14400)
                    await aiofiles.os.remove(tmplocation)
            except:
                await msg.reply(f"Something went wrong. The video download likely failed and no file was found to upload. ```{exitcode}```")
            else:
                await msg.reply(f"Something has gone abnormally wrong, and I don't know the error.")
            # remove the file after a certain amount of time (in this case, 14400 seconds is 4 hours)


def setup(bot: commands.Bot):
    bot.add_cog(mediastuff(bot))
