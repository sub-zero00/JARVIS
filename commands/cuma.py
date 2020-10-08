import discord
from discord.ext import commands

#author: sub-zero
#mübarek günler içim

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_version = bot.bot_version

    @commands.command()
    async def cuma(self, mesaj):
        await mesaj.send("Bizleri nimetlerine şükreden, takdirine rıza gösteren, belâ ve musibetlere sabreden, korktuklarından emin, umduklarına nâil olan bahtiyar kullarından eyle Allah’ım! Amin. Cumanız mübarek olsun.")








def setup(bot):
    bot.add_cog(info(bot))