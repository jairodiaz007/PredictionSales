#!/usr/bin/env python
# coding: utf-8

# In[198]:


import openpyxl as xl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[202]:


path='E:/Study/Data Science/Ocula/'
fileName = 'ventas20190101-20231231.xlsx'
path = path+fileName
prediction2023 = 2023
df = pd.read_excel(path, sheet_name='SummarySells')
specificRow=df.iloc[0]
value=np.array([2019,2020,2021,2022])
TotalSelling=np.array(specificRow)
print(TotalSelling)
def fx(x1,coef):
    fx=0
    n=len(coef)-1
    for p in coef:        
        fx=fx+p*x1**n        
        n=n-1        
    return fx

for i in range(0,4):
    coef = np.polyfit(value,TotalSelling,i)
    p = np.polyval(coef,prediction2023)
    print(f"para grado: {i} la prediccion es {p}")
    x1=np.linspace(2019, prediction2023 + 1, 6)    
    y1=fx(x1,coef)
    
    plt.figure(figsize=[30,10])
    plt.title("cantidad de ventas vs año para grado: " + str(i))    

    plt.scatter(value,TotalSelling,s=120,c='blue')
    plt.plot(x1,y1,"-",linewidth=3,color="orange")
    
    plt.scatter(prediction2023,p,s=150,c='red')
    
    plt.yticks(range(5000000,1000000000,100000000))
    plt.grid("on")
    ax=plt.gca()  
    ax.set_xlabel("$años$")
    ax.set_ylabel("$Dinero$")
    plt.show()



# In[ ]:




