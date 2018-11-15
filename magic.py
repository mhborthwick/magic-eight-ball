import random
import time

#business logic (calculations)
def get_fortune(xx):
    if xx > 6:
        fortune = 'Probably, maybe?'
    elif xx > 3:
        fortune = 'Almost certainly!'
    else:
        fortune = 'Answer cloudy, try again later.'

    return fortune

#user logic (interface)
def think_mystic_thoughts():
    wait = random.randint(1, 10)
    start = 0

    print('thinking....')

    while start < wait:
        print('.' * random.randint(1, 15))
        time.sleep(1)
        start += 1

def main():
    print('The magic 8 ball sees all!')
    test = input('What is your question?\n\t> ')
    test2 = test.split(' ')

    print(test2)
    
    if '?' in test2[-1]:
        think_mystic_thoughts()
        print('Your fortune is:')
        i = random.randint(1, 8)
        fortune = get_fortune(i)
        print(fortune)
    else:
        print('Enter a question pls!')

if __name__ == '__main__':
    main()
