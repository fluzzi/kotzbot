#!/usr/bin/python3
import discord
import os
import datetime
import langdetect
import subprocess
from discord.ext import commands
from dotenv import load_dotenv
from langdetect import detect
from random import randint
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
prefix = ['silla-san ','silla san ','Silla-san ','Silla-San ','Silla san ','Silla San ','SILLA SAN ','SILLA-SAN ','silla-sama ','silla sama','Silla-sama ','Silla-Sama ','Silla sama ','Silla Sama ','SILLA SAMA ','SILLA-SAMA ']
prefixes = ['silla san','silla-san','silla sama','silla-sama']
comms = ['help','ayuda','guia','guide','cosmo','legion','guía','legión','info','add','delete','del','remove','rem','admins']
import time
import threading
import json
dataText = ""
def fileWatcher():
    global data, dataText
    while True:
        f = open('dicts.json')
        content = f.read()
        f.close()
        if content != dataText:
            print("File was modified! Reloading it...")
            data = json.loads(content)
            dataText = content
        time.sleep(2) #Adjust this to get the best performance
threading.Thread(target=fileWatcher).start()
bot = commands.Bot(command_prefix=commands.when_mentioned_or(*prefix), case_insensitive=True)
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
            'Miércoles': 3,
            'Jueves': 4,
            'Viernes': 5,
            'Sabado': 6,
            'Sábado': 6,
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
            3: 'Miércoles',
            4: 'Jueves',
            5: 'Viernes',
            6: 'Sábado',
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
    if cosmo.lower() == 'mañana':
        return get_today('es', datetime.datetime.today().isoweekday() + 1)
    if cosmo.lower() == 'tomorrow':
        return get_today('en', datetime.datetime.today().isoweekday() + 1)
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

def get_info(char):
    todos = ""
    if char.lower() == 'lista':
        for key in data['info']:
            todos = todos + key + ', '
        todos = todos.rstrip(' ').rstrip(',')
        return todos
    elif char.lower() in data['info']:
        return data['info'][char.lower()]
    else:
         return 0

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

def get_today(lang,date = "" ):
    if date == "":
        date = datetime.datetime.today().isoweekday()
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

def get_admins():
    result = ""
    for key in data['admins']:
        result = result + key + ': [ ' + " , ".join(data['admins'][key]) + ' ]\n'
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

def add_data(editor,typ,name,link):
    if typ.lower() == "info":
        if name.lower() in data['info']:
            msg = name + " already exist"
        else:
            data['info'][name.lower()] = link
            with open('dicts.json', 'w') as fp:
                json.dump(data, fp, sort_keys=True, indent=4)
            addcommand = "git add dicts.json && git commit -m 'command add {} {}' && git push -u origin master".format(typ,editor)
            addf = subprocess.Popen(addcommand,shell=True)
            msg = name + " added succesfuly"
        return msg
    elif typ.lower() == "guia":
        if name.lower() in data['guiadic']:
            msg = name + " already exist"
        else:
            data['guiadic'][name.lower()] = link
            with open('dicts.json', 'w') as fp:
                json.dump(data, fp, sort_keys=True, indent=4)
            addcommand = "git add dicts.json && git commit -m 'command add {} {}' && git push -u origin master".format(typ,editor)
            addf = subprocess.Popen(addcommand,shell=True)
            msg = name + " added succesfuly"
        return msg
    elif typ.lower() == "guide":
        if name.lower() in data['guidedic']:
            msg = name + " already exist"
        else:
            data['guidedic'][name.lower()] = link
            with open('dicts.json', 'w') as fp:
                json.dump(data, fp, sort_keys=True, indent=4)
            addcommand = "git add dicts.json && git commit -m 'command add {} {}' && git push -u origin master".format(typ,editor)
            addf = subprocess.Popen(addcommand,shell=True)
            msg = name + " added succesfuly"
        return msg
    elif typ.lower() == "legion":
        if name.lower() in data['legion']:
            msg = name + " already exist"
        else:
            data['legion'][name.lower()] = link
            with open('dicts.json', 'w') as fp:
                json.dump(data, fp, sort_keys=True, indent=4)
            addcommand = "git add dicts.json && git commit -m 'command add {} {}' && git push -u origin master".format(typ,editor)
            addf = subprocess.Popen(addcommand,shell=True)
            msg = name + " added succesfuly"
        return msg
    elif typ.lower() == "admins":
        if name in data['admins']:
            msg = name + " already exist"
        else:
            data['admins'][name] = link.lower().split()
            with open('dicts.json', 'w') as fp:
                json.dump(data, fp, sort_keys=True, indent=4)
            addcommand = "git add dicts.json && git commit -m 'command add {} {}' && git push -u origin master".format(typ,editor)
            addf = subprocess.Popen(addcommand,shell=True)
            msg = name + " added succesfuly"
        return msg

def del_data(editor,typ,name,link):
    if typ.lower() == "info":
        if name.lower() not in data['info']:
            msg = name + " don't exist"
        else:
            del data['info'][name.lower()]
            with open('dicts.json', 'w') as fp:
                json.dump(data, fp, sort_keys=True, indent=4)
            addcommand = "git add dicts.json && git commit -m 'command delete {} {}' && git push -u origin master".format(typ,editor)
            addf = subprocess.Popen(addcommand,shell=True)
            msg = name + " deleted succesfuly"
        return msg
    elif typ.lower() == "guia":
        if name.lower() not in data['guiadic']:
            msg = name + " don't exist"
        else:
            del data['guiadic'][name.lower()]
            with open('dicts.json', 'w') as fp:
                json.dump(data, fp, sort_keys=True, indent=4)
            addcommand = "git add dicts.json && git commit -m 'command delete {} {}' && git push -u origin master".format(typ,editor)
            addf = subprocess.Popen(addcommand,shell=True)
            msg = name + " deleted succesfuly"
        return msg
    elif typ.lower() == "guide":
        if name.lower() not in data['guidedic']:
            msg = name + " don't exist"
        else:
            del data['guidedic'][name.lower()]
            with open('dicts.json', 'w') as fp:
                json.dump(data, fp, sort_keys=True, indent=4)
            addcommand = "git add dicts.json && git commit -m 'command delete {} {}' && git push -u origin master".format(typ,editor)
            addf = subprocess.Popen(addcommand,shell=True)
            msg = name + " deleted succesfuly"
        return msg
    elif typ.lower() == "legion":
        if name.lower() not in data['legion']:
            msg = name + " don't exist"
        else:
            del data['legion'][name.lower()]
            with open('dicts.json', 'w') as fp:
                json.dump(data, fp, sort_keys=True, indent=4)
            addcommand = "git add dicts.json && git commit -m 'command delete {} {}' && git push -u origin master".format(typ,editor)
            addf = subprocess.Popen(addcommand,shell=True)
            msg = name + " deleted succesfuly"
        return msg
    elif typ.lower() == "admins":
        if name not in data['admins']:
            msg = name + " don't exist"
        else:
            del data['admins'][name]
            with open('dicts.json', 'w') as fp:
                json.dump(data, fp, sort_keys=True, indent=4)
            addcommand = "git add dicts.json && git commit -m 'command delete {} {}' && git push -u origin master".format(typ,editor)
            addf = subprocess.Popen(addcommand,shell=True)
            msg = name + " deleted succesfuly"
        return msg

def randomResponse():
    responses = data["respuestas_standard"]
    quantityOfResponses = len(responses)
    indexOfSelectedResponse = randint(0, quantityOfResponses - 1)
    return responses[indexOfSelectedResponse]

def getQuestion(text):
    questions = data["preguntas"]
    questionsFiltered = list(filter(lambda question: question["pregunta"] in text, questions))
    return questionsFiltered

def isInQuestions(text):
    questionsFiltered = getQuestion(text)
    return len(questionsFiltered) > 0

def getResponseToQuestion(text):
    questionsFiltered = getQuestion(text)
    responses = questionsFiltered[0]["respuestas"]
    quantityOfResponses = len(responses)
    indexOfSelectedResponse = randint(0, quantityOfResponses - 1)
    return responses[indexOfSelectedResponse]

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(pass_context=True)
async def help(ctx):
    msg = ('{0.author.mention} \n HELP\n cosmo list -> get list of cosmo names\n cosmo name of cosmo -> get cosmo release date and location\n cosmo today/tomorrow/weekday -> get cosmo released on specific day\n guide list -> get list of characters name\n guide character name -> get character youtube guide\n legion # -> leader info of legion on specified server\n info character name -> show infography of requested character')
    msg = msg.format(ctx.message)
    await ctx.send(msg)

@bot.command(pass_context=True)
async def ayuda(ctx):
    msg = ('{0.author.mention} \n AYUDA\n cosmo lista -> lista los nombres de los cosmos\n cosmo nombre de cosmo -> muestra los dias y lugares del cosmo\n cosmo hoy/mañana/dia de la semana -> muestra los cosmos que salen ese dia\n guia lista -> lista los nombres de los personajes\n guia nombre del personaje -> muestra el video del analisis del personaje\n legión # -> muestra el nombre del lider de la legión en el servidor\n info lista -> lista las infografías disponibles\n info nombre del personaje -> muestra la infografía del personaje')
    msg = msg.format(ctx.message)
    await ctx.send(msg)

@bot.command(pass_context=True)
async def admins(ctx, * , arg = None):
        msg = get_admins()
        await ctx.send(msg)

@bot.command(pass_context=True)
async def add(ctx, typ = None, name = None, datos = None):
    if ( typ in data['admins'][str(ctx.author)] ):
        msg = add_data(str(ctx.author),typ,name,datos)
        await ctx.send(msg)
    else:
        msg = "No hago caso a insectos."
        await ctx.send(msg)

@bot.command(pass_context=True, aliases=['remove', 'del', 'rem'])
async def delete(ctx, typ = None, name = None):
    if ( typ in data['admins'][str(ctx.author)] ):
        msg = del_data(str(ctx.author),typ,name,data)
        await ctx.send(msg)
    else:
        msg = "No hago caso a insectos."
        await ctx.send(msg)

@bot.command(pass_context=True)
async def info(ctx, * , arg = None):
    real = get_info(arg)
    if real == 0:
        await ctx.send('Infografía invalida...')
        return
    else:
        msg = ('{0.author.mention} Infografía ' + arg.capitalize() + ':\n' + real)
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

@bot.command(pass_context=True, aliases=['legión'])
async def legion(ctx, *, arg = None):
    msg = (get_legion(arg))
    msg = msg.format(ctx.message)
    await ctx.send(msg)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    elif any(i in message.content.lower() for i in comms):
        pass
    elif bot.user in message.mentions or any (i in message.content.lower() for i in prefixes):
        if isInQuestions(message.content.lower()):
            if (message.channel.id == 565536811242487840):
                return
            else:
                msg = getResponseToQuestion(message.content.lower())
        elif ("Alezar#8727" == str(message.author)) or ("Gederico#5402" == str(message.author)):
            if ("te amo" in message.content) or ("te quiero" in message.content):
                msg = (message.author.mention + ' y yo a ti \U0001F60D')
            elif ("te odio" in message.content):
                msg = (message.author.mention + ' no me odies \U0001F61E')
            else:
                if (message.channel.id == 565536811242487840):
                    return
                else:
                    msg = randomResponse()
        else:
            if ("te amo" in message.content) or ("te quiero" in message.content):
                msg = (message.author.mention + ' ok gracias')
            elif ("te odio" in message.content):
                msg = (message.author.mention + ' y yo a ti, insignificante humano')
            else:
                if (message.channel.id == 565536811242487840):
                    return
                else:
                    msg = randomResponse()
        await message.channel.send(msg)
    elif bot.user not in message.mentions:
        if (message.channel.id == 565536811242487840):
            if detect(message.content) == 'es' and len(message.content) > 3:
                msg = (message.author.mention + ' This is an english only channel // Este canal es solo en ingles\n para español usar <#624818561961164810>')
                await message.channel.send(msg)
            else:
                return
        else:
            return
    await bot.process_commands(message)

bot.run(token)


