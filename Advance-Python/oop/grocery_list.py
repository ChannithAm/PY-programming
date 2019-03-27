#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : grocery_list.py
# Author            : Channith Am <amcnith@gmail.com>
# Date              : 22.01.2019
# Last Modified Date: 22.01.2019
# Last Modified By  : Channith Am <amcnith@gmail.com>

class GroceryList(list):

    def discard(self, price):
        for product in self:
            if product.price > price:
                # Remove method is implemeted in the class "list"
                self.remove(product)
        return self

    def __str__(self):
        out = "Grocery List: \n\n"
        for p in self:
            out += "name: " + p.name + " - price: " + str(p.price) + "\n"

        return out


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

grocery_list = GroceryList()

# extend method also belongs to 'list' class
grocery_list.extend([Product("bread", 5), Product("milk", 10),
                    Product("rice", 12)])

print(grocery_list)

grocery_list.discard(11)

print(grocery_list)
