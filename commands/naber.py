import discord
from discord.ext import commands

#author: sub-zero
#class yapısını görmek için

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_version = bot.bot_version

    @commands.command()
    async def naber(self, mesaj):
        await mesaj.send("iyi sen")






def setup(bot):
    bot.add_cog(info(bot))