#import discord
#from discord.ext import commands
#
#bot = commands.Bot(command_prefix="+")
#
#@bot.event
#async def on_ready():
#   # Configura el estado personalizado del bot
#   activity = discord.Activity(
#   type=discord.ActivityType.watching,  # Puedes cambiar "watching"
#        name="🔱 Administrando servidores!"
#    )
#    await bot.change_presence(activity=activity)
#    print(f"Bot conectado como {bot.user.name}")
#
# Define tus comandos personalizados y el resto de la lógica del bot aquí
#
# Inicia el bot con su token
#bot.run("TU_TOKEN_AQUÍ")
