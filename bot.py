import discord
from discord.ext import commands


bot = commands.Bot(
    command_prefix="~/", 
    activity=discord.Game(
        name="Bot Reddit community: r/MisakaTopicBot | Invite me use '~invite' command"
    )
)

bot.remove_command('help')

@bot.event
async def on_ready():
    print("bot is ready")
    bot.load_extension('getTopic.en')
    bot.load_extension('getTopic.cn')
    bot.load_extension('feedback.help')
    bot.load_extension('feedback.invite')
    bot.load_extension('feedback.suggest')
    bot.load_extension('getpfp.pfp')

bot.run("bot-token")
