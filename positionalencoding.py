import numpy as np
import matplotlib.pyplot as plt

def getPositionalEncoding(seq_len, d, n=10000):
    P = np.zeros((seq_len, d))
    for k in range(seq_len):
        for i in np.arange(int(d/2)):
            denominator = np.power(n, 2*i/d)
            P[k, 2*i] = np.sin(k/denominator)
            P[k, 2*i+1] = np.cos(k/denominator)

    return P

P = getPositionalEncoding(seq_len=6,d =6, n=100)
print(P)
cax = plt.matshow(P)
plt.gcf()

def plotSinosoid(k, d=512, n=10000):
    x = np.arange(0,100,1)
    denominator = np.power(n, 2*x/d)
    y = np.sin(k/denominator)
    plt.plot(x, y)
    plt.title('k='+str(k))


fig = plt.figure(figsize=(15,4))
for i in range(4):
    plt.subplot(141+i)
    plotSinosoid(i*4)
plt.show()



