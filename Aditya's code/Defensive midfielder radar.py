# -*- coding: utf-8 -*-
"""
Created on Sun May 17 15:30:50 2020

@author: Aditya
"""

import pandas as pd
from math import pi
import matplotlib.pyplot as plt
%matplotlib inline

def createRadar(player, data):
    Attributes = ["DCS","PD","Passes completed","Progressive passing","Tackles Won","Dribbled past","Succesfull pressures","Intercepting Passes","Erro percentage"]
    
    data += data [:1]
    
    angles = [n / 9* 2 * pi for n in range(9)]
    angles += angles [:1]
    
    ax = plt.subplot(111, polar=True)

    plt.xticks(angles[:-1],Attributes)
    ax.plot(angles,data)
    ax.fill(angles, data, 'blue', alpha=0.1)

    ax.set_title(player)
    plt.show()
    
    
    
    
    createRadar("Partey",[34.0,54.1,82.4,32.7,64.1,31.8,30.9,17.6,8.0])
    
#DCS=Dribbles completed Succesfullly(in percentage)
#PD=Progrssive Distance[in percentage,prog dist/total sit*100)
#passes completed is in percentage
#progrssive passes(Progdist/Toataldist*100)
#Tackeles won in percentage ,i.e tackles won upon total tackels
#Number of times players driblled past-percentage of dribblers tackled
#Suucessfull pressures oalso in percentage(sucesspress/totalpress*100)
#intercepting passes=intercepting passes per 90*10
#errors=error/number of games*100