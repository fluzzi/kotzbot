import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix=commands.when_mentioned)
bot.remove_command('help')
cdays = {
        'firedrop': 3326170,
        'pstone': 3125160,
        'cstone': 22262,
        'eagleeye': 24260,
        'astick': 25062,
        'flowerring': 21171,
        'whitemist': 23171,
        'rosary': 25171,
        'tenacity': 3125160,
        'bloom': 22262,
        'dualdef': 3326071,
        'peacefruit': 24060,
        'seiya': 3415060,
        'bodycare': 21171,
        'knowing': 24171,
        'spiritprint': 26171,
        'staunch': 3102162,
        'healbook': 420316071,
        'newmoon': 411305160,
        'letter': 24260,
        'lotus': 22171,
        'butterfly': 23171,
        'hummingbird': 25171,
        'crystalfire': 26171,
        'daffodil': 21260,
        'kinggiant': 22260,
        'roc': 23260,
        'hyacinth': 24260,
        'mandala': 25260,
        'silverdragon': 26070,
        'vulcanchain': 26070,
        'salamander': 26070,
        'soapberry': 26070,
        '2hornsnake': 21171,
        'felina': 23171,
        'windelf': 24171,
        'dragonteeth': 25171,
        'marshfairy': 0,
        'bloodelf': 0,
        'kingfisher': 0,
        'decelerator': 0,
        'windflower': 0,
        'hephaestus': 0,
        'iris': 0,
        'laureltree': 0,
        'manjuska': 0,
        'equinox': 0
        }
def get_cosmo(cosmo):
    todos = "\n"
    cosmoboth = {
        'seiya': 'seiya',
        'mandala': 'mandala',
        'felina': 'felina',
        'iris': 'iris'
            }
    cosmoes = {
        'piedra fisica': 'pstone',
        'piedra cosmica': 'cstone',
        'gota de fuego': 'firedrop',
        'ojo de aguila': 'eagleeye',
        'antiadherente': 'astick',
        'anillo de flores': 'flowerring',
        'niebla blanca': 'whitemist',
        'rosario': 'rosary',
        'tenacidad': 'tenacity',
        'floracion': 'bloom',
        'defensa dual': 'dualdef',
        'fruta de paz': 'peacefruit',
        'seiya': 'seiya',
        'cuidado de cuerpo': 'bodycare',
        'conocimiento': 'knowing',
        'devoto': 'staunch',
        'libro curacion': 'healbook',
        'luna nueva': 'newmoon',
        'carta': 'letter',
        'loto': 'lotus',
        'mariposa': 'butterly',
        'colibri': 'hummingbird',
        'fuego de cristal': 'crystalfire',
        'narciso': 'daffodil',
        'rey gigante': 'kinggiant',
        'ruc': 'roc',
        'jacinto': 'hyacinth',
        'mandala': 'mandala',
        'dragon de plata': 'silverdragon',
        'cadena de hephesto': 'vulcanchain',
        'salamandra': 'salamander',
        'jaboncillo': 'soapberry',
        'serpiente dos cuernos': '2hornsnake',
        'felina': 'felina',
        'elfo del viento': 'windelf',
        'dientes de dragon': 'dragonteeth',
        'hada del pantano': 'marshfairy',
        'elfo sangriento': 'bloodelf',
        'martin pescador': 'kingfisher',
        'decelerador': 'decelerator',
        'anemona': 'windflower',
        'armadura de hephesto': 'hephaestus',
        'iris': 'iris',
        'arbol de laurel': 'laureltree',
        'lycoris': 'manjuska',
        'flor de equinocio': 'equinox'
    }
    cosmoen = {
        'phyisical stone': 'pstone',
        'cosmic stone': 'cstone',
        'fire drop': 'firedrop',
        'eagle-eye': 'eagleeye',
        'anti-stick': 'astick',
        'flower ring': 'flowerring',
        'white mist': 'whitemist',
        'rosary': 'rosary',
        'tenacity': 'tenacity',
        'bloom': 'bloom',
        'dual defence': 'dualdef',
        'peace fruit': 'peacefruit',
        'seiya': 'seiya',
        'body care': 'bodycare',
        'knowing': 'knowing',
        'staunch': 'staunch',
        'heal book': 'healbook',
        'new moon': 'newmoon',
        'letter': 'letter',
        'lotus': 'lotus',
        'butterfly': 'butterfly',
        'hummingbird': 'hummingbird',
        'crystal fire': 'crystalfire',
        'daffodil': 'daffodil',
        'king giant': 'kinggiant',
        'roc': 'roc',
        'hyacinth': 'hyacinth',
        'mandala': 'mandala',
        'silver dragon': 'silverdragon',
        'vulcan chain': 'vulcanchain',
        'salamander': 'salamander',
        'soapbarry': 'soapberry',
        'two horned snake': '2hornsnake',
        'felina': 'felina',
        'wind elf': 'windelf',
        'rising dragon teeth': 'dragonteeth',
        'marsh fairy': 'marshfairy',
        'blood elf': 'bloodelf',
        'kingfisher': 'kingfisher',
        'decelerator': 'decelerator',
        'windflower': 'windflower',
        'hephaestus armor': 'hephaestus',
        'iris': 'iris',
        'laurel tree': 'laureltree',
        'manjuska': 'manjuska',
        'equinox flower': 'equinox'
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
    if cosmo == 'list':
        for key in cosmoen:
            todos = todos + key + ', '
        todos = todos.rstrip(' ').rstrip(',')
        return todos
    if cosmo == 'lista':
        for key in cosmoes:
            todos = todos + key + ', '
        todos = todos.rstrip(' ').rstrip(',')
        return todos
    elif cosmo in cosmoboth:
        days = list(map(int,str(cdays[cosmoboth[cosmo]])))
        if days[0] == 0:
            result= '\n Available on boxes and other events, no shrine or titans \n Disponible en cajas y otros eventos, no esta en Altar o Titanes.'
        else:
            for _ in range(days[0]):
                result= result + '\n' + dya[days[start]] + ': ' + plugar[days[location]]
                start += 2
                location += 2
    elif cosmo in cosmoes:
        days = list(map(int,str(cdays[cosmoes[cosmo]])))
        if days[0] == 0:
            result= '\n Disponible en cajas y otros eventos, no esta en Altar o Titanes.'
        else:
            for _ in range(days[0]):
                result= result + '\n' + dia[days[start]] + ': ' + lugar[days[location]]
                start += 2
                location += 2
    elif cosmo in cosmoen:
        days = list(map(int,str(cdays[cosmoen[cosmo]])))
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
    guia = {
            'Pandora': 'https://www.youtube.com/watch?v=iG43RbRRqxU',
            'Tauro': 'https://youtu.be/w-4nqw8WJ4M',
            'Poseidon': 'https://youtu.be/J4JpU3WxzOM',
            'Radamantis': 'https://youtu.be/mxp0pe2r9L4',
            'Seiya armadura divina': 'https://youtu.be/kfjGSMYct0s',
            'Gran patriarca': 'https://youtu.be/5Ymc3l7hfLg',
            'Shion': 'https://youtu.be/-6U07cqK97k',
            'Shun Nebular': 'https://youtu.be/H126yUhuzwQ',
            'Hyoga dorado': 'https://youtu.be/TDQBTurv6ks',
            'Arayashiki Shaka': 'https://youtu.be/tUKbUsbWEU8',
            'Saori': 'https://youtu.be/69CAMS5qTck',
            'Krishna': 'https://youtu.be/N9eea4Cy-Ag',
            'Kanon': 'https://youtu.be/XKaNS5UF0HE',
            'Escila': 'https://youtu.be/ai-BhQvGID0',
            'Mu': 'https://youtu.be/lf6OpwveQno',
            'Dohko': 'https://youtu.be/LJUewHLobS0',
            'Seiya flecha dorada': 'https://youtu.be/_zrSvcpRZ9k',
            'Shura': 'https://youtu.be/CV6GLqtQcU8',
            'Aioria': 'https://youtu.be/jFr2k-fJkSE',
            'Shaka': 'https://youtu.be/nqfOAcnce_Q',
            'Aioros': 'https://youtu.be/54k0ZCOQEyk',
            'Afrodita': 'https://youtu.be/KR4UfiDGOes',
            'Milo': 'https://youtu.be/eV5icwh9Kuo',
            'Saga': 'https://youtu.be/HeSzQ-3o9a4'
            }
    guide = {
            'Pandora': 'https://www.youtube.com/watch?v=85qcdq3PYC4&t=6s',
            'Taurus': 'https://youtu.be/cuGPBJ9wEsI',
            'Poseidon': 'https://youtu.be/B8V5LRpqGGQ',
            'Rhadamanthys': 'https://youtu.be/hmYlu1pL0PM',
            'Divine Cloth Seiya': 'https://youtu.be/lKVYe32e5b4',
            'Pope': 'https://youtu.be/Jq0ciJs7USg',
            'Nebular Shun': 'https://youtu.be/BflRXk0I3m0',
            'Golden Cygnus Hyoga': 'https://youtu.be/LFBoyXeZpm8',
            'Arayashiki Shaka': 'https://youtu.be/OPbJ4z6pyc8',
            'Saori': 'https://youtu.be/MsfGVpJMmj4',
            'Krishna': 'https://youtu.be/jeWk6yyZRPc',
            'Kanon': 'https://youtu.be/Uv4b6USvAhk',
            'Scylla': 'https://youtu.be/rC2acVJd2J0',
            'Mu': 'https://youtu.be/hwGpN2SCNHY',
            'Dohko': 'https://youtu.be/t9r7jviQKd0',
            'Golden Arrow Seiya': 'https://youtu.be/GLeNqDmf4dE',
            'Shura': 'https://youtu.be/jWgzAyxnYsY',
            'Aiolia': 'https://youtu.be/n0gmRB_GgZs',
            'Shaka': 'https://youtu.be/pyerg0BiGOE',
            'Aiolos': 'https://youtu.be/fGSJC0sYz4g',
            'Aphrodite': 'https://youtu.be/008U_UBl6Mc',
            'Milo': 'https://youtu.be/LhJTPlI_Rac',
            'Saga': 'https://youtu.be/oM-iyT0J_mA',
            'Shion': 'https://youtu.be/PeTHpvP_rAU'
            }
    if lang == "en":
        if char == 'list':
            for key in guide:
                todos = todos + key + ', '
            todos = todos.rstrip(' ').rstrip(',')
            return todos
        elif char in guide:
            return guide[char]
        else:
            return 0
    elif lang == "es":
        if char == 'lista':
            for key in guia:
                todos = todos + key + ', '
            todos = todos.rstrip(' ').rstrip(',')
            return todos
        elif char in guia:
            return guia[char]
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
