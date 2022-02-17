import random
import asyncio
import os
import discord
import numpy.random
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
        if text:
            await ctx.reply(random.choice(text.split()))
        else:
            await ctx.reply(f"You've given me nothing to chose between.")

    @commands.command(name="8ball")
    async def eightball(self, ctx: commands.Context):
        responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
                     "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
                     "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
                     "Yes.", "Yes – definitely.", "You may rely on it."]
        msg = await ctx.reply(':8ball: *Thinking*')
        choice = random.choice(responses)
        await asyncio.sleep(1)
        # i want to keep this cause its really funny
        #await msg.edit(':8ball: '+"...".join(choice))
        await msg.edit(f':8ball: {choice}')

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

    @commands.command(name="battle")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def auto_battle(self, ctx: commands.Context, member: discord.Member = None):
        if not member or member == ctx.author:
            await ctx.reply("Suicide is not an option!")
        else:
            embed = discord.Embed(
                description=f"A challenge has been called!\n\n{ctx.author.mention} and {member.mention} are fighting to the death!"
            )
            msg = await ctx.reply(embed=embed)
            await asyncio.sleep(2)
            pnts_author = 0
            pnts_member = 0
            for x in range(5):
                user = [ctx.author.mention, member.mention]
                random.shuffle(user)
                moves = [
                    f'{user[0]} punched {user[1]} in the face!',
                    f'{user[0]} kicked {user[1]} in the legs!',
                    f'{user[0]} slapped {user[1]} in the face!',
                    f'{user[0]} shot {user[1]} with a BB gun!',
                    f'{user[0]} hit {user[1]} in the head with a toaster!'
                ]
                if user[0] == ctx.author.mention:
                    pnts_author = pnts_author + 1
                else:
                    pnts_member = pnts_member + 1
                await msg.edit(embed=discord.Embed(
                    description=f'{random.choice(moves)}\n'
                ).set_footer(text=f"{ctx.author}: {pnts_author} points | {member}: {pnts_member} points"))
                await asyncio.sleep(2)

            if pnts_author == pnts_member:
                await msg.edit(embed=discord.Embed(description="It's a tie!"))
            elif pnts_author > pnts_member:
                await msg.edit(embed=discord.Embed(description=f"{ctx.author.mention} wins!"))
            elif pnts_author < pnts_member:
                await msg.edit(embed=discord.Embed(description=f"{member.mention} wins!"))


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
