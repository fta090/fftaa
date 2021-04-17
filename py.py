import discord
from discord.ext import commands
from utils import *
import platform

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="*", pm_help=None, description="Python", intents=intents)
        self.bot_version = "1.0.0"
        self.bot_name = "Python"
        self.author = "FTA"
        self.getDeviceOs = platform.system()
       
        self.load_extension("cogs.info")
        self.load_extension("cogs.çekiliş")
        self.load_extension("cogs.yazankazanır")
    async def on_ready(self):
        print("Bot Başladı")
        print("BOT: {}".format(self.user.name))
        print("BOT İD: {}".format(self.user.id))
       

    async def on_command_error(self, context, exception):
        if isinstance(exception, discord.ext.commands.errors.CommandNotFound):
            await context.send("`Böyle Bir komut Bulamadım.`" .format(context))






bot = Bot()       
bot.run(TOKEN)



