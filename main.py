import random
import time
import argparse

symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'

def generate(path_file, length_from, length_to, amount):
    start = time.time()

    with open(path_file, 'w') as f:
        for _ in range(amount):
            for _ in range(random.randint(length_from, length_to)):
                f.write(random.choice(symbols))

            f.write('\n')

    print('Generation time:', time.time() - start)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Password Generator')
    parser.add_argument('f', type=str, help='File path')
    parser.add_argument('lf', type=int, help='Password length from')
    parser.add_argument('lt', type=int, help='Password length up to')
    parser.add_argument('a', type=int, help='Amount')

    args = parser.parse_args()
    generate(args.f, args.lf, args.lt, args.a)
