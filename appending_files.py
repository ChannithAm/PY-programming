#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : appending_files.py
# Author            : Channith Am <amcnith@gmail.com>
# Date              : 08.03.2019
# Last Modified Date: 08.03.2019
# Last Modified By  : Channith Am <amcnith@gmail.com>

appendMe = '\nNew bit of information'

appendFile = open('exampleFile.txt', 'a')
appendFile.write(appendMe)
appendFile.close()
