import json
import discord
from discord.ext import commands, tasks
from discord.utils import get

# Defining Bot
intents = discord.Intents.all()
activity = discord.Game(name="the yogd hunting game")
bot = commands.Bot(command_prefix="", activity=activity, status=discord.Status.online, intents=intents, owner_id=487247155741065229)

# Removing default help command
bot.remove_command("help")

with open('config.json', 'r') as f:
    config = json.load(f)

# Fetching prefix
bot.command_prefix = config["prefix"]

@bot.event
async def on_ready():
    print("Bot connected to Discord!")

@bot.command(name="check")
async def check(ctx):
    await ctx.message.delete()
    member = bot.get_guild(906804682452779058).get_member(config["memberID"])
    name = member.name + "#" + member.discriminator
    channel = bot.get_guild(906804682452779058).get_channel(906804682452779062)
    if not config["name"] == name:
        with open('config.json', 'w') as f:
            config["name"] = name
            config["names"].append(name)
            json.dump(config, f, indent=4)
            embed = discord.Embed(title="He did it again!", description=f"New Name: {name}", color=discord.Color.red())
            await channel.send(content=f"@here", allowed_mentions=discord.AllowedMentions(everyone=True))
            await channel.send(embed=embed)

@tasks.loop(hours=1)
async def check():
    member = bot.get_guild(906804682452779058).get_member(config["memberID"])
    name = member.name + "#" + member.discriminator
    channel = bot.get_guild(906804682452779058).get_channel(906804682452779062)
    if not config["name"] == name:
        with open('config.json', 'w') as f:
            config["name"] = name
            config["names"].append(name)
            json.dump(config, f, indent=4)
            embed = discord.Embed(title="He did it again!", description=f"New Name: {name}", color=discord.Color.red())
            await channel.send(content=f"@here", allowed_mentions=discord.AllowedMentions(everyone=True))
            await channel.send(embed=embed)

bot.run(config["token"])