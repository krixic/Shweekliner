import discord
from discord import app_commands
from discord.ext import commands
from replit import db
from utils import generate_points_key, generate_weekly_key

class add(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @app_commands.command(
    name = "add",
    description = "Add points to users")

  async def add(
    self,
    interaction: discord.Interaction,
    user: discord.Member,
    amount: int):

    userid = str(user.id)
    all_database_keys = db.keys()
    points_key = generate_points_key(userid)
    weekly_key = generate_weekly_key(userid)

    if points_key in all_database_keys and weekly_key in all_database_keys:
      db[points_key] += amount
      db[weekly_key] += 1
    else:
      db[points_key] = amount
      db[weekly_key] = 1

    embed = discord.Embed(title="Add", description=f"{user}'s balance", color=0x00ff00)
    embed.add_field(name="Added Stars ⭐️", value=f"{amount}")
    embed.add_field(name="New Total", value=f"{db[points_key]}")
    embed.add_field(name="Amount of Weeklies Beaten", value=f"{db[weekly_key]}")

    await interaction.response.send_message(embed=embed)
    
async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(
    add(bot),
    guilds = [discord.Object(id = 944699617939968050)])