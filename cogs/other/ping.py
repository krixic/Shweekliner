import discord
from discord import app_commands
from discord.ext import commands

class ping(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @app_commands.command(
    name = "ping",
    description = "Current ping of the bot")
  
  async def ping(
    self,
    interaction: discord.Interaction) -> None:    
    await interaction.response.send_message(f"Pong! {round(self.bot.latency * 1000)}ms")
    
async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(
    ping(bot),
    guilds = [discord.Object(id = 823034655304581120)])