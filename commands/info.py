import discord
from discord.ext import commands

#Author: sub-zero
#komutları gösteren embed dosyası

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_version = bot.bot_version

    @commands.command()
    async def bilgi(self, mesaj):
        embed = discord.Embed(title="KODLAR", color=0x2ee9fe)
        embed.set_thumbnail(url="https://ih1.redbubble.net/image.309418928.2932/flat,1000x1000,075,f.u2.jpg")
        embed.add_field(name="-kick-", value="bahsedilen kişiyi sunucudan atar", inline=False)
        embed.add_field(name="-cuma mesajı-", value="mübarek günler için", inline=False)
        embed.add_field(name="-repeat-", value="tekrar", inline=False)
        embed.add_field(name="-sa-", value="as", inline=False)
        embed.add_field(name="-bilgi-", value="bu mesajı gönderir", inline=False)
        embed.add_field(name="-update-", value="advanced", inline=False)
        embed.add_field(name="-naber-", value="sohbet", inline=False)
        embed.add_field(name="-tkm-", value="taş-kağıt-makas", inline=False)
        embed.add_field(name="-yt-", value="yazı-tura", inline=False)
        embed.set_footer(text="Author: Sub-zero")
        await mesaj.send(embed=embed)





def setup(bot):
    bot.add_cog(info(bot))