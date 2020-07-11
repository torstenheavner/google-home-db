from importlib import *
import discord
from discord.ext import commands, tasks
import ease_of_use as eou
import os
import requests



class General(commands.Cog):
	def __init__(self, bot):
		self.bot = bot



	def cog_unload(self):
		eou.log(text="Offline", cog="General", color="magenta")



	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.bot: return

		if message.content.startswith("ok google, "):
			content = message.content.split("ok google, ")[1]

			if content.startswith("are you alive?"):
				await message.channel.send(embed=eou.makeEmbed(title="Yup!", description="Google Home is online."))

			# add commands here:
			# elif content.startswith("command name"):
			#	what to happen when the command is done



def setup(bot):
	eou.log(text="Online", cog="General", color="magenta")
	bot.add_cog(General(bot))
	reload(eou)
