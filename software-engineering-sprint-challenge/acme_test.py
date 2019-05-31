#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS, inventory_report


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_method(self):
        """Test default product explode being '...boom!'."""
        prod = Product('Test Product')
        self.assertEqual(prod.explode(), '...boom!')


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme reports are super cool!"""
    def test_default_num_products(self):
        """Test default num product equals 30!"""
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        """Test that generated names are all valid"""
        products = generate_products()
        product_names = []
        legal_names = ADJECTIVES + NOUNS
        for prod in products:
            product_names += prod.name.split()
        self.assertEqual(set(product_names), set(legal_names))

    def test_inventory_report(self):
        """Test that checks printed report is in the correct format"""
        #this test rquires another import
        import sys, io

        #this redirects sys.stoudt to a buffer
        stdout = sys.stdout
        sys.stdout = io.StringIO()

        #initializie products to report
        products = generate_products()
        inventory_report(products)

        #get output and restore sys.stdout
        output = sys.stdout.getvalue()
        sys.stdout = stdout

        print('\n', output)
        

if __name__ == '__main__':
    unittest.main()
