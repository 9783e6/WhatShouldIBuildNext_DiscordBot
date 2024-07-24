import discord
from discord import app_commands
from discord.app_commands import Choice
from discord.ext import commands
import utils.projects_data as pd
import utils.users_db as udb


class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="what_should_i_build_next", description="Says what you should build.")
    @app_commands.describe(category="Select the category you want to build a project in.")
    @app_commands.choices(category=pd.get_categories_as_choices())
    @app_commands.describe(difficulty="Select the difficulty level for the project.")
    @app_commands.choices(difficulty=pd.get_difficultries_as_choices())
    async def chest_open(self, interaction: discord.Interaction, category: Choice[int] = None, difficulty: Choice[int] = None):
        user_id = interaction.user.id
        viewed_projects = udb.get_user_viewed_projects(user_id)

        project = pd.select_random_project(viewed_projects, category, difficulty)
        if project is not None:
            udb.add_user_viewed_projects(user_id, project["project_id"])
            embed = discord.Embed(
                title=f"You should build {project['project_name']}!",
                description=f"{project['project_desc'].capitalize()}",
                color=0x9783e6,
            )
            embed.set_footer(text=f"Category: {project["category"]} / Difficulty: {project["difficulty"]}")
        else:
            embed = discord.Embed(
                title=f"You viewed all available projects!",
                description="Use /reset_viewed_projects to reset your viewed projects history.",
                color=0x9783e6,
            )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="reset_viewed_projects", description="Reset your viewed projects history")
    async def reset_viewed_projects(self, interaction: discord.Interaction):
        user_id = interaction.user.id

        udb.clear_user_viewed_projects(user_id)
        embed = discord.Embed(
            title=f"Your viewed projects history have been reset!",
            color=0x9783e6,
        )
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Commands(bot))
