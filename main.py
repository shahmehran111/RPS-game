import random

li = ['scissor', 'rock', 'paper']

while True:
    u_count = 0
    c_count = 0
    option = int(input('''
    1. Play
    2. Exit
        '''))
    if option == 1:
        for n in range(0,5):

                ch = int(input('''
                        1. scissor
                        2. rock
                        3. paper
                        '''))
                user = li[ch-1]
                com = random.choice(['scissor', 'rock', 'paper'])

                if user == com:
                    print('''Draw''')

                elif user == 'scissor' and com == 'paper' or user == 'paper' and com == 'rock' or user == 'rock' and com == 'scissor':
                    print('''You Win''')
                    u_count += 1
                else:
                    print('''Computer Win''')
                    c_count += 1
        if u_count == c_count:
            print("Match Draw")
        elif u_count > c_count:
            print("Congratulation You Won!!!!!!!")
            print("Your score : ", u_count)
            u_count = 0
        else:
            print("Computer Won")
            print("computer score : ", c_count)
            c_count = 0
    else:
        break