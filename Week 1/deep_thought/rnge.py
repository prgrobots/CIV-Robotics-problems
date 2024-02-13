
secret = 50
flag = False

while flag == False:

    guess = input('gess a number')
    print('Boiling than 5') if guess in range(secret + 5) or range(secret -5) else None
