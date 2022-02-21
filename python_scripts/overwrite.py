import filecmp
import os

'''This script is merely for
overwriting oldSPD.txt for
testing purposes.'''

x = '28123981740982710'

with open('oldSPD.txt','w') as f:
    f.write(x)

os.system('rm -rf ./NRS_SPD_2021-2_CSV')
