def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input('Your name: ')
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input('Remainders of dividing your age by 3: '))
    rem5 = int(input('Remainders of dividing your age by 5: '))
    rem7 = int(input('Remainders of dividing your age by 7: '))

    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input('Number: '))
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print("Is Python similar to Parceltongue?")
    print("1. Yes, both are snake-y")
    print("2. Definitely not")
    print("3. I guess?")
    print("4. What?")
    answer = input('Your answer (1-4): ')
    if answer == 2:
        print('Completed, have a nice day!')
    elif answer == 1:
        print('Well yes, but actually no.')
    else:
        print('Better luck next time.')


def end():
    print('Congratulations, have a nice day!')
