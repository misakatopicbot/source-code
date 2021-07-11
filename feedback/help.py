import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="Help menu", description="You can get help for Misaka Topic Bot", color=0xff0000)
        embed.add_field(name="~help", value="This Help menu", inline=True)
        embed.add_field(name="~topic", value="Get topic in English", inline=True)
        embed.add_field(name="~huati", value="Get topic in Chinese", inline=True)
        embed.add_field(name="~suggest [content]", value="Give owner your suggestion", inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
