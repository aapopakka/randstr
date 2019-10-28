## Generates random strings and hashes them with crypt.mksalt() and saves the hashed string in an output file
#
#
import string
import crypt
import readline
from random import *
 
chars = string.ascii_letters + string.digits
getfilename = input('Choose outputfile: ')
filename = getfilename+'.rpw'
randchars =  "".join(choice(chars) for x in range(randint(10, 14)))
salt = crypt.mksalt()
crypted = crypt.crypt(randchars, salt)
 
file = open(filename, 'w')
file.write(crypted+"\n")
file.close()
 
print("Random generated string: ",randchars,"\nHash: ",crypted,"\nSalt: ",salt,"\nOutput file: ",filename)
##
#
