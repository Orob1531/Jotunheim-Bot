"""
Este arquivo armazena o início do Bot. Aqui serão feitas as chamadas aos comandos.
"""
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from Comandos import clear

# Desabilita a mensagem de erro do Pylint para importações
# pylint: disable=import-error

# Carrega as variáveis de ambiente a partir do arquivo .env
load_dotenv()

# Obtém o token das variáveis de ambiente e autentificação
CLIENT_ID = os.getenv("DISCORD_CLIENT_ID")
CLIENT_SECRET = os.getenv("DISCORD_CLIENT_SECRET")
TOKEN = os.getenv("DISCORD_TOKEN")

# Verifica se o token foi carregado corretamente
if TOKEN is None:
    print("Token não encontrado. Certifique-se de configurar DISCORD_TOKEN no arquivo .env.")
    exit(1)

# Define as intenções necessárias para o seu bot
# Cria uma instância do bot com as intenções
# Configurar el bot
intents = discord.Intents.all()
intents.members = True
intents.messages = True
bot = commands.Bot(command_prefix="+", intents=intents)  # Cambia el prefijo a tu elección

# Evento para indicar que o bot está pronto
@bot.event
async def on_ready():
    """
    Este evento se llama cuando el bot se ha conectado y está listo para funcionar.
    Configura el estado personalizado del bot para mostrar "🔱 Administrando servidores!"
    como actividad.
    """
    activity = discord.Activity(
        type=discord.ActivityType.custom,  # Tipo de actividad,
        #puedescambiarlo según tus preferencias
        name="🔱 Administrando servidores!"  # Texto de la actividad
    )
    await bot.change_presence(activity=activity)
    print(f"Bot conectado como {bot.user.name}")

# Importe e carregue seus comandos e funcionalidades de outros arquivos
# Importa la extensión del comando "clear"
# Agrega la extensión al bot
bot.add_cog(clear.Clear(bot))
#
# Por exemplo:
# from comandos import meu_comando
# bot.add_command(meu_comando)
#
# Exemplo de importação de um módulo de comandos:
# from comandos import comando1, comando2
# bot.add_command(comando1)
# bot.add_command(comando2)

# Inicia o bot com o token
bot.run(TOKEN)
