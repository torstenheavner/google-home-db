import sys
from discord.ext import commands
import discord
import ease_of_use as eou

sys.path.append("T:/all 2/Codes")
bot = commands.Bot(command_prefix="ok google, ")

cogs = eou.getData()["cogs"]
eou.clear()
for cog in cogs:
	bot.load_extension(cog)
	eou.log(text=("%s loaded" % cog.upper()))


async def is_owner(ctx):
	return ctx.author.id == 184474965859368960


@bot.event
async def on_connect():
	eou.log(text="Connected")


@bot.event
async def on_disconnect():
	eou.log(text="Disconnected")


@bot.event
async def on_ready():
	eou.log(text="Ready")
	game = discord.Activity(type=discord.ActivityType.listening, name="your household.")
	await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command(name="reload", brief="Reload one or all of the bots cogs")
@commands.check(is_owner)
async def _reload(ctx, cog="all"):
	try:
		await ctx.message.delete()
	except:
		pass
	log = []
	cogs = eou.getData()["cogs"]
	if cog == "all":
		for extension in cogs:
			try:
				bot.reload_extension(extension)
				log.append("**%s** reloaded successfully." % extension)
			except:
				bot.load_extension(extension)
				log.append("**%s** loaded successfully." % extension)

		embed = eou.makeEmbed(title="%s Reloaded Modules" % ctx.author.name, description="\n".join(log))
		await ctx.send(embed=embed)
		eou.log(text="Reloded all modules", ctx=ctx)
	else:
		try:
			bot.reload_extension(cog)
			await ctx.send(embed=eou.makeEmbed(title="%s Reloaded %s" % (ctx.author.name, cog), description="Successfully reloaded!"))
		except:
			bot.load_extension(cog)
			await ctx.send(embed=eou.makeEmbed(title="%s Reloaded %s" % (ctx.author.name, cog), description="Successfully loaded!"))
		eou.log(text="Reloaded %s" % cog, ctx=ctx)


@_reload.error
async def _reload_error(ctx, error):
	if isinstance(error, commands.CheckFailure):
		await ctx.send(embed=eou.makeEmbed(title="Whoops!", description="Only the bot owner can do that command."))
#
#
# @bot.command(name="ping?", brief="Check if the bot is online")
# async def ping(ctx):
# 	await ctx.send(embed=eou.makeEmbed(title="Pong!", description="Google Home is online."))
# 	eou.log(text="Bot Pinged", ctx=ctx)


with open("T:/all 2/tokens/google home.txt", "r") as token:
	bot.run(token.read())
