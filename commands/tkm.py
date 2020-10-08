import discord
from discord.ext import commands
from random import randint

#author: sub-zero
#eğlenceli bir oyun

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_version = bot.bot_version

    @commands.command()
    async def tkm(self, mesaj, value:str ):
        a = randint(1,3)
        if value == "tas" and a == 1:

            embed = discord.Embed(title="--------- Taş-Kağıt-Makas ---------", color=0xece000)
            embed.add_field(name="taş :new_moon: ", value="you", inline=True)
            embed.add_field(name="taş :new_moon:", value="me", inline=True)
            embed.add_field(name="--------- berabere ---------", value=".", inline=False)
            embed.set_footer(text="Author: Sub-zero")
            await mesaj.send(embed=embed)
            """
            await mesaj.send("taş")
            await mesaj.send("berabere")
            """
        elif value == "tas" and a == 2:

            embed = discord.Embed(title="--------- Taş-Kağıt-Makas ---------", color=0xece000)
            embed.add_field(name="taş :new_moon:", value="you", inline=True)
            embed.add_field(name="kağıt :page_with_curl: ", value="me", inline=True)
            embed.add_field(name="--------- ben kazandım ---------", value=".", inline=False)
            embed.set_footer(text="Author: Sub-zero")
            await mesaj.send(embed=embed)
            """
            await mesaj.send("kağıt")
            await mesaj.send("ben kazandım")
            """
        elif value == "tas" and a == 3:
            embed = discord.Embed(title="--------- Taş-Kağıt-Makas ---------", color=0xece000)
            embed.add_field(name="taş :new_moon:", value="you", inline=True)
            embed.add_field(name="makas :scissors:", value="me", inline=True)
            embed.add_field(name="--------- sen kazandın ---------", value=".", inline=False)
            embed.set_footer(text="Author: Sub-zero")
            await mesaj.send(embed=embed)
            """
            await mesaj.send("makas")
            await mesaj.send("sen kazandın")
            """
        elif value == "kagit" and a == 1:
            embed = discord.Embed(title="--------- Taş-Kağıt-Makas ---------", color=0xece000)
            embed.add_field(name="kağıt :page_with_curl:", value="you", inline=True)
            embed.add_field(name="taş :new_moon:", value="me", inline=True)
            embed.add_field(name="--------- sen kazandın ---------", value=".", inline=False)
            embed.set_footer(text="Author: Sub-zero")
            await mesaj.send(embed=embed)
            """
            await mesaj.send("taş")
            await mesaj.send("sen kazandın")
            """
        elif value == "kagit" and a == 2:
            embed = discord.Embed(title="--------- Taş-Kağıt-Makas ---------", color=0xece000)
            embed.add_field(name="kağıt :page_with_curl:", value="you", inline=True)
            embed.add_field(name="kağıt :page_with_curl:", value="me", inline=True)
            embed.add_field(name="--------- berabere ---------", value=".", inline=False)
            embed.set_footer(text="Author: Sub-zero")
            await mesaj.send(embed=embed)
            """
            await mesaj.send("kağıt")
            await mesaj.send("berabere")
            """
        elif value == "kagit" and a == 3:
            embed = discord.Embed(title="--------- Taş-Kağıt-Makas ---------", color=0xece000)
            embed.add_field(name="kağıt :page_with_curl:", value="you", inline=True)
            embed.add_field(name="makas :scissors:", value="me", inline=True)
            embed.add_field(name="--------- ben kazandım ---------", value=".", inline=False)
            embed.set_footer(text="Author: Sub-zero")
            await mesaj.send(embed=embed)
            """
            await mesaj.send("makas")
            await mesaj.send("ben kazandım")
            """
        elif value == "makas" and a == 1:
            embed = discord.Embed(title="--------- Taş-Kağıt-Makas ---------", color=0xece000)
            embed.add_field(name="makas :scissors:", value="you", inline=True)
            embed.add_field(name="taş :new_moon:", value="me", inline=True)
            embed.add_field(name="--------- ben kazandım ---------", value=".", inline=False)
            embed.set_footer(text="Author: Sub-zero")
            await mesaj.send(embed=embed)
            """
            await mesaj.send("taş")
            await mesaj.send("ben kazandım")
            """
        elif value == "makas" and a == 2:
            embed = discord.Embed(title="--------- Taş-Kağıt-Makas ---------", color=0xece000)
            embed.add_field(name="makas :scissors:", value="you", inline=True)
            embed.add_field(name="kağıt :page_with_curl:", value="me", inline=True)
            embed.add_field(name="--------- sen kazandın ---------", value=".", inline=False)
            embed.set_footer(text="Author: Sub-zero")
            await mesaj.send(embed=embed)
            """
            await mesaj.send("kağıt")
            await mesaj.send("sen kazandın")
            """
        elif value == "makas" and a == 3:
            embed = discord.Embed(title="--------- Taş-Kağıt-Makas ---------", color=0xece000)
            embed.add_field(name="makas :scissors:", value="you", inline=True)
            embed.add_field(name="makas :scissors:", value="me", inline=True)
            embed.add_field(name="--------- berabere ---------", value=".", inline=False)
            embed.set_footer(text="Author: Sub-zero")
            await mesaj.send(embed=embed)
            """
            await mesaj.send("makas")
            await mesaj.send("berabere")
            """
        else:
            await mesaj.send("ne salak adamsın taş-kağıt-makas oynamayı bilmiyon mu")








def setup(bot):
    bot.add_cog(info(bot))