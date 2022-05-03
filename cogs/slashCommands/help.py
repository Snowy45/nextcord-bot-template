import nextcord, json
from nextcord.ext import commands



class Help(commands.Cog):
    def __init__(self, bot):
        self.bot: nextcord.Client = bot

    # Creating the slash command
    # In order to test Slash Commands right away you will need to add your test server ID,
    # add guild_ids and enter your guild id inside of it(This can only take 1 id at a time)
    @nextcord.slash_command(name="help", description="Shows you a list of all of the bot's commands")
    async def help(self, interaction: nextcord.Interaction):

        # Creating the help embed
        embed = nextcord.Embed(title="Commands List", color=nextcord.Colour.random())
        
        with open("help.json", 'r') as helpFile:
            data = helpFile.read()
            obj = json.loads(data)
            commands = obj["commands"]

        for command in commands:
            # Getting the commands description from the json file
            # If you want to add more fields to your command data such as necessary permissions 
            # you can do that and then load that data
            description: str = commands[command]["description"]

            # Adding a new field to the help embed with the command's name and description
            embed.add_field(name=f"`{command}`",value=description,inline=True)
        
        # Sending the help embed
        await interaction.response.send_message(embed=embed, ephemeral=True)


# A setup function is a necessary function inside a cog file
# This functions if used to load the: class Help which will 
# load all of the events inside of it
def setup(bot):
    bot.add_cog(Help(bot))
