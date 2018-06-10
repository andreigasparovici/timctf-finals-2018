from netcat import *

nc = Netcat('89.38.210.129', 6662)

N = int(nc.read_until('2. Enter password').split('\n')[1].split(' ')[1])

PASSWORD = "I am your father"

crafted_string = "\0" + PASSWORD

nc.write('1\n')

nc.read_until('What do you wanna sign?')

nc.write(crafted_string + '\n')

signed_value = nc.read_until('2. Enter password').split('\n')[0].split(':')[0]

nc.write('2\n')

nc.read_until('Give me the secret password.')

nc.write(signed_value + ':' + PASSWORD + '\n')

print nc.read().strip()
