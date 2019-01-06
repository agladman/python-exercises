from random import choice


class Robot:

    def __init__(self):
        self.name = None
        self.bootcount = 0

    def __repr__(self):
        if self.bootcount == 0:
            return f'{self.__class__} | unbooted'
        else:
            return f'{self.__class__} | {self.__dict__}'

    def boot(self):
        self.bootcount += 1
        self.generate_name()

    def generate_name(self):
        used = self.load_used_names()
        while True:
            u = ''.join(next(self.upper()) for _ in range(2))
            d = ''.join(next(self.digit()) for _ in range(3))
            namestring = u + d
            if namestring not in used:
                self.name = namestring
                self.save_used_name()
                break

    @staticmethod
    def upper():
        yield choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    @staticmethod
    def digit():
        yield choice('0123456789')

    @staticmethod
    def load_used_names():
        with open('src/names.txt', 'r') as f:
            return f.readlines()

    def save_used_name(self):
        with open('src/names.txt', 'a') as f:
            f.write(self.name + '\n')
