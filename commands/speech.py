import discord
from discord.ext import commands

#author: sub-zero
#komuttan sonrakı str değerini almak için

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_version = bot.bot_version


    @commands.command()
    async def repeat(self, mesaj, value:str ):
        await mesaj.send(value)





def setup(bot):
    bot.add_cog(info(bot))