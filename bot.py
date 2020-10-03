import discord
from roller import fullRoll
from parse import parseCmd
from discord.ext import commands
from config import settings

#todo: system dictionary
# d20
# GURPS
# wod

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command(pass_context=True)
async def roll(ctx, *args): # Создаём функцию и передаём аргумент ctx.
 if args and len(args)==1 : params = parseCmd(args[0])
 else                     : params = parseCmd('')
#бросок
 rolls = fullRoll(*params)
 result = ''
 for roll in rolls:
  result+=f'[{roll[1]}]'
  if   roll[0]== 1 : result+=f'success	'
  elif roll[0]== 2 : result+=f'crit!	'
  elif roll[0]==-1 : result+=f'fail	'
  elif roll[0]==-2 : result+=f'crit fail!	'
  else             : result+=f'	'
#вывод результата броска
 await ctx.send(f'{result}')


bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена

