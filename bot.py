import discord
import os
import random

from variables import token_discord 

from discord.ext import commands


bot = commands.Bot(command_prefix='causa!')

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
async def archivar(ctx,*args):
	
	data = args
	demandante = ''
	demandado = ''
	resultado = ''


	
	if len(data) == 0:
		msj = '''
		
		:warning: Te falta ingresar el nombre del demandante y demandado :warning: 
		``` causa!abrir "nombre_demandante" "nombre_demandado" "resultado" ```

		'''
		await ctx.send(msj)
	if len(data) == 1:
		demandante = data[0]
		await ctx.send("Te falta ingresar el nombre del demandado")

	if len(data) == 2:
		demandante = data[0]
		demandado = data[1]
		await ctx.send("Te falta ingresar el resultado de la causa")
	else:
		demandante = data[0]
		demandado = data[1]
		resultado = data[2]
		causa = str(random.randint(00000, 99999))
		m1 = ':briefcase: Se ha archivado una nueva causa por <@{0}> '.format(ctx.message.author.id)
		m2 = '''
		========================
		Causa Nº {0}
		Demandante: {1}
		Demandado: {2}
		=
		Resultado
		=
		{3}
		========================

		'''.format(causa,demandante,demandado,resultado)
		await ctx.send(m1 + m2)


 


bot.run(token_discord)