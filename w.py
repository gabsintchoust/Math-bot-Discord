import nextcord
from nextcord.ext import commands


class HelpCommand(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @nextcord.slash_command(
        name = "randomaster", 
        description = "random 0 easy to hard infinite 1/(2^(points+1))"
        )

    async def help(self,
        interaction: nextcord.Interaction
    ) -> None:
        await interaction.response.send_message(content=f"Hello {interaction.user.mention}!")

def setup(bot: commands.Bot) -> None:
    bot.add_cog(
        HelpCommand(bot)
    )