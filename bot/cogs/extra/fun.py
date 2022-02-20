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

    @commands.command(name="choose", aliases=['pick'])
    async def choose(self, ctx, *, text: str = None):
        if text:
            await ctx.reply(random.choice(text.split()))
        else:
            await ctx.reply(f"You've given me nothing to chose between.")

    @commands.command(name="8ball", aliases=['8-ball', '8b', '8'])
    async def eightball(self, ctx):
        responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
                     "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
                     "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
                     "Yes.", "Yes – definitely.", "You may rely on it."]
        msg = await ctx.reply(':8ball: *Thinking*')
        choice = random.choice(responses)
        await asyncio.sleep(1)
        # i want to keep this cause its funny
        # await msg.edit(':8ball: '+"...".join(choice))
        await msg.edit(f':8ball: {choice}')

    @commands.command(name="ascii")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def ascii(self, ctx, *, text: str = "Hello World!"):
        textart = text2art(text, 'random')
        try:
            await ctx.reply(f"```{textart}```")
        except:
            data = io.BytesIO(textart)
            await ctx.reply(file=discord.File(data, f'ascii-{ctx.author.id}.txt'))

    @commands.command(name="battle")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def auto_battle(self, ctx, member: discord.Member = None):
        if member == None or member == ctx.author:
            await ctx.reply("Suicide is not an option!")
        elif member == self.bot.user:
            await ctx.reply("You can't beat the bot.")
        else:
            msg = await ctx.reply(embed=discord.Embed(
                title="A challenge has been called!",
                description=f"{ctx.author.mention} and {member.mention} are fighting to the death!"
            ))
            await asyncio.sleep(2)
            pnts = [0, 0]
            for x in range(6):
                user = [ctx.author.mention, member.mention]
                random.shuffle(user)
                moves = [
                    f'{user[0]} punched {user[1]} in the face!',
                    f'{user[0]} kicked {user[1]} in the legs!',
                    f'{user[0]} slapped {user[1]} in the face!',
                    f'{user[0]} shot {user[1]} with a BB gun!',
                    f'{user[0]} hit {user[1]} in the head with a toaster!',
                    f'{user[0]} makes a critical strike on {user[1]}!'
                ]
                if user[0] == ctx.author.mention:
                    pnts[0] += 1
                else:
                    pnts[1] += 1
                points_footer = f"{ctx.author}: {pnts[0]} points | {member}: {pnts[1]} points"
                await msg.edit(embed=discord.Embed(
                    description=f'{random.choice(moves)}\n'
                ).set_footer(text=points_footer))
                await asyncio.sleep(2)

            if user[0] == user[1]:
                embedmsg = discord.Embed(
                    description="It's a tie!").set_footer(text=points_footer)
            elif user[0] > user[1]:
                winner = ctx.author
                embedmsg = discord.Embed(
                    description=f"{winner.mention} wins!").set_footer(text=points_footer)
            elif user[0] < user[1]:
                winner = member
                embedmsg = discord.Embed(
                    description=f"{winner.mention} wins!").set_footer(text=points_footer)

            await msg.edit(embed=embedmsg)


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
