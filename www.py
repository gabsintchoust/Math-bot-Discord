import discord
from discord.ext import commands
from random import randint
from ./ww.gitignore

client = commands.Bot(command_prefix='!', description="by/par gabsintchoust")  

def randeum():
    points = 0
    continuer = 50
    tentative = 1
    result = ""
    while tentative != 0:
        tentative = randint(0, 1)
        points += 1
        continuer /= 2
        result = f"{points} points avec {continuer}% d'avoir eu ce résultat et de s'arrêter juste après"
    return result

@client.command(description="Renvoie un résultat aléatoire")
async def randomaster(ctx):  
    result = randeum()
    await ctx.send(result)

client.add_command(randomaster)

client.run(token)
