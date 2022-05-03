import nextcord, json, os
from nextcord.ext import commands


# Getting the bots configurations from the configurations.json file
# You can add your own config data and extract it like in here
with open('configurations.json', 'r') as config:
    data=config.read()
    obj = json.loads(data)
    token = str(obj["token"])
    prefix = str(obj["prefix"])
    ownerID = int(obj["owner_id"])


intents = nextcord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=prefix, intents = intents)


# On_Ready event is called once the bot is ready to run
# In the ready event we set the bot status and print a debug message to our console 
# so we know it's ready to function
@bot.event
async def on_ready():
    print(f"Logging as {bot.user}")
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name=f"{prefix}help"))


# Loading cog extensions for the bot
# This loops thru the cogs folder and searches for
# files and files inside directories and then loads them
for fileOrFolder in os.listdir("./cogs"):
    if fileOrFolder.endswith(".py"):
        bot.load_extension("cogs." + fileOrFolder[:-3])
    else:
        for f in os.listdir("./cogs/" + fileOrFolder):
            if f.endswith(".py"):
                bot.load_extension(f"cogs.{fileOrFolder}.{f[:-3]}")


bot.run(token)