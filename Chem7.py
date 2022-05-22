"""

Práctica 7 - Química
Grado en Física - Universidad de Alicante
Luis Lucas García

"""

import matplotlib.pyplot as plt
import numpy as np

entrada = open("datos2", "r")

vAg, vTio, t1, t2, t3 = [], [], [], [], []

for linea in entrada:
    
    vAg.append(float(linea.split()[0]))
    vTio.append(float(linea.split()[1]))
    t1.append(float(linea.split()[2]))
    t2.append(float(linea.split()[3]))
    t3.append(float(linea.split()[4]))
    
entrada.close()

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.title("Experimento 1")
plt.plot(vTio, t1, "r*")
plt.xlabel("$ V_{Na_{2}SO_{3}} $ (mL)")
plt.ylabel("t (s)")
plt.subplot(1, 3, 2)
plt.title("Experimento 2")
plt.plot(vTio, t2, "r*")
plt.xlabel("$ V_{Na_{2}SO_{3}} $ (mL)")
plt.ylabel("t (s)")
plt.subplot(1, 3, 3)
plt.title("Experimento 3")
plt.plot(vTio, t2, "r*")
plt.xlabel("$ V_{Na_{2}SO_{3}} $ (mL)")
plt.ylabel("t (s)")
plt.savefig("scatterdatos.png", dpi=1200)

y1 = [np.log(1/i) for i in t1]
y2 = [np.log(1/i) for i in t2]
y3 = [np.log(1/i) for i in t3]
x = [0.2] + [(vTio[i]*0.2)/(vAg[i] + vTio[i]) for i in range(1, len(vTio))]

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.title("Experimento 1")
plt.plot(x, y1, "g*")
plt.xlabel("$ [Na_{2}SO_{3}]_{0} $")
plt.ylabel("- ln t")
plt.subplot(1, 3, 2)
plt.title("Experimento 2")
plt.plot(x, y2, "g*")
plt.xlabel("$ [Na_{2}SO_{3}]_{0} $")
plt.ylabel("- ln t")
plt.subplot(1, 3, 3)
plt.title("Experimento 3")
plt.plot(x, y3, "g*")
plt.xlabel("$ [Na_{2}SO_{3}]_{0} $")
plt.ylabel("- ln t")
plt.savefig("scatterajuste.png", dpi=1200)

P1 = np.polyfit(x, y1, 1) #m = 11.642
P2 = np.polyfit(x, y2, 1) #m = 12.428
P3 = np.polyfit(x, y3, 1) #m = 12.443
print((11.642 + 12.428 + 12.443)/3)

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.title("Experimento 1")
plt.plot(x, y1, "g*")
plt.plot(x, np.polyval(P1, x), label="Recta de ajuste")
plt.xlabel("$ [Na_{2}SO_{3}]_{0} $")
plt.ylabel("- ln t")
plt.legend()
plt.subplot(1, 3, 2)
plt.title("Experimento 2")
plt.plot(x, y2, "g*")
plt.plot(x, np.polyval(P2, x), label="Recta de ajuste")
plt.xlabel("$ [Na_{2}SO_{3}]_{0} $")
plt.ylabel("- ln t")
plt.subplot(1, 3, 3)
plt.title("Experimento 3")
plt.plot(x, y3, "g*")
plt.plot(x, np.polyval(P3, x), label="Recta de ajuste")
plt.xlabel("$ [Na_{2}SO_{3}]_{0} $")
plt.ylabel("- ln t")
plt.savefig("rectajuste.png", dpi=1200)