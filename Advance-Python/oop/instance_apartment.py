#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : instance_apartment.py
# Author            : Channith Am <amcnith@gmail.com>
# Date              : 21.01.2019
# Last Modified Date: 21.01.2019
# Last Modified By  : Channith Am <amcnith@gmail.com>

from create_apartment import Apartment

d1 = Apartment(_id=1, mts2=100, value=5000)

print("sold?", d1.sold)

d1.sell()
print("sold?", d1.sold)
d1.sell()
