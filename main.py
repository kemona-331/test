import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'ログインしました: {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('こんにちは！')

bot.run("YOUR_BOT_TOKEN")
