import numpy as np
import matplotlib.pyplot as plt

FROM = 0
TO = 0.5
N = 1000
T = (TO-FROM)/N

x = np.linspace(start=FROM, stop=TO, num=N)
y = np.zeros(N)
for n in range(1, 6):
    y += n*np.cos(n*10*2*np.pi*x)

plt.plot(x, y)
plt.show()

xf = np.linspace(start=0.0, stop=1.0/(2.0*T), num=N//2)
yf = np.fft.fft(y)

plt.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.axis([0, 80, 0, 6])
plt.show()
