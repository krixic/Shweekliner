import discord
from discord import app_commands
from discord.ext import commands
from replit import db
from utils import generate_points_key, generate_weekly_key

class balance(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @app_commands.command(
    name = "balance",
    description = "Get the balance")
  
  async def balance(
    self,
    interaction: discord.Interaction,
    user: discord.Member) -> None:

    userid = str(user.id)
    points_key = generate_points_key(userid)
    weekly_key = generate_weekly_key(userid)

    all_database_keys = db.keys()
    if not points_key in all_database_keys and not weekly_key in all_database_keys:
      db[points_key] = 0
      db[weekly_key] = 0
      
    embed = discord.Embed(title="Balance", description=f"{user}'s balance")
    embed.add_field(name="Stars ⭐️", value=f"{db[points_key]}")
    embed.add_field(name="Weeklies Beaten", value=f"{db[weekly_key]}")

    await interaction.response.send_message(embed=embed)
    
async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(
    balance(bot),
    guilds = [discord.Object(id = 944699617939968050)])