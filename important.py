import random

an = 200
ru = 60
sh = 80

while an>0:
    ra =random.randrange(ru,sh)
    an = an-ra

    if an <= 00 :
        an = 00
    print("your random is",ra,"you haved",an)

    if an == 00:
      print("you died")
      break



