import discord
from discord.ext import commands
from random import randint

#author: sub-zero
#basit random bir değer

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_version = bot.bot_version

    @commands.command()
    async def yt(self, mesaj,):
        a = randint(1,2)
        if a == 1:
            await mesaj.send("Tura")
        else:
            await mesaj.send("Yazı")



def setup(bot):
    bot.add_cog(info(bot))