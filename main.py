import math
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import make_interp_spline

matplotlib.use('TkAgg')

#Функция для прорисовывания общего графика
def oneGraph(x, masOneGraph, g, t, axs):
    masColor = ['k', 'k', 'k', 'k', 'k', 'k', 'k', 'tab:red']
    for i in range(0, len(masOneGraph)):
        X_Y_Spline = make_interp_spline(x, masOneGraph[i])
        X_ = np.linspace(x.min(), x.max(), 500)
        Y_ = X_Y_Spline(X_)
        axs[g, t].plot(X_, Y_, color=masColor[i])
        axs[g, t].set_ylabel('f(t)')
        axs[g, t].set_xlabel("t")


def masGraph(masK, masFt, axs):
    x = np.array(masK)
    Ki = 0
    masOneGraph = []

    # Основной график прорисовывается во всех окнах для фиксации значений оси.
    yO = np.array(masFt)
    X_Y_Spline = make_interp_spline(x, yO)
    X_O = np.linspace(x.min(), x.max(), 500)
    Y_O = X_Y_Spline(X_O)

    for g in range(0, k // 2 + 1):
        for t in range(0, 2):
            masElementGraph = [0] * 7

            if g == k // 2 and t == 1:
                masElementGraph = masFt
                y = np.array(masElementGraph)
                masOneGraph.append(y)
                oneGraph(x, masOneGraph, g, t, axs)
                return
            else:
                masElementGraph[Ki] = masFt[Ki]

            if Ki == 0:
                strfω = "0"
            else:
                strfω = f'f({Ki}/2ω)'
            y = np.array(masElementGraph)
            masOneGraph.append(y)

            X_Y_Spline = make_interp_spline(x, y)

            X_ = np.linspace(x.min(), x.max(), 500)
            Y_ = X_Y_Spline(X_)
            axs[g, t].plot(X_O, Y_O, color="w", label = f'n = {Ki}')
            axs[g, t].plot(X_, Y_, label = strfω)
            axs[g, t].set_ylabel(f'f{Ki}(t)')
            axs[g, t].set_xlabel("t")
            axs[g, t].legend()
            Ki += 1


def F_t(t, fc, k, ftInp):
    pi = math.pi
    masK = []
    masFt = []
    dT = 1 / (2 * fc)
    Wc = 2 * pi * fc
    res = 0

    fig, axs = plt.subplots(4, 2, figsize=(15, 15))

    for ki in range(0, k + 1):
        chisl = math.sin(Wc * (t - dT))
        znam = Wc * (t - dT)

        Ft = ftInp[ki] * (chisl) / (znam)
        res += Ft
        masFt.append(Ft)
        masK.append(ki)

    masGraph(masK, masFt, axs)
    plt.show()
    return res


T = int(input("T = "))
Fc = int(input("fc = "))
k = int(input("k = "))

#Высоты квантованного отчёта
ftInp = [0.5, 0.6, 1.2, 2.1, 2.8, 2.3, 1.1]

ft = F_t(T, Fc, k, ftInp)
print(str(ft))
