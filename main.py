#Após ter baixado o dsicrod.py vamos importá-lo.
#Para isso vamos utilizar o "import".
#Vamos também importar o "json" para carregar o arquivo de config do bot.

import discord
import json
from discord.ext.commands import Bot

#Abaixo vamos carregar nosso arquivo.

with open("config.json", "r") as file:
    config = json.loads(file.read())

#Agora, vamos declarar a váriavel principal do nosso Bot.

bot = Bot(command_prefix=config["prefixo"], description="Um simples Bot.")
