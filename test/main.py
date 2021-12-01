from scipy.fftpack import fft
import matplotlib.pyplot as plt
import numpy as np

N=2**20
dt=0.0001
t=np.arange(0,N*dt,dt)
freq=np.linspace(0,1.0/dt,N)

y=np.sin(2*np.pi*5*t)
yf=fft(y)/(N/2)

plt.figure(2)
plt.subplot(211)
plt.plot(t,y)
plt.xlim(0,1)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.subplot(212)
plt.plot(freq,np.abs(yf))
plt.xlim(0,10)
plt.ylim(0,1)
plt.xlabel("frequency")
plt.ylabel("amplitude")
plt.tight_layout()
plt.show()