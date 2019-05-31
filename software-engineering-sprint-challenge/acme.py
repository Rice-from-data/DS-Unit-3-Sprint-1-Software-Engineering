'''
Product class to hold all of our products
'''

import random


class Product:
    '''
    A generalizable class to hold all Acme products
    '''

    def __init__(self, name=None, price=10, weight=20, flammability=0.5, 
                 identifier=random.randint(1000000,10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        '''
        Calculates the desirability of stealing this product
        '''
        steal_factor = self.price / self.weight

        if steal_factor < 0.5:
            return 'Not so stealable...'
        elif 0.5 <= steal_factor < 1:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'
    
    def explode(self):
        '''
        Calculates the explosive potential of the product
        '''
        exp_pot = self.flammability * self.weight

        if exp_pot < 10:
            return '...fizzle.'
        if 10 <= exp_pot < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    '''
    A specific product inheriting from Product with a weight of 10
    '''
    def __init__(self, name=None, price=10, weight=10, flammability=0.5, 
                 identifier=random.randint(1000000,10000000)):
        super().__init__(name=name, price=price, weight=weight, 
                        flammability=flammability, identifier=identifier)

    def explode(self):
        '''
        override explode method
        '''
        return "...it's a glove."

    def punch(self):
        '''
        what did you think this was for?
        '''
        if self.weight < 5:
            return "That tickles."
        if 5 <= self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
