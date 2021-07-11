import discord
from discord.ext import commands
from urllib import request, parse
import json, http.client, random, hashlib
from bs4 import BeautifulSoup

class BaiduTranslate:
    def __init__(self,fromLang,toLang):
        self.url = "/api/trans/vip/translate"
        self.appid="20151113000005349"
        self.secretKey = 'osubCEzlGjzvw8qdQc41'
        self.fromLang = fromLang
        self.toLang = toLang
        self.salt = random.randint(32768, 65536)
 
    def BdTrans(self,text):
        sign = self.appid + text + str(self.salt) + self.secretKey
        md = hashlib.md5()
        md.update(sign.encode(encoding='utf-8'))
        sign = md.hexdigest()
        myurl = self.url + \
            '?appid=' + self.appid + \
            '&q=' + parse.quote(text) + \
            '&from=' + self.fromLang + \
            '&to=' + self.toLang + \
            '&salt=' + str(self.salt) + \
            '&sign=' + sign
        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)
            response = httpClient.getresponse()
            html = response.read().decode('utf-8')
            html = json.loads(html)
            dst = html["trans_result"][0]["dst"]
            return True , dst
        except Exception as e:
            return False , e

class CN(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def huati(self, ctx):
        topicWebsite = request.urlopen("https://www.conversationstarters.com/generator.php")  
        bs=BeautifulSoup(topicWebsite, "html.parser")
        topic = bs.find('div', id='random')
        BaiduTranslate_test = BaiduTranslate('en','zh')
        Results = BaiduTranslate_test.BdTrans(topic.text)
        def fetch_data(url):
            req = request.Request(url)
            with request.urlopen(req) as f:
                return json.loads(f.read().decode('utf-8'))
        URL = 'https://raw.githubusercontent.com/misakatopicbot/Question-repo/master/topics.json'
        data = fetch_data(URL)
        topics = dict(data)
        n = random.randint(0, len(topics['topic_cn'])-1)
        if Results[0] == False:
            await ctx.send(topics['topic_cn'][n])
        else:
            await ctx.send(Results[1])

def setup(bot):
    bot.add_cog(CN(bot))
