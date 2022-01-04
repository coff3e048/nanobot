import random
import asyncio
import os
import discord
from assets.py.insultfile import insult_list
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
        if text == None:
            await ctx.reply(f"You've given me nothing to chose between.")
        else:
            await ctx.reply(random.choice(text.split()))

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
        # the way this works is insanely bad, dont keep this PLEASE.
        textart = text2art(text, 'random')
        file = f'ascii-{ctx.author.id}.txt'
        if len(textart) > 1000:
            if os.path.exists(file):
                os.remove(file)
                pass
            else:
                f = open(file, 'x')
                f.write(str(textart))
                f.close()

                fr = open(file, 'r')
                await ctx.reply(file=discord.File(file))
                f.close()
                fr.close()
                os.remove(file)
        else:
            await ctx.reply(f"```{textart}```")

    @commands.command(name="insult")
    async def insult(self, ctx, member: discord.Member = None):
        insults = insult_list.list
        if member != None:
            await ctx.reply(f"{member.mention} {random.choice(insults)}")
        else:
            await ctx.reply(f"{ctx.author.mention} {random.choice(insults)}")

    @commands.command(name="duel", alias=["standoff"])
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def duel(self, ctx, member1: discord.Member = None):
        msgembed_kys = discord.Embed(
            description="You shot yourself. Good job.",
            colour=discord.Colour.red()
        )

        msgembed_ = discord.Embed(
            description=f"**{ctx.author}** challenged **{member1}** to a duel!",
        )
        msgembed_.set_footer(
            text="Be the first to click 💥 to win!"
        )

        thedude = '🤠'
        leftgun = '<a:GunShake_l:921999253335846922>'
        rightgun = '<a:GunShake_r:921998646885634068>'
        alotof_spaces = "        "

        if member1 != None:
            msg = await ctx.reply(f'{thedude}{rightgun} {alotof_spaces} {leftgun}{thedude}', embed=msgembed_)
            await asyncio.sleep(random.randint(3, 8))
            await msg.add_reaction('💥')
            cache_msg = discord.utils.get(msg.guild.members, id=msg.id)

        else:
            msg = await ctx.reply(f'{thedude}{leftgun}')
            await asyncio.sleep(2)
            msg_e1 = await msg.edit('💥')
            await asyncio.sleep(3)
            await msg_e1.edit("💥 \n", embed=msgembed_kys)


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
