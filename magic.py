import random
import time


def get_fortune(i=3):
    if i == 1:
        fortune = 'Probably, maybe?'
    if i == 2:
        fortune = 'Almost certainly!'
    else:
        fortune = 'Answer cloudy, try again later.'

    return fortune


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
    input('What is your question?\n\t> ')
    think_mystic_thoughts()
    print('Your fortune is:')
    i = random.randint(1, 8)
    fortune = get_fortune()
    print(fortune)


if __name__ == '__main__':
    main()
