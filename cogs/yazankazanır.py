import discord
import random
from discord.ext import commands

@client.command(aliases=["gay-test"])
async def howgay(ctx, kullanici: discord.User = None):
    if not kullanici: kullanici = ctx.author

    embed = discord.Embed()
    embed.title = "gay r8 machine"
    embed.description = f"{'You are' if kullanici == ctx.author else f'{kullanici.name} is'} {random.randint(1,100)}% gay :gay_pride_flag:"
    embed.color = discord.Colour.random()
    await ctx.send(embed=embed)