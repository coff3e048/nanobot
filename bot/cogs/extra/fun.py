import random
import asyncio
import os
import discord
from nextcord.ext import commands
from art import text2art


class Fun(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="roll")
    async def roll(self, ctx, first: int = 1, second: int = 100):
        await ctx.reply(f"{random.randint(first,second)} *({first} - **{second}**)*")

    @commands.command(name="choose")
    async def choose(self, ctx: commands.Context, *, text: str = None):
        if text is not None:
            await ctx.reply(random.choice(text.split()))
        else:
            await ctx.reply(f"You've given me nothing to chose between.")

    @commands.command(name="8ball")
    async def eightball(self, ctx: commands.Context):
        responses = [
            "It is certain",
            "Outlook good",
            "You may rely on it",
            "Ask again later",
            "Concentrate and ask again",
            "Reply hazy, try again",
            "My reply is no",
            "My sources say no"
        ]
        msg = await ctx.reply(':8ball: *Thinking...*')
        await asyncio.sleep(1)
        await msg.edit(f':8ball: {random.choice(responses)}')

    @commands.command(name="ascii")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def ascii(self, ctx: commands.Context, *, text: str = "Hello World!"):
        textart = text2art(text, 'random')
        file = f'ascii-{ctx.author.id}.txt'
        try:
            await ctx.reply(f"```{textart}```")
        except:
            data = io.BytesIO(textart)
            await ctx.reply(file=discord.File(data, file))

    @commands.command(name="duel", alias=["standoff"])
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def duel(self, ctx, member1: discord.Member = None):
        # This command is still useless. Fix it later
        msgembed_kys = discord.Embed(
            description="You shot yourself. Good job.",
            colour=discord.Colour.red()
        )

        msgembed_ = discord.Embed(
            description=f"**{ctx.author.mention}** challenged **{member1.mention}** to a duel!",
        )
        msgembed_.set_footer(
            text="Be the first to click 💥 to win!"
        )

        thedude = '🤠'
        leftgun = '<a:GunShake_l:921999253335846922>'
        rightgun = '<a:GunShake_r:921998646885634068>'
        alotof_spaces = "        "

        if member1 is not None:
            msg = await ctx.reply(f'{thedude}{rightgun} {alotof_spaces} {leftgun}{thedude}', embed=msgembed_)
            await asyncio.sleep(random.randint(3, 6))
            await msg.add_reaction('💥')

            def check(reaction, user): return user == ctx.author or member1 and str(
                reaction.emoji) in "💥"

            for reactor in msg.reactions:
                reactors = await bot.wait_for("reaction_add", check=check, timeout=10)
                for member in reactors:
                    if ctx.author in member:
                        await ctx.reply(ctx.author.mention)
                        break
                    elif member1 in member:
                        await ctx.reply(member1.mention)
                        break
        else:
            msg = await ctx.reply(f'{thedude}{leftgun}')
            await asyncio.sleep(2)
            msg_e1 = await msg.edit('💥')
            await asyncio.sleep(3)
            await msg_e1.edit("💥 \n", embed=msgembed_kys)


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
