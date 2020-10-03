import re

def parseCmd(cmd):
 repeat     = 1
 condition  = 0
 number     = 1
 sides      = 20
 explode    = False
 noCrit     = False
 lower      = False
 bias       = 0
 difficulty = float("-inf")
 rollPattern = re.compile('((?P<repeat>\d+)x)?(?P<condition>[\+\-]+)?(?P<rollBase>((?P<number>\d+)?d(?P<sides>\d+)?)?(?P<crit>[\!\?])?(?P<bias>[\+\-]\d+)?)?(/(?P<lower><)?(?P<difficulty>\d+))?')
 match = rollPattern.match(cmd)
 if match and len(match.group(0)) == len(cmd):
  if match.group('repeat'): repeat = int(match.group('repeat'))
  if match.group('condition'):
   signs = re.findall(r'[\+\-]', match.group('condition'))
   for sign in signs:
    if (sign == '+') : condition+=1
    else             : condition-=1
  if match.group('rollBase'):
   if match.group('number'): number  = int(match.group('number' ))
   if match.group('sides'): sides   = int(match.group('sides'  ))
   if match.group('crit'):
    if re.match(r'\?', match.group('crit')) : noCrit  = True
    else                                   : explode = True
   if match.group('bias'): bias    = int(match.group('bias'   ))
  if match.group('difficulty'): difficulty = int(match.group('difficulty'))
  if match.group('lower'): lower = True
  
 else : repeat = 0
 return [repeat,condition,number,sides,explode,noCrit,lower,bias,difficulty]
