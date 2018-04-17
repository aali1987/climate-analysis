#!/sur/bin/env python

"""
Awesome weather predictor
"""

import random


def is_raining():
    if random.random() > 0.5:
        print('it is raining')


def main():
    is_raining()


if __name__ == '__main__':
    main()
