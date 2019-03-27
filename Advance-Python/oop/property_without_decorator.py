#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : property_without_decorator.py
# Author            : Channith Am <amcnith@gmail.com>
# Date              : 22.01.2019
# Last Modified Date: 22.01.2019
# Last Modified By  : Channith Am <amcnith@gmail.com>

class Color:

    def __init__(self, rgb_code, name):
        self.rgb_code = rgb_code
        self._name = name

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    name = property(get_name, set_name)
