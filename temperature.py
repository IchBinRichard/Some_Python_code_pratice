#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 15:46:09 2022

@author: lijiaheng
"""

#攝氏轉華氏 或 華氏轉攝氏

def F_temp_to_C ():
    F_temp = float(input('華氏溫度：'))
    C_temp = float(5/9) * (F_temp - 32) 
    print('華氏溫度 %5.2f度，等於攝氏溫度 %5.2f度' %(F_temp, C_temp))

def C_temp_to_F ():    
    C_temp = float(input('攝氏溫度：'))
    F_temp = 1.8 * C_temp + 32 
    print('攝氏溫度 %5.2f度，等於華氏溫度 %5.2f度' %(C_temp, F_temp))
    
def temp_trans():
    enter = int(input('華氏轉攝氏請輸入1，攝氏轉華氏請輸入2，結束請輸入0:'))
    if enter == 1:
        F_temp_to_C()
        temp_trans()
    elif enter == 2:
        C_temp_to_F()
        temp_trans()
    elif enter != 0:
        print('選項錯誤，重來一次')
        temp_trans()
    else:
        print("謝謝您的使用！")
        return 

temp_trans()
    