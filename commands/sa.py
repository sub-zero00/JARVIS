import discord
from discord.ext import commands

#author: sub-zero
#class yapısını görmek için -2

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_version = bot.bot_version

    @commands.command()
    async def sa(self, mesaj):
        await mesaj.send("as")






def setup(bot):
    bot.add_cog(info(bot))