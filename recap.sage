from netcat import Netcat

NC = Netcat('89.38.210.128', 337)

NC.read_until('Command: ')

def encrypt_value(value):
  NC.write('1\n')
  NC.read_until('Input your message:')
  NC.write(hex(value) + '\n')
  data = NC.read_until('Command: ')
  return data.split('\n')[1].split(' ')[2]

values = [ ]

for i in range(11):
  value =encrypt_value(i * 0x100 + 0xFF)
  values.append((i, int(value, 16),))

R = PolynomialRing(QQ, 'x')
f = R.lagrange_polynomial(values)

NC.write('2\n')
for i in range(11):
  data = NC.read_until('\n')
  to_enc = int(data.split(' ')[2], 16)
  enc = hex(int(f((to_enc - 0xFF)/ 0x100) % (11 ** 128)))

  NC.write(enc[:-1] + '\n')

print NC.read_until('}').split('\n')[1]

NC.close()
