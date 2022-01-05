import yt_dlp
import os
import subprocess
import asyncio
import discord
from nextcord.ext import commands
from dotenv import load_dotenv
from os import getenv
from env_var import env

class ytdlcmd(commands.Cog):
  
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(name="ytdl")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def yt_dl(self, ctx, query: str = None, convert: str = "video"):

    # Example video(s): http://www.youtube.com/watch?v=BaW_jenozKc
    #                   http://www.youtube.com/watch?v=jNQXAC9IVRw
    #                   https://www.youtube.com/watch?v=ywgeloPNmxk
    #                   https://youtu.be/khK_afMwAdA

    # Btw, this script is incredibly garbage and doesn't work very well. When a user tries to use [p]ytdl, the whole bot will stop and wait until the download / upload is finished.
    
      async with yt_dlp.YoutubeDL() as ydl:
          info_dict = ydl.extract_info(query, download=False)
          video_id = info_dict.get("id", None)
              
      dlpath = "'.temp/%(id)s.%(ext)s'"
      usage = "[p]ytdl 'https://youtube.com/...'' video / audio (default: video)" 
      
      if query == None:
          await ctx.reply(f"No YouTube URL found.\n```{usage}```")
      else:
          if convert == 'video':
              media_format = 'webm'
              opts = f'--recode-video {media_format}'
          elif convert == 'audio':
              media_format = 'ogg'
              opts = f'-x --audio-format {media_format}'
          elif convert == 'audio-opus':
              media_format = 'opus'
              opts = f'-x --audio-format {media_format}'
          else:
              await ctx.reply(f"Invalid usage.\n```{usage}```")
            
          vidfile = f'{video_id}.{media_format}'
          firstmsg = await ctx.reply(f"Downloading <{query}>...")

	# And here lies the major problem. 
  # https://fredrikaverpil.github.io/2017/06/20/async-and-await-with-subprocesses/
  
          try:
              child = await subprocess.Popen(
                f"./bin/yt-dlp --max-filesize 300M -f 18/5/36 --no-playlist {opts} --break-on-existing --no-exec -o {dlpath} {query}",
                shell=True
                )
              exitCode = child.communicate()[0]
              rc = child.returncode
          except Exception as e:
              await firstmsg.edit(f"```{e}```")

          if rc == 0:
              try:
                  await ctx.reply(file=discord.File(f".temp/{vidfile}"))
              except:
                  await ctx.reply(
                    f"<{query}> is too big to upload to Discord. \n\nhttp://{webdomain}/temp/{vidfile}"
                    )

              await firstmsg.delete()
          else:
              await ctx.reply(f"Download failed. Try again or use a different source.")

    
    
def setup(bot: commands.Bot):
    bot.add_cog(ytdlcmd(bot))
