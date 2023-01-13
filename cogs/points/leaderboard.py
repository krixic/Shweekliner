import discord
from discord import app_commands
from discord.app_commands import Choice
from discord.ext import commands
from replit import db

class leaderboard(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @app_commands.command(
    name = "leaderboard",
    description = "Show the leaderboard"
  )

  @app_commands.describe(
    choices = "Type of leaderboard"  
  )

  @app_commands.choices(choices = [
    Choice(name = "Stars ⭐️", value = "Stars ⭐️"),
    Choice(name = "Weeklies Beaten", value = "Weeklies")
  ])
  
  async def leaderboard(
    self,
    interaction: discord.Interaction,
    choices: app_commands.Choice[str]):

    points_array = []
    weekly_array = []

    all_database_keys = db.keys()

    all_database_keys_starting_with_points = db.prefix("points")
    all_database_keys_starting_with_weekly = db.prefix("weekly")
      
    for database_key in all_database_keys_starting_with_points:
      id = self.bot.get_user(int(database_key[7:]))
      points_array.append({"id": id, "points": db[database_key]})
    for database_key in all_database_keys_starting_with_weekly:
      id = self.bot.get_user(int(database_key[7:]))
      weekly_array.append({"id": id, "points": db[database_key]})

    sorted_points_array = sorted(points_array, key=lambda d: d['points']) 
    sorted_weekly_array = sorted(weekly_array, key=lambda d: d['points']) 
  
    embed = discord.Embed(title="Leaderboard", description=f"Top 10 Users in {str(choices.value)}", color=0x00ff00)
      
    index = 1
      
    if (len(all_database_keys))/2 > 10:
      x = 10
    else:
      x = (len(all_database_keys))/2

    if choices.value == "Stars ⭐️":
      for amt_index in range(len(sorted_points_array)-1, -1, -1):
        amt = sorted_points_array[amt_index]
        embed.add_field(name = f'{index}: {amt["id"]}', value = f'{amt["stars"]}', inline=False)
      
        if index == x:
          break
        else:
          index += 1
          
    if choices.value == "Weeklies":
      for amt_index in range(len(sorted_weekly_array)-1, -1, -1):
        amt = sorted_weekly_array[amt_index]
        embed.add_field(name = f'{index}: {amt["id"]}', value = f'{amt["points"]}', inline=False)
      
        if index == x:
          break
        else:
          index += 1

    await interaction.response.send_message(embed=embed)
    
async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(
    leaderboard(bot),
    guilds = [discord.Object(id = 944699617939968050)])