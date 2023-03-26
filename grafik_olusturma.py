import matplotlib.pyplot as plt
import numpy as np
"""
x= [1,2,3,4]
y=[1,4,9,16]
#plt.plot(x,y,color="red",linewidth="5")
#plt.plot(x,y,"--g")
plt.plot(x,y,"o--r")
plt.axis([0,6,0,20])

plt.title("grafik başlığı")
plt.xlabel("xlabel")
plt.ylabel("ylabel")

plt.show()
"""

"""
x= np.linspace(0,2,100)

plt.plot(x, x, label="linear",color="red")
plt.plot(x, x**2, label="quadric",color="yellow")
plt.plot(x, x**3, label="cubic")

plt.xlabel("x eksenim")
plt.ylabel("y eksenim")

plt.title("basit Gragiğim")

plt.legend()

plt.show()"""

"""x= np.linspace(0,2,100)
fig,axs = plt.subplots(3)

axs[0].plot( x, x, color="red")
axs[0].set_title("linear")
axs[1].plot( x, x**2, color="green")
axs[1].set_title("quadric")
axs[2].plot( x, x**3, color="blue")
axs[2].set_title("cubic")

plt.tight_layout()
plt.show()"""

"""
x= np.linspace(0,2,100)
fig,axs = plt.subplots(2,2)
fig.suptitle("grafik başlığı")

axs[0,0].plot( x, x, color="red")
axs[0,1].plot( x, x**2, color="blue")
axs[1,0].plot( x, x**3, color="green")
axs[1,1].plot( x, x**4, color="yellow")

plt.tight_layout()
plt.show()"""

import  pandas as pd

df = pd.read_excel("100şirket.xlsx")
df = df.drop(["SEKTÖR (NACE REV.2)"],axis= 1).groupby("2018 GELİR ARALIĞI (TL)").mean()
df.head().plot(subplots=True)
plt.legend()
plt.tight_layout()
plt.show() #perfect
