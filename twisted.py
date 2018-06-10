import sys
from randcrack import RandCrack

rc = RandCrack()

from netcat import Netcat

nc = Netcat('89.38.210.129', 6672)

nc.read_until('2. No, give me the next number\n')

for i in range(624):
  nc.write('2\n')
  try:
    nr = int(nc.read_until('\n').split('\n')[0].split(':')[1].strip())
    rc.submit(nr)
  except:
    pass

nc.write('1\n')
for i in range(10):
  pred=rc.predict_randrange(0, 4294967295)
  nc.write(str(pred) + '\n')
  nc.read_until(': ')

print nc.read().strip()
