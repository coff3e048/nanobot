import discord
import aiohttp
from nextcord.ext import commands


class Bible(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    @commands.command(name="bible")
    async def animal_fact(self, ctx, book: str = "Genesis", text: str = "1:1-3", trans: str = "web"):
        URL = f"https://bible-api.com/{book}%20{text}?verse_numbers=true&translation={trans}"
        async with self.session.get(URL, headers={}) as response:
            if response.status == 200:
                data = await response.json()
                embed = discord.Embed(
                    title=data["reference"],
                    url=URL,
                    description=data["text"][:750]
                )
                embed.set_footer(text=f"Translation: {data['translation_name']} ({data['translation_id']})")
                msg = await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(
                    color=discord.Color.red(),
                    description=f'Likely not a real book / verse. Try again.\n\nCheck https://bible-api.com for more details.'
                )
                embed.set_footer(text=f'API Response status: {response.status}')
                await ctx.reply(embed=embed,
                delete_after=30)


def setup(bot: commands.Bot):
    bot.add_cog(Bible(bot))
