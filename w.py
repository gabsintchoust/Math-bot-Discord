async def invite(ctx):
    permissions = discord.Permissions().all()
    oauth_url = discord.utils.oauth_url(client.user.id, permissions=permissions)
    await ctx.send(f"Voici le lien pour inviter le bot sur votre serveur: {oauth_url}")