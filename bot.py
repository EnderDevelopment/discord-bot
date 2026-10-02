import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

class NexarisBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix='!', intents=intents)
        self.db = Database()
        self.load_modules()

        def load_modules(self):
            for filename in os.listdir('./modules'):
                if filename.endswith('.py'):
                    self.load_extension(f'modules.{filename[:-3]}')

                    async def on_ready(self):
                        print(f'Logged in as {self.user}')

                        bot = NexarisBot()
                        bot.run(os.getenv('DISCORD_TOKEN'))
