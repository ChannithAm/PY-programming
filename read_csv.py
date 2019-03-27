#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : read_csv.py
# Author            : Channith Am <amcnith@gmail.com>
# Date              : 11.03.2019
# Last Modified Date: 27.03.2019
# Last Modified By  : Channith Am <amcnith@gmail.com>

import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    print(readCSV)

    dates = []
    colors = []

    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)
        
    print(dates)
    print(colors)

    try:
        whatColor = input('What color do you wish to know the date of?')
        if whatColor in colors:
            colorx = colors.index(whatColor)

            theDate = dates[colorx]
            print('The data of ', whatColor, 'is ', theDate)
        else:
            print('Color not found, or is not a color')
    except Exception as e:
        print(e)

    print('Continuing')
