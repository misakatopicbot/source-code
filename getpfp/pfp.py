import discord
from discord.ext import commands


class Getpfp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def getpfp(self, ctx, member:typing.Optional[discord.Member] = "own"):
        if member == "own":
            member = ctx.author
        mem_pfp = member.avatar_url
        embed = discord.Embed(
        title=f"There's pfp for {member}",
        color=discord.Color.blue()
        )
        embed.set_image(url=mem_pfp)
        await ctx.send(embed=embed)
    

def setup(bot):
    bot.add_cog(Getpfp(bot))
