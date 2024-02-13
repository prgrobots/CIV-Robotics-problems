import random

secret = random.randint(1,100)
print(secret) 
flag = False

while flag == False:
    guess = int(input("what's your guess? : "))

    if guess >= secret +10:
        print('Warm, try again')

    elif secret <= guess -10:
        print('Freezing, try again')

    elif secret >= guess + 5:
        print('Hot, try again')

    elif secret <= guess - 5:
        print('Cold, try again')

    elif guess == secret:
        flag = True
        print('well done')
    


