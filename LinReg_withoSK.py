import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('headbrain.csv')
data.head()

X=data['Head Size(cm^3)'].values
Y=data['Brain weight(grams)'].values

mean_x=np.mean(X)
mean_y=np.mean(Y)

n=len(X)

numer=0
denom=0
for i in range(n):
    numer+=(X[i]-mean_x)*(Y[i]-mean_y)
    denom+=(X[i]-mean_x)**2
    b1=numer/denom
    b0=mean_y-(b1*mean_x)

print("Coefficients")
print(b1,b0)

max_x = np.max(X)+100
min_x = np.min(X)-100

x=np.linspace(min_x,max_x,1000)
y = b0+b1*x

plt.plot(x,y,color='#58b970', label='Regression Line')
plt.scatter(X,Y,c='#ef5423', label='Scatter Plot')

plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()

rmse=0
for i in range(n):
    y_pred=b0+b1*X[i]
    rmse+=(Y[i]-y_pred)**2
rmse= np.sqrt(rmse/n)
print("RMSE")
print(rmse)

ss_tot=0
ss_res=0
for i in range(n):
    y_pred= b0+b1*X[i]
    ss_tot+=(Y[i]-mean_y)**2
    ss_res+=(Y[i]-y_pred)**2
r2=1-(ss_res/ss_tot)
print("R2 Score")
print(r2)











