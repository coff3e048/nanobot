import discord
from nextcord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kickmember(self, ctx, member=None, *, reason: str = "No given reason"):
        try:
            await member.kick(reason=reason)
        except:
            member = ctx.guild.get_member(member)
            await member.kick(reason=reason)
        await ctx.reply(f"{member.mention} (*{member.id}*) was kicked for `{reason}`")

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def banmember(self, ctx, member=None, *, reason: str = "No given reason"):
        try:
            await member.ban(reason=reason)
        except:
            member = ctx.guild.get_member(member)
            await member.ban(reason=reason)
        await ctx.reply(f"{member.mention} (*{member.id}*) was banned for `{reason}`")

    @commands.command(name="unban")
    @commands.has_permissions(ban_members=True)
    async def unbanmember(self, ctx, member=None):
        try:
            await member.unban()
        except:
            member = ctx.guild.get_member(member)
            await member.unban()
        await ctx.reply(f"{member.mention} (*{member.id}*) was unbanned for `{reason}`")

    @commands.command(name="massban")
    @commands.has_permissions(administrator=True)
    async def mass_banmember(self, ctx, *, members=None):
        default_reason = f"Mass Ban by {ctx.author}"
        for member in members.split():
            try:
                await member.ban(reason=default_reason)
            except:
                member = ctx.guild.get_member(member)
                await member.ban(reason=default_reason)
        await ctx.reply(f"{members} were mass-banned.")


def setup(bot: commands.Bot):
    bot.add_cog(Admin(bot))
