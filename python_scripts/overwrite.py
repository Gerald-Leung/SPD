import filecmp

'''This script is merely for
overwriting oldSPD.txt for
testing purposes.'''

x = '28123981740982710'

with open('oldSPD.txt','w') as f:
    f.write(x)
