import random

def rollDie(number,sides,explode):
 i = 0
 roll = 0
 while i<number:
  i+=1
  roll+=random.randint(1, sides)
 if explode and roll == number*sides: roll+=rollDie(number,sides,explode)
 return roll
def fullRoll(repeat,condition,number,sides,explode,noCrit,lower,bias,difficulty):
#проверка на корректрость ввода
 result = []
 if repeat<=0 or number<=0 or sides<=1: return result
#несколько проверок
 rep = 0
 while rep < repeat:
  rep+=1
#бросок с преимуществом или помехой
  if condition != 0:
   tmp = []
   conditionRep = 0
   while conditionRep < abs(condition):
    conditionRep+=1
    tmp.append(rollDie(number,sides,explode))
   if condition>0: roll = max(tmp)
   else          : roll = min(tmp)
  else           : roll = rollDie(number,sides,explode)
#проверка на крит
  if noCrit                    : crit = 0
  else:
   if   (roll == number*sides) : crit = 1
   elif (roll == number*1)     : crit = -1
   else                        : crit = 0
#проверка на успех
  roll+=bias
  if difficulty!=float("-inf"):
   roll-=difficulty
   if   crit== 1: sucsess = 2
   elif crit==-1: sucsess = -2
   elif (not lower and roll>=0) or (lower and roll<=0): sucsess = 1
   else : sucsess = -1
  else : sucsess = 0
  res = [sucsess,roll]
  result.append(res)
 return result