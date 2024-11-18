import numpy as np
import matplotlib.pyplot as plt

R = 1e6 #ohm
C = 1.5e-6 #farhad

def v(t):
    return 9 * (1 - np.exp(-t/(R * C)))

t = np.linspace(0, 10, 1000)
y_verdi = v(t)


def les_liste(tekstfil):
    with open(tekstfil, "r") as f:
        innhold = f.readlines()
        tider = []
        spenninger = []
        
        for linje in innhold:
            tid = linje.split(",")[0]
            spenning = linje.split(",")[1]
            
            tider.append(float(tid))
            spenninger.append(float(spenning))
    return tider, spenninger

tider, spenninger = les_liste("/Users/steff/OneDrive - NTNU/Dokumenter/1.Termin/matte/RC-krets.txt")
        
plt.plot(tider, spenninger)
plt.plot(t, y_verdi)
plt.xlabel("t")
plt.ylabel("v(t)")
plt.grid()
plt.legend()
plt.show()