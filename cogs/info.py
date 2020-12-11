import discord

from discord.ext import commands

class Info(commands.Cog):
    """Information commands for the bot."""

    def __init__(self, bot):
        """Initial function that runs when the class has been created."""
        self.bot = bot

    @commands.command()
    async def opensource(self, ctx, name):
        """Informs that the bot is indeed open-source and post the link to the code."""

        await ctx.send(f'De bot is open-source! De code van de bot is hier terug te vinden; https://github.com/niekesselink/Klimaat-Bot')

def setup(bot):
    bot.add_cog(Info(bot))
