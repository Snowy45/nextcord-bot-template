import nextcord
from nextcord.ext import commands


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Creating an event listener and listening
    # for incoming command errors in order to handle them
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        # Checking if the error is a Command Cooldown error
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.channel.send(f"Command is on cooldown, try again in {error.retry_after:.1f}s", delete_after=2)
        # Checking if the error is a Missing Permissions error
        elif isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(f"Insufficient permissions, permission needed: {error.missing_permissions}", delete_after= 2)
        # Checking if the error is a Not Owner error
        elif isinstance(error, commands.NotOwner):
            await ctx.channel.send(f"Insufficient permissions: you must be owner in order to use this command", delete_after= 2)

def setup(bot):
    bot.add_cog(ErrorHandler(bot))
