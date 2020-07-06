import discord
import os
from discord.ext import commands
import random

token = "NzI5NTU4MDA1NTkwNTIzOTE0.XwKsAw.uWLL0u0Fo0Z9TJsoLUVXRVFUwcw"


bot = commands.Bot(command_prefix='pjud!')

# @bot.command()
# async def start(ctx):
# 	os.system("java -Xmx2G -jar /opt/minecraft/survival/minecraft_server.jar nogui")
# 	await ctx.send('Iniciando server')

# @bot.command()    
# async def admin(ctx,*,arg):
# 	ex = os.system(arg)
# 	await ctx.send(ex)


@bot.command()
async def hola(ctx):
	await ctx.send('Bienvenid@  <@{0}> al Poder Judicial de COPETIADOS 3.0'.format(ctx.message.author.id))

@bot.command()
async def open(ctx,demandante,demandado):
	causa = str(random.randint(00000, 99999))
	m1 = 'Se ha habierto una nueva causa por <@{0}> '.format(ctx.message.author.id)
	m2 = '''
	========================
	Causa Nº {0}
	Demandante: {1}
	Demandado: {2}
	Status: Abierto
	========================

	'''.format(causa,demandante,demandado)
	await ctx.send(m1 + m2)


@bot.command()
async def take(ctx,causa,abogado1):
	demandante = "Alex Zeld"
	demandado = "Pablo Escobar"
	motivo = "Se definio que el acusado debera pagar $1.000.000 CLP al demandante"
	abogado1 = abogado1

	m1 = '<@{0}> ha tomado el caso nº{1} '.format(ctx.message.author.id,causa)
	m2 = '''
	========================
	Causa Nº {0}
	Demandante: {1}
	Demandado: {2}
	Status: En Progreso

	Abogado Demandante: {3}

	========================

	'''.format(causa,demandante,demandado,abogado1)
	await ctx.send(m1 + m2)


@bot.command()
async def auto(ctx,causa):
	abogado1 = "Mila Wallace"

	resultado = random.randint(1, 100)

	if resultado < 30:
		resultado = "Se ha perdido el caso"

	else:
		resultado = "Se ha ganado el caso"

	m2 = '''
	========================
	Causa Nº {0}
	Abogado Demandante: {1} 
	
	========================
	
	Resultado automatico: ```{2}```

	========================

	'''.format(causa,abogado1,resultado)
	await ctx.send(m2)



@bot.command()
async def close(ctx,causa):
	demandante = "Alex Zeld"
	demandado = "Pablo Escobar"
	motivo = "Se definio que el acusado debera pagar $1.000.000 CLP al demandante"
	abogado1 = "Mila Wallace"

	m1 = 'Se ha cerrado una nueva causa por <@{0}> '.format(ctx.message.author.id)
	m2 = '''
	========================
	Causa Nº {0}
	Demandante: {1}
	Demandado: {2}
	Status: Cerrado

	Abogado Demandante: {3} 

	Motivo: ```{4}```

	========================

	'''.format(causa,demandante,demandado,abogado1,motivo)
	await ctx.send(m1 + m2)

@bot.command()
async def search(ctx,causa):
	demandante = "Alex Zeld"
	demandado = "Pablo Escobar"
	motivo = "Se definio que el acusado debera pagar $1.000.000 CLP al demandante"
	abogado1 = "Mila Wallace"

	
	m2 = '''
	========================
	Causa Nº {0}
	Demandante: {1}
	Demandado: {2}
	Status: Cerrado

	Abogado Demandante: {3} 

	Motivo: ```{4}```
	========================

	'''.format(causa,demandante,demandado,abogado1,motivo)
	await ctx.send(m2)


bot.run(token)