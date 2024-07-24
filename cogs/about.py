import discord
from discord import app_commands
from discord.ext import commands
import config


class About(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="about", description="Displays info about the bot.")
    async def reset_viewed_projects(self, interaction: discord.Interaction):
        user_id = interaction.user.id

        embed = discord.Embed(
            title=f"Info about WhatShouldIBuildNext",
            description=f"This bot was developed by [9783e6](https://github.com/9783e6)(<@1033575643323052102> on discord).\n\n[My discord server(Support/bug reports/feature requests here)](https://discord.gg/3HQKbwFzpR)\n\n[Project's source code]().\n",
            color=0x9783e6,
        )
        embed.set_footer(text=f"This instance of the bot is ran by {config.InstanceRanBy}.")
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(About(bot))