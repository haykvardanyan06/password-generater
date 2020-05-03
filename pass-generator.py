from random import randint

def yesorno(s):
    case = None
    while not (case == 'y' or case == 'Y' or case == 'n' or case == 'N' ):
        case = input('Enable {0} (Y/N) '.format(s))
    if (case == 'y' or case == 'Y'):
        return True
    else:
        return False

pass_range = None

while not (type(pass_range) == int):
    try:
        pass_range=int(input('Input length of password from the big 8 '))
        if pass_range < 8:
            print('%s < 8' %pass_range)
            pass_range = None
    except:
        print('!!! Input integer !!!')

uppercase = lowercase = symbol = []

if yesorno('uppercase'):
    uppercase = list(range(65,91))


if yesorno('lowercase'):
    lowercase = list(range(97,123))


if yesorno('symbol'):
    symbol = list(range(33,65)) + list(range(123,127)) + list(range(91,97))

pass_list = uppercase + lowercase + symbol

        
password = ''
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
