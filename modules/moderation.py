import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def warn(self, ctx, member: discord.Member, *, reason):
            # Implement warn logic
            await ctx.send(f'{member.mention} has been warned for {reason}')

            @commands.command()
            async def kick(self, ctx, member: discord.Member, *, reason):
                # Implement kick logic
                await ctx.send(f'{member.mention} has been kicked for {reason}')

                @commands.command()
                async def ban(self, ctx, member: discord.Member, *, reason):
                    # Implement ban logic
                    await ctx.send(f'{member.mention} has been banned for {reason}')

                    async def setup(bot):
                        await bot.add_cog(Moderation(bot))
