import discord
from discord.ext import commands

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_version = bot.bot_version
        self.bot_name = bot.bot_name
        self.author = bot.author
        self.getDeviceOs = bot.getDeviceOs
       
    @commands.command()
    async def bilgi(self, mesaj):
        embed=discord.Embed(title="Sar-9 BİLGİ", color=0x00eeff)
        embed.add_field(name="Versiyon", value=fh, inline=True)
        embed.add_field(name="Yapımcı", value=self.author, inline=True)
        embed.add_field(name="Kütüphane", value="Discord.py", inline=True)
        embed.set_footer(text="Sar-9, Sarsılmaz DP Rampage Markasıdır...")
        await mesaj.send(embed=embed)




def setup(bot):
    bot.add_cog(info(bot))