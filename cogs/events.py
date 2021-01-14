import discord

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
        self.bot.uptime = datetime.utcnow()
        print('Bot has started.')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Event that happens once a member joins the guild the bot is in."""

        # Send welcome message
        #await self.send_welcome(self, member)

        # Add the 'Lid' role in case it's the national server.
        if member.guild.id == 536211241589276698:
            role = member.guild.get_role(799057755579088908)
            await member.add_roles(role)

    @commands.command()
    async def testwelcome(self, ctx):
        """Command to send the welcome message to the initiator, for testing purposes only."""
        await self.send_welcome(ctx.author)

    async def send_welcome(self, member):
        """Function that sends a welcome message in direct message."""
        await member.send(f"Hallo en welkom in de **Klimaatmars 2021** organising Discord server!\n\n"
            "In deze Discord server vindt alle organisatie plaats om deze klimaatmars mogelijk te maken in zoveel mogelijk steden. Bovenaan de lijst van alle kanalen staan eerst de algemene kanalen; in <#773544889350094848> worden nieuwsberichten geplaatst, in <#773545849187467265> kan je zelf algemene informatie delen of kan je <TO BE MADE> checken om te zien hoe bepaalde functionaliteiten werken in Discord. Iets verder in de lijst staan alle steden gesorteerd op alfabetische volgorde waar andere mensen al actief bezig zijn met organiseren.\n\n"
            "Wij zouden het leuk vinden als je in het kanaal <#773544933831344219> jezelf introduceert, je kan hier bijvoorbeeld zeggen waar vandaan komt en wat je achtergrond is. Vervolgens kan je jouw stad opzoeken in de lijst van de kanalen en daar aansluiten met de rest. Mocht jouw stad nog niet in de lijst staan of als je andere vragen hebt kan je deze stellen in het <#773549382582272011> kanaal.\n\n"
            "*(Let op, dit is een automatisch gestuurd bericht via een bot die mensen verwelkomt op de server. Reacties op dit bericht wordt niet gelezen.)*")

def setup(bot):
    bot.add_cog(Events(bot))
