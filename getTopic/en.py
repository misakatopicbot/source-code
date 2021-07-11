import discord
from discord.ext import commands
from urllib import request
from bs4 import BeautifulSoup

class EN(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def topic(self, ctx):
       topicWebsite = request.urlopen("https://www.conversationstarters.com/generator.php")  
       bs=BeautifulSoup(topicWebsite, "html.parser")
       topic = bs.find('div', id='random')
       await ctx.send(topic.text)

def setup(bot):
    bot.add_cog(EN(bot))
