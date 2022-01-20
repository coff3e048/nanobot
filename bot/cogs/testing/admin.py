import discord
from nextcord.ext import commands


class admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def adminreply(punish, member, reason):
        msg = f"{member.mention} (**{member.userid}**)"
        _withreason = f"for `{reason}`"
        if punish == "kick" or "ban":
            if reason != None:
                msg = f"{msg} got {punish}ed {_withreason}"
            else
                msg = f"{msg} got {punish}ed"
        return msg


    @commands.command(name="kick")
    async def kickmember(self, ctx: commands.Context, member: discord.Member = None, *, reason: str):
        await member.kick(reason=reason)
        await ctx.reply(adminreply("kick", member, reason)
        

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def banmember(self, ctx: commands.Context, member: discord.Member = None, *, reason: str):
        await member.ban(reason=reason)
        await ctx.reply(adminreply("ban", member, reason)


    @commands.command(name="masskick")
    async def mass_kickmember(self, ctx: commands.Context, *, members: discord.Member = None):
        for members in members:
            await member.ban(reason=reason)
        await ctx.reply()



def setup(bot: commands.Bot):
    bot.add_cog(admin(bot))
