import discord
from nextcord.ext import commands
from aiohttp import request


class httpTest(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    @command.commands(name="animalfact")
    async def animal_fact(self, ctx: commands.Context):
        URL = "https://some-random-api.ml/animal/"
        
        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data["fact"])
            else:
                await ctx.send(f"API returned a {response.status} status")

def setup(bot: commands.Bot):
    bot.add_cog(httpTest(bot))
