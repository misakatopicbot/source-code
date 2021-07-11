import discord
from discord.ext import commands
import smtplib
from email.mime.text import MIMEText

class Suggest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def suggest(self, ctx, *, content:str):
        server_name = str(ctx.guild.name)
        server_id = str(ctx.guild.id)
        author_name = str(ctx.author)
        author_id = str(ctx.author.id)
        message = MIMEText(content+"\nServer name: "+server_name+"\nServer ID: "+server_id+"\nAuthor: "+author_name+"\nAuthor ID: "+author_id, 'plain', 'utf-8')
        message['From'] = "from"
        message['To'] =  "to"
 
        subject = 'You got suggestion from Misaka Topic Bot "~suggest" command'
        message['Subject'] = subject
 
        smtpObj = smtplib.SMTP('smtp.server.com', port)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login('username', 'password')
        smtpObj.sendmail('from', 'to', message.as_string())
        smtpObj.quit()

        await ctx.send("Your suggestion has been sent to the owner!")

def setup(bot):
    bot.add_cog(Suggest(bot))
