#!/usr/bin/env python3


symbols = list(' !"#$%&''()*+,-./:;<=>?@[\]^_`{|}~')

inputs = [
'samsung',
'galaxy',
'panasonic',
'hewlett',
'packard',
'pavillion',
'pavilion',
'hannis',
'brother',
'epson',
'lenovo',
'thinkpad',
'asus',
'google',
'microsoft',
'windows',
'android',
'dell',
'goldstar',
'syncmaster',
'lucky',
'flatron',
'hanns',
'hannsg',
'apple',
'tplink',
'uniden',
'vtech',
'plantronics',
'motorola',
'logitech'
]

for e1 in inputs:
    for e2 in inputs:
        if e1 != e2:
            for d in range(100):
                print(f'{e1}{d:02}{e2}')
                for s in symbols:
                    print(f'{e1}{d:02}{e2}{s}')
