import discord
from discord.ext import commands
from random import randint

with open('.gitignore', 'r') as file:
    token = file.read().strip()

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

async def invite(ctx):
    permissions = discord.Permissions().all()
    oauth_url = discord.utils.oauth_url(client.user.id, permissions=permissions)
    await ctx.send(f"Voici le lien pour inviter le bot sur votre serveur: {oauth_url}")

client.run(token)
