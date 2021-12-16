import discord
from nextcord.ext import commands

import yt_dlp

class ytdl_cmd(commands.Cog):
  

    def __init__(self, bot):
        self.bot = bot

    def my_hook(d):
      if d['status'] == 'finished':
        print('Done downloading, now converting ...')

    @commands.command(name="ytdl")
    async def yt_dl(self, ctx, *, query: str = None, convert: str = "video"):
      if query == None:
        await ctx.reply("No YouTube URL found.")
      else:
        if convert == "video":
          ydl_opts = {
            'remux-video': 'webm'
            'noplaylist'
          }
        if convert == "audio":
          ydl_opts = {
            'audio-format':'mp3'
            'extract-audio'
            'noplaylist'
          }
        await ctx.reply("Attempting download")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
          try:
            ydl.download([query])
          except ERROR as e:
            await ctx.reply(f"{e}")
      
    
def setup(bot: commands.Bot):
  bot.add_cog(ytdl_cmd(bot))