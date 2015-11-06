#!/usr/bin/env python3
# -*- coding: utf-8 -*-


height = float(input('Height(m): '))
weight = float(input('Weight(KG): '))


bml = weight / (height * height)

if bml >= 32:
    print('Severe obesity') #ÑÏÖØ·ÊÅÖ
elif bml >= 28:
    print('Obesity') #·ÊÅÖ
elif bml >= 25:
    print('Overweight')
elif bml >= 18.5:
    print('Normal')
else:
    print('Too light')
