import random 
import string
import os
import progressbar
import time
 
bar = progressbar.ProgressBar(widgets=[progressbar.Bar(left='[', marker='=', right=']')]).start()

t = 0
while t < 100:
    bar.update(t)
    t += 1
    time.sleep(0.1)

bar.finish()