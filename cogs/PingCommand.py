from discord import Option
from discord.commands import slash_command
from discord.ext import commands


class PingCommand(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @slash_command(name='ping', description='Example slash command.')
    async def test_command(self, ctx: discord.ApplicationContext, test_string: Option(str, 'The string to say')):
        await ctx.defer()
        return f"User said {test_string}"
        
def setup(bot: commands.Bot) -> None:
    bot.add_cog(PingCommand(bot))
    bot.tree.sync()  # Ensure the slash command is synced with the Discord API

    **setup**
    def load cog():
        try:
            import os
            print(os.getcwd())
            
        except Exception as e:
            print("An error occurred: ", str(e))
            
def setup(bot: commands.Bot) -> None:
    bot.add_cog(PingCommand(bot))
    bot.tree.sync()  # Ensure the slash command is synced with the Discord API