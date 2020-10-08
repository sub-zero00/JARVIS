import discord
from discord.ext.commands import Bot
from discord.ext import commands

#author: sub-zero
#J.A.R.V.I.S.

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=">",pm_help= None, description="bot")
        self.bot_version = "1.0.0"
        self.bot_name ="Jarvis"
        self.load_extension("commands.info")
        self.load_extension("commands.update")
        self.load_extension("commands.speech")
        self.load_extension("commands.kick")
        self.load_extension("commands.sa")
        self.load_extension("commands.cuma")
        self.load_extension("commands.naber")
        self.load_extension("commands.tkm")
        self.load_extension("commands.yt")

    async def on_ready(self):
        print("merhaba ben jarvis")

    async def on_command_error(self, context, exception):
        if isinstance(exception , discord.ext.commands.errors.CommandNotFound):
            await context.send("ne diyon amk ")






bot = Bot()
token = "NzM0MDk1MTA2ODkzNjc2NjE1.XxMtWA.dnAm1Vzv3CEKJilO7Zh366_X_5w"
bot.run(token)



