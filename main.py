import os
import discord
from discord.ext import commands
from webserver import keep_alive

class Shweekliner(commands.Bot):
  
  def __init__(self):
    super().__init__(
      command_prefix ='w!',
      intents = discord.Intents.all(),
      application_id = 1057817779950075924)

    self.initial_extensions = [
      "cogs.other.ping",
      "cogs.points.balance",
      "cogs.points.add",
      "cogs.points.remove",
      "cogs.points.leaderboard",
      "cogs.points.weekly",
    ]

  async def setup_hook(self):
    for ext in self.initial_extensions:
      await self.load_extension(ext)
      
    await bot.tree.sync(guild = discord.Object(id = 944699617939968050))
    
  async def on_ready(self):
    print(f'{self.user} has connected to Discord!')

bot = Shweekliner()
keep_alive()
TOKEN = os.environ.get("TOKEN")
bot.run(TOKEN)