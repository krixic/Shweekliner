import discord
from discord import app_commands
from discord.ext import commands
import datetime

class weekly(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @app_commands.command(
    name = "weekly",
    description = "Send the weekly")

  async def weekly(
    self,
    interaction: discord.Interaction,
    name: str,
    author: str,
    id: str,
    stars: str):

    embed = discord.Embed(title="New Weekly ‼️", color=0x2c2f96)
    embed.add_field(name="Name", value=f"{name}")
    embed.add_field(name="Author", value=f"{author}")
    embed.add_field(name="ID", value=f"{id}")
    embed.add_field(name="Stars", value=f"{stars}")
    embed.timestamp = datetime.datetime.utcnow()

    await interaction.response.send_message(embed=embed)
    
async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(
    weekly(bot),
    guilds = [discord.Object(id = 944699617939968050)])