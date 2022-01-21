import discord
from nextcord.ext import commands


class admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kickmember(self, ctx: commands.Context, member: discord.Member = None, *, reason: str = "No given reason"):
        await member.kick(reason=reason)
        msg = f"{member.mention} (*{member.id}*) was kicked for `{reason}`"
        await ctx.reply(msg)

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def banmember(self, ctx: commands.Context, member: discord.Member = None, *, reason: str = "No given reason"):
        await member.ban(reason=reason)
        msg = f"{member.mention} (*{member.id}*) was banned for `{reason}`"
        await ctx.reply(msg)


def setup(bot: commands.Bot):
    bot.add_cog(admin(bot))