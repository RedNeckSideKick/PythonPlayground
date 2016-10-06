# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 14:41:05 2016

@author: ekessel
"""

import matplotlib.pyplot as plt

leftSpace = 15
rightSpace = 30
topSpace = 3
bottomSpace = 3

dates = [
1665,
1674,
1838,
1839,
1855]

heights = [
-1,
 1,
-2,
 2,
 0]

names = [
"Hooke",
"Leewenhoek",
"Schleiden",
"Schwann",
"Virchow"]

fig = plt.figure(1)
plt.subplot(111)
plt.cla()
axis = plt.subplot(312)

plt.grid()

for n in range(dates.__len__()):
   plt.text(dates[n] + 3, heights[n], names[n]) 

plt.plot(dates,heights,'s')
axis.get_yaxis().set_visible(False)
plt.axis([dates[0] - leftSpace, dates[dates.__len__()-1] + rightSpace, -bottomSpace, topSpace])
plt.title("Cell Theory Contributors Timeline\n")
plt.xlabel("Year")