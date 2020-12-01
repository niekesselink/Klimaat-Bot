import discord
import os

from datetime import datetime
from discord.ext import commands

class Events(commands.Cog):
    """General event handler for the bot."""

    def __init__(self, bot):
        """Initial function that runs when the class has been created."""
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Event that happens once the bot has started."""

        # But is running.
        print('Bot has started.')
        self.bot.uptime = datetime.utcnow()
        
def setup(bot):
    bot.add_cog(Events(bot))
