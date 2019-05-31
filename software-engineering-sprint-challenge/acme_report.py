#!/usr/bin/env python
"""
A module to generate random products and summarize them.
"""

from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']

NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    '''
    Method to generate a list (default length 30) of random products
    '''
    products = []

    for i in range(1, num_products+1):
        prod = Product(name=ADJECTIVES[randint(0, 4)] + ' '
                 + NOUNS[randint(0, 4)], price=randint(5, 100), 
                 weight=randint(5, 100), flammability=uniform(0, 2.5))
        products.append(prod)

    return products


def inventory_report(products):
    '''
    Method to print a summary of a list of products
    '''
    names = []
    prices = []
    weights = []
    flam = []

    # fill our field lists from our product lists
    for prod in products:
        names.append(prod.name)
        prices.append(prod.price)
        weights.append(prod.weight)
        flam.append(prod.flammability)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names: ', len(set(names)))
    print('Average price: ', sum(prices)/len(prices))
    print('Average weight: ', sum(weights)/len(weights))
    print('Average flammability: ', sum(flam)/len(flam))

if __name__ == '__main__':
    inventory_report(generate_products())
