#!/usr/bin/env python3


"""Coin Flip Simulation - Write some code that simulates flipping a
    single coin however many times the user decides. The code should
    record the outcomes and count the number of tails and heads.
    """


from random import choice


class Session():

    def __init__(self, flips, count=0, heads=0, tails=0):
        self._flips = flips
        self._count = count
        self._heads = heads
        self._tails = tails

    def __repr__(self):
        s = '<{0}.{1} object; flips {2}, count {3}, heads {4}, tails {5}.>'.format(
            self.__module__,
            type(self).__name__,
            self._flips,
            self._count,
            self._heads,
            self._tails)
        return s

    def __str__(self):
        return f'Reults from {self._heads + self._tails} flips: heads {self._heads}, tails {self._tails}.'

    def __iter__(self):
        yield self._heads
        yield self._tails

    def __add__(self, other):
        new_flips = self._flips + other._flips
        new_count = self._count + other._count
        new_heads = self._heads + other._heads
        new_tails = self._tails + other._tails
        return (new_flips, new_count, new_heads, new_tails)

    def flip(self):
        result = choice([True, False])
        if result is True:
            self._heads += 1
        else:
            self._tails += 1

    def go(self):
        for _ in range(self._flips):
            self._count += 1
            self.flip()

    def step(self):
        if self._count <= self._flips:
            self.flip()
            self._count += 1
        else:
            raise StopIteration

    @classmethod
    def best_of_three(cls):
        x = cls(3)
        x.go()
        return x

    @property
    def has_started(self):
        return self._count > 0

    @property
    def is_finished(self):
        return self._count == self._flips

    @property
    def is_tied(self):
        return self._heads == self._tails

    @property
    def has_winner(self):
        return self.is_finished and self._heads != self._tails

    @property
    def winner(self):
        if self.has_winner:
            if self._heads > self._tails:
                return 'heads'
            else:
                return 'tails'
        else:
            return None


def main():
    flips = int(input('How many times do you want to flip the coin? '))
    s = Session(flips)
    s.go()
    print(s)


if __name__ == '__main__':
    main()
