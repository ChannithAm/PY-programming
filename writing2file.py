#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : writing2file.py
# Author            : Channith Am <amcnith@gmail.com>
# Date              : 08.03.2019
# Last Modified Date: 08.03.2019
# Last Modified By  : Channith Am <amcnith@gmail.com>

text = 'Sample Text to Save\nNew line!'

saveFile = open('exampleFile.txt', 'w')
saveFile.write(text)
saveFile.close()
