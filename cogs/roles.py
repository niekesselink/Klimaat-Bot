import asyncio
import discord

from discord.ext import commands

class Roles(commands.Cog):
    """Information commands for the bot."""

    def __init__(self, bot):
        """Initial function that runs when the class has been created."""
        self.bot = bot

    @commands.group()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def roles(self, ctx):
        """Commands for adding role reactions."""
        return

    @roles.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def addtoall(self, ctx, role_name):
        """Add a role to a member or to everyone if 'all' is given."""

        # Get role by name.
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if role is None:
            return await ctx.send('Role not found!')

        # Inform the progress is starting.
        await ctx.send(f'Starting to add the role `{role_name}` to everyone. This could take some time depending on amount of members due to Discord API rate limit.')

        # Let's loop through all the members and add the roles. There is a timeout of 3 seconds due to rate limit.
        for member in ctx.guild.members:
            await member.add_roles(role)
            await asyncio.sleep(0.5)

        # Done!
        await ctx.send('Done adding roles!')

def setup(bot):
    bot.add_cog(Info(bot))
