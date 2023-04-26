"""Python tem modolo de datetime"""

import datetime

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

print(datetime.datetime.now())

nasc = input('Informe sua data de nascimento dd/mm/yyyy: ')

print(nasc)

nasc = nasc.split('/')

nasc = datetime.datetime(int(nasc[2]), int(nasc[1]), int(nasc[0]))

print(nasc)