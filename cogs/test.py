import discord
import asyncio

class Test(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    #coinflip

    @commands.command(aliases=['flip', 'coin'])
    async def coinflip(self, ctx):
        try:
            coinsides = ['Heads', 'Tails']
            await ctx.send(f"^^ {ctx.author.name} flipped a coin and got {random.choice(coinsides)}! ^^")
        except Exception as e:
            print(e)
            await ctx.send("An Error has been logged.")

def setup(client):
    client.add_cog(Test(client))
