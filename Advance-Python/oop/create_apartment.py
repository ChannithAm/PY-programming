#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : create_apartment.py
# Author            : Channith Am <amcnith@gmail.com>
# Date              : 21.01.2019
# Last Modified Date: 21.01.2019
# Last Modified By  : Channith Am <amcnith@gmail.com>

class Apartment:
    '''
    Class that reprecesnts an apartment for sale
    value is in USD
    '''
    def __init__(self, _id, mts2, value):
        self._id = _id
        self.mts2 = mts2
        self.value = value
        self.sold = False

    def sell(self):
        if not self.sold:
            self.sold = True
        else:
            print("Apartment {} was sold".format(self._id))
