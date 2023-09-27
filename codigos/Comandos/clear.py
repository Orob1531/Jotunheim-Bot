"""
Este arquivo armazena o Código do comando /clear do Bot.
"""
import discord
from discord.ext import commands

class Clear(commands.Cog):
    """
    Comando de límpeza para apagar mensagens em um canal de Discord.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount: int = 1):
        """
        Apaga um número específico de mensagens (1 por predeterminado).
        Uso: +clear [cantidad]
        """
        if amount < 1:
            await ctx.send("La cantidad debe ser al menos 1.")
            return

        try:
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send(f"Foram apagadas {amount} mensagens.", delete_after=5)
        except discord.Forbidden:
            await ctx.send("Não tenho permissões para apagar Mensagens.")

def setup(bot):
    """
    Borra un número especificado de mensajes en el canal actual.

    :param ctx: El contexto de comando.
    :type ctx: discord.ext.commands.Context
    :param amount: El número de mensajes para borrar (por defecto 5).
    :type amount: int
    """
    bot.add_cog(Clear(bot))
