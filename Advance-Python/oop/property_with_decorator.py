#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : property_with_decorator.py
# Author            : Channith Am <amcnith@gmail.com>
# Date              : 22.01.2019
# Last Modified Date: 22.01.2019
# Last Modified By  : Channith Am <amcnith@gmail.com>

class Color:

    def __init__(self, rgb_code, name):
        self._rgb_code = rgb_code
        self._name = name

    # Create the property using the name of the attribute.
    # Then we define how to get/set/delete it.
    @property
    def name(self):
        print("Function tho get the name color")
        return self._name

    @name.setter
    def name(self, new_name):
        print("Function to set the name as {}".format(new_name))
        self._name = new_name

    @name.deleter
    def name(self):
        print("Erase the name!!")
        del self._name
