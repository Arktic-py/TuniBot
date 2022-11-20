import discord, requests, random
from discord.ext import commands

url = "http://randomfox.ca/floof/"
@commands.command(aliases=["foxy"])
async def fox(ctx: commands.Context):
	taglist = ["Isnt he cute?", "Just look at him!!", "SOO cute", "Omg look how cute he is!", "ULTRA CUTE!!"]
	tagline = random.choice(taglist)
	res = requests.get(url).json()
	if res['image'] is not None:
		embed = discord.Embed(
			colour=discord.Colour.dark_blue(),
			title=(f'🦊 {tagline}')
		)
		embed.set_image(url=res['image'])
		return await ctx.reply(embed=embed)
	else:
		embed = discord.Embed(
			colour=discord.Colour.dark_blue(),
			title='🦊❌ Foxy fox Error',
			description='Could not load Fox image(s).'
		)
		return await ctx.reply(embed=embed)

