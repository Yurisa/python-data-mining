# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt  
import scipy as sp
x = np.array([23.80, 27.60, 31.60, 32.40, 33.70, 34.90, 43.20,52.80,63.80,73.40])
y = np.array((41.40, 51.8, 61.70, 67.90,68.70,77.50,95.90,137.40,155.0,175.0))

xmean = np.mean(x)
ymean = np.mean(y)
Lxx = np.sum((x-xmean)**2)
Lxy = np.sum((y-ymean)*(x-xmean))
b1 = Lxy/Lxx
b0 = ymean - b1*xmean
y1 = b1*x+b0
plt.plot(x, y, 'b*')#,label=$cos(x^2)$)
plt.plot(x,y1,'r')
plt.xlabel("x value")
plt.ylabel("y value")
plt.xlim(20,80)
plt.ylim(40, 200)
plt.title('x-y data')
plt.legend()
plt.show()
z1 = np.polyfit(x, y, 1)  #一次多项式拟合，相当于线性拟合
z2 = np.polyfit(x,y,2)
y2 = z2[0]*x*x+z2[1]*x+z2[2]
r1 = sum((y1-y)**2)/10
r2 = sum((y2-y)**2)/10

p1 = np.poly1d(z1)
p2 = np.poly1d(z2)
print(p1)
print(p2)
#from sklearn.linear_model import LinearRegression  
#linreg = LinearRegression()  
#model=linreg.fit((x**x,x), y)  

