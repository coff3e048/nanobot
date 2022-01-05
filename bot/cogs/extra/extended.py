import aiohttp
import cowsay
import re
import discord
import base64
from nextcord.ext import commands


class Extended(commands.Cog):
    """Search YouTube for videos."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_msg = None
        self.session = aiohttp.ClientSession()


    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        self.last_msg = message


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


    @commands.group(name="say")
    async def say(self, ctx: commands.Context, saytype: str = "cow", *, text: str = "Hello world!"):
        try:
            await ctx.reply(f"```{cowsay.get_output_string(saytype,text)}```")
        except Exception as e:
            await ctx.reply(f"```{e}```")


    @commands.command(name="avatar", aliases=["pfp", "a"])
    async def get_avatar(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        avatarEmbed = discord.Embed(title=f"{member.name}'s avatar").set_image(url=member.avatar.url)
        try:
            await ctx.reply(embed=avatarEmbed)
        except:
            await ctx.author.send(embed=avatarEmbed)


def setup(bot: commands.Bot):
    bot.add_cog(Extended(bot))
