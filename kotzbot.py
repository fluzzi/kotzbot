#!/usr/bin/python3
import discord
import os
import datetime
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
import json
with open('dicts.json') as json_file:
    data = json.load(json_file)
bot = commands.Bot(command_prefix=commands.when_mentioned_or('silla-san ','silla san ','Silla-san ','Silla-San ','Silla san ','Silla San ','SILLA SAN ','SILLA-SAN ', ':androlSillaSan:'), case_insensitive=True)
bot.remove_command('help')
def get_cosmo(cosmo):
    todos = "\n"
    dayc = {
            'Monday': 1,
            'Tuesday': 2,
            'Wednesday': 3,
            'Thursday': 4,
            'Friday': 5,
            'Saturday': 6,
            'Sunday': 7
        }
    diac = {
            'Lunes': 1,
            'Martes': 2,
            'Miercoles': 3,
            'Jueves': 4,
            'Viernes': 5,
            'Sabado': 6,
            'Domingo': 7
        }
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
    if cosmo.lower() == 'hoy':
        return get_today('es')
    if cosmo.lower() == 'today':
        return get_today('en')
    if cosmo.lower().capitalize() in diac:
        return get_today('es',diac[cosmo.lower().capitalize()])
    if cosmo.lower().capitalize() in dayc:
        return get_today('en',dayc[cosmo.lower().capitalize()])
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

def get_today(lang,date = datetime.datetime.today().isoweekday()):
    if lang == "es":
        titans = "\nTitanes: "
        shrine = "Altar: "
    if lang == "en":
        titans = "\nTitans: "
        shrine = "Shrine: "
    result = ""
    for key in data['cdays']:
        start1 = 1
        location1 = 2
        start2 = 1
        location2 = 2
        days = list(map(int,str(data['cdays'][key])))
        if days[0] > 0:
            for _ in range(days[0]):
                if (days[location1] == 0 or days[location1] == 2) and days[start1] == date:
                    if lang == "es":
                        titans = titans  + list(data['cosmoes'].keys())[list(data['cosmoes'].values()).index(key)] + ', '
                    elif lang == "en":
                        titans = titans + list(data['cosmoen'].keys())[list(data['cosmoen'].values()).index(key)] + ', '
                    break
                else:
                    start1 += 2
                    location1 += 2
            for _ in range(days[0]):
                if (days[location2] == 1 or days[location2] == 2) and days[start2] == date:
                    if lang == "es":
                        shrine = shrine + list(data['cosmoes'].keys())[list(data['cosmoes'].values()).index(key)] + ', '
                    elif lang == "en":
                        shrine = shrine + list(data['cosmoen'].keys())[list(data['cosmoen'].values()).index(key)] + ', '
                    break
                else:
                    start2 += 2
                    location2 += 2
    titans = titans.rstrip(' ').rstrip(',')
    shrine = shrine.rstrip(' ').rstrip(',')
    result = titans + '\n' + shrine
    return result

def get_legion(server = ""):
    result = ""
    if server == "lista" or server == "list":
        for key in data['legion']:
            result = result + key.upper() + ': ' + data['legion'][key] + '\n'
    elif server.lower() in data['legion']:
        result = server.upper() + ': ' + data['legion'][server.lower()]
    else:
        result = 'La legion no existe en ' + server.upper()
    return result

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(pass_context=True)
async def help(ctx):
    msg = ('{0.author.mention} \n HELP\n cosmo list -> get list of cosmo names\n cosmo name of cosmo -> get cosmo release date and location\n cosmo today/weekday -> get cosmo released on specific day\n guide list -> get list of characters name\n guide character name -> get character youtube guide')
    msg = msg.format(ctx.message)
    await ctx.send(msg)

@bot.command(pass_context=True)
async def ayuda(ctx):
    msg = ('{0.author.mention} \n AYUDA\n cosmo lista -> lista los nombres de los cosmos\n cosmo nombre de cosmo -> muestra los dias y lugares del cosmo\n cosmo hoy/dia de la semana -> muestra los cosmos que salen ese dia\n guia lista -> lista los nombres de los personajes\n guia nombre del personaje -> muestra el video del analisis del personaje')
    msg = msg.format(ctx.message)
    await ctx.send(msg)

@bot.command(pass_context=True, aliases=['guía'])
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

@bot.command(pass_context=True)
async def legion(ctx, *, arg = None):
    msg = (get_legion(arg))
    msg = msg.format(ctx.message)
    await ctx.send(msg)
bot.run(token)
