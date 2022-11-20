import requests, discord
from discord.ext import commands
import settings

@commands.command()
async def chat(ctx: commands.Context, *, message: str):
	brainId = format(settings.CHAT_API_ID)
	apiKey = format(settings.CHAT_API_KEY)
	res = requests.get(f'http://api.brainshop.ai/get?bid={brainId}&key={apiKey}&uid={ctx.author.id}&msg={message}')
	content = res.json()['cnt']
	embed = discord.Embed(
		colour=discord.Colour.blue(),
		title='🎃 Tunybot',
		description=f'**{content}**'
	)
	await ctx.reply(embed=embed)

@chat.error
async def chat_error(ctx: commands.Context, error: commands.CommandError):
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(
			colour=discord.Colour.blue(),
			title='❌ Error: `Missing Argument`',
			description='```Please enter a message.```'
		)
		return await ctx.reply(embed=embed)