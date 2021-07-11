import discord
from discord.ext import commands


class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        await ctx.send("https://discord.com/api/oauth2/authorize?client_id=802840763049574411&permissions=2048&scope=bot")

def setup(bot):
    bot.add_cog(Invite(bot))
