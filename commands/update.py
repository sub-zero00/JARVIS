import discord
from discord.ext import commands

#author: sub-zero
#bot çalışırkan extensionları güncellemek için

class adminkomut(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command(hidden= True)
    async def update(self, mesaj, value:str):
        dizin = "commands."

        try:
            self.bot.unload_extension(dizin+value)
            self.bot.load_extension(dizin+value)
            await mesaj.send(value + " dosyası yenilendi")

        except ImportError as e:
            print(e)

def setup(bot):
    bot.add_cog(adminkomut(bot))