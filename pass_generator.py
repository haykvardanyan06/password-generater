from random import randint


pass_range = uppercase = lowercase = symbol = None
while not (type(pass_range) == int):
    try:
        pass_range=int(input('Input length of password from the big 8 '))
        if pass_range < 8:
            print('%s < 8' %pass_range)
            pass_range = None
    except:
        print('!!! Input integer !!!')
        
password = ''

while not (uppercase == 'y' or uppercase == 'Y' or uppercase == 'n' or uppercase == 'N' ):
    uppercase = input('Enable uppercase (Y/N) ') #65-90
if (uppercase == 'y' or uppercase == 'Y'):
    uppercase = list(range(65,91))
else:
    uppercase = []
while not (lowercase == 'y' or lowercase == 'Y' or lowercase == 'n' or lowercase == 'N' ):
    lowercase = input('Enable lowercase (Y/N) ') #97-122
if (lowercase == 'y' or lowercase == 'Y'):
    lowercase = list(range(97,123))
else:
    lowercase = []
while not (symbol == 'y' or symbol == 'Y' or symbol == 'n' or symbol == 'N' ):
    symbol = input('Enable symbol (Y/N) ') #33-64, 123-126, 91-96
if (symbol == 'y' or symbol == 'Y'):
    symbol = list(range(33,65)) + list(range(123,127)) + list(range(91,97))
else:
    symbol = []

pass_list = uppercase + lowercase + symbol
if pass_list != []:
    j = 0
    for i in range(pass_range):
        j = randint(33,127)
        while not j in pass_list:
            j = randint(33,127)
        password += chr(j)
        j = 0
    print('Your password: %s' %password)
else:
    print('!!! generation canceled !!!')
