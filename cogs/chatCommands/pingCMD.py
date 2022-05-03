import nextcord
from nextcord.ext import commands


class PingCmd(commands.Cog):

    def __init__(self, bot):
        self.bot: nextcord.Client = bot

    @commands.command(name="ping")
    @commands.is_owner()
    async def ping(self, ctx: commands.Context):
        if ctx.author.id == self.bot.user.id:
            return
        await ctx.message.delete(delay=3)
        await ctx.channel.send(f"❗️My ping is: `{self.bot.latency*1000:.0f}ms`❗️", delete_after=3)

# A setup function is a necessary function inside a cog file
# This functions if used to load the: class PingCmd which will 
# load all of the events inside of it
def setup(bot):
    bot.add_cog(PingCmd(bot))

