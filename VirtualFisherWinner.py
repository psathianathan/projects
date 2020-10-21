# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 01:54:45 2020

@author: Dhushi
"""

import pyautogui as pg
#import time
import numpy as np
pg.PAUSE = 10

pg.FailSafeException = True

pg.PAUSE
i = 0
while i < 5:
    n = np.random.randint(0,10)
    if n>1 and n<5:
        pg.typewrite('%f\n')
        pg.PAUSE = np.random.uniform(4,7)
        pg.PAUSE
        pg.typewrite('I love fishing\n')
    elif n>=5:
        pg.typewrite('%fish\n')
        pg.PAUSE = np.random.uniform(5,6)
        pg.PAUSE
        pg.typewrite('Fishing is great\n')
    elif n == 1:
        pg.typewrite('%s a\n')
        pg.PAUSE = 1
        pg.PAUSE
    else:
        pg.typewrite('%sell all\n')
        pg.PAUSE = 1
        pg.PAUSE
    pg.PAUSE