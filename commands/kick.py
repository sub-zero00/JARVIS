import discord
from discord.ext import commands

#author: sub-zero
#server üyesini kovmak için

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_version = bot.bot_version

    @commands.command()
    async def kick(self, mesaj, member : discord.Member, * , reason = None ):
        if str(member) == "sub-zero#4766":
            await mesaj.send("sen kimi kovuyon lan")
        else:
            try:
                await member.kick(reason=reason)
                await mesaj.send("hadi yallah")
            except:
                await mesaj.send("başaramadık abi")










def setup(bot):
    bot.add_cog(info(bot))