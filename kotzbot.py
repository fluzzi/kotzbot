#!/usr/bin/python3
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
import json
with open('dicts.json') as json_file:
    data = json.load(json_file)
bot = commands.Bot(command_prefix=commands.when_mentioned, case_insensitive=True)
bot.remove_command('help')
def get_cosmo(cosmo):
    todos = "\n"
    day = {
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday',
            7: 'Sunday'
        }
    dia = {
            1: 'Lunes',
            2: 'Martes',
            3: 'Miercoles',
            4: 'Jueves',
            5: 'Viernes',
            6: 'Sabado',
            7: 'Domingo'
        }
    dya = {
            1: 'Lunes/Monday',
            2: 'Martes/Tuesday',
            3: 'Miercoles/Wednesday',
            4: 'Jueves/Thursday',
            5: 'Viernes/Friday',
            6: 'Sabado/Saturday',
            7: 'Domingo/Sunday'
        }
    place= {
            0: 'Titans',
            1: 'Shrine',
            2: 'Titans and Shrine' 
            }
    lugar= {
            0: 'Titanes',
            1: 'Altar',
            2: 'Titanes y Altar' 
            }
    plugar= {
            0: 'Titans',
            1: 'Altar/Shrine',
            2: 'Titans y Altar/shrine' 
            }
    start = 1
    location = 2
    result = ""
    if cosmo.lower() == 'list':
        for key in data['cosmoen']:
            todos = todos + key + ', '
        todos = todos.rstrip(' ').rstrip(',')
        return todos
    if cosmo.lower() == 'lista':
        for key in data['cosmoes']:
            todos = todos + key + ', '
        todos = todos.rstrip(' ').rstrip(',')
        return todos
    elif cosmo.lower() in data['cosmoboth']:
        days = list(map(int,str(data['cdays'][data['cosmoboth'][cosmo.lower()]])))
        if days[0] == 0:
            result= '\n Available on boxes and other events, no shrine or titans \n Disponible en cajas y otros eventos, no esta en Altar o Titanes.'
        else:
            for _ in range(days[0]):
                result= result + '\n' + dya[days[start]] + ': ' + plugar[days[location]]
                start += 2
                location += 2
    elif cosmo.lower() in data['cosmoes']:
        days = list(map(int,str(data['cdays'][data['cosmoes'][cosmo.lower()]])))
        if days[0] == 0:
            result= '\n Disponible en cajas y otros eventos, no esta en Altar o Titanes.'
        else:
            for _ in range(days[0]):
                result= result + '\n' + dia[days[start]] + ': ' + lugar[days[location]]
                start += 2
                location += 2
    elif cosmo.lower() in data['cosmoen']:
        days = list(map(int,str(data['cdays'][data['cosmoen'][cosmo.lower()]])))
        if days[0] == 0:
            result= '\n Available on boxes and other events, no shrine or titans.'
        else:
            for _ in range(days[0]):
                result= result + '\n' + day[days[start]] + ': ' + place[days[location]]
                start += 2
                location += 2
    else:
        result = 0
    return (result)


def get_guide(char,lang):
    todos = ""
    if lang == "en":
        if char.lower() == 'list':
            for key in data['guidedic']:
                todos = todos + key + ', '
            todos = todos.rstrip(' ').rstrip(',')
            return todos
        elif char.lower() in data['guidedic']:
            return data['guidedic'][char.lower()]
        else:
            return 0
    elif lang == "es":
        if char.lower() == 'lista':
            for key in data['guiadic']:
                todos = todos + key + ', '
            todos = todos.rstrip(' ').rstrip(',')
            return todos
        elif char.lower() in data['guiadic']:
            return data['guiadic'][char.lower()]
        else:
            return 0
        return

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(pass_context=True)
async def help(ctx):
    msg = ('{0.author.mention} \n HELP\n cosmo list -> get list of cosmo names\n cosmo name of cosmo -> get cosmo release date and location\n guide list -> get list of characters name\n guide character name -> get character youtube guide')
    msg = msg.format(ctx.message)
    await ctx.send(msg)

@bot.command(pass_context=True)
async def ayuda(ctx):
    msg = ('{0.author.mention} \n AYUDA\n cosmo lista -> lista los nombres de los cosmos\n cosmo nombre de cosmo -> muestra los dias y lugares del cosmo\n guia lista -> lista los nombres de los personajes\n guia nombre del personaje -> muestra el video del analisis del personaje')
    msg = msg.format(ctx.message)
    await ctx.send(msg)

@bot.command(pass_context=True)
async def guia(ctx, * , arg = None):
    real = get_guide(arg,"es")
    if real == 0:
        await ctx.send('Guia invalida...')
        return
    else:
        msg = ('{0.author.mention} Guia ' + arg.capitalize() + ':\n' + real)
        msg = msg.format(ctx.message)
        await ctx.send(msg)

@bot.command(pass_context=True)
async def guide(ctx, * , arg = None):
    real = get_guide(arg,"en")
    if real == 0:
        await ctx.send('Invalid guide...')
        return
    else:
        msg = ('{0.author.mention} Guide ' + arg.capitalize() + ':\n' + real)
        msg = msg.format(ctx.message)
        await ctx.send(msg)

@bot.command(pass_context=True)
async def cosmo(ctx, *, arg = None):
    real = get_cosmo(arg)
    if real == 0:
        await ctx.send('Invalid cosmo...')
        return
    else:
        msg = ('{0.author.mention} Cosmo ' + arg.capitalize() + ':' + real)
        msg = msg.format(ctx.message)
        await ctx.send(msg)

bot.run(token)
