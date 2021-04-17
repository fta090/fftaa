import discord
from discord.ext import commands
import random

class cekilis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
       
    @commands.command(bot=False)
    async def cekilis(self, ctx):
       await ctx.send(random.choice(self.bot.guilds[0].members))



def setup(bot):
    bot.add_cog(cekilis(bot))