import discord
from discord.ext import commands

class Streaming(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def stream(self, ctx, platform, username):
            # Implement streaming notification logic
            await ctx.send(f'Streaming notification for {username} on {platform}')

            async def setup(bot):
                await bot.add_cog(Streaming(bot))
