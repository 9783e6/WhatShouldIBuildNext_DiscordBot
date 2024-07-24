import discord
from discord.ext import commands
from config import TOKEN


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.default(), command_prefix="!")

        self.cogs_extensions = ["cogs.commands", "cogs.about"]

    async def setup_hook(self):
        for ext in self.cogs_extensions:
            await super().load_extension(ext)

        await bot.tree.sync()
        print("Cog loading complete!")

    async def on_ready(self):
        print(f"Logged in as {bot.user}")


bot = Bot()
bot.run(TOKEN)
