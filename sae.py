

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:40:55 2023

@author: aakhrib
"""

# -*- coding: utf-8 -*-

# TP semaine-2  (2022-2023 ) sattistique descriptive  R2.08

import numpy as np  
import matplotlib.pyplot as plt
import numpy.random as alea

plt.close('all')

#---------------------------------------------------------------

def moyenne(data):   
    n = len(data)
    moy=(np.sum(data))/n
    return moy

def variance(data):  
    tapP = []
    for x in data:
        tapP.append(x*x)

    var = moyenne(tapP)-(moyenne(data))**2
    return var

def covariance(dataX,dataY):  
    # n=len(dataX)
    cov = (moyenne(dataX*dataY))-(moyenne(dataX)*moyenne(dataY))
    return cov


def ecartType(data):
    ecart_type = np.std(data)
    return ecart_type





# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------moy, écart-typ------------------------------------

# Ensemble de données-----------------------------------------------------------------------------------------------------------------
valeurs1 = [-2.127, -0.274, -0.938, -0.972, 1.394, -1.787, 0.451, -0.027, -2.358, 0.825, 2.042, -1.618, 0.338, 1.333, 1.421, -1.796, 2.193, -0.282, 0.336, 2.357, 1.384, -0.318, -0.93, 0.75, 2.06, -1.918, -0.043, -2.044, -0.257, -2.095, -1.849, 1.659, -1.196, -1.134, -0.75, 0.123, -2.384, 2.236, 1.121, 0.584, 1.11, -0.312, 1.641, 2.382, -1.344, -1.83, -1.276, 2.079, -1.534, -1.017, 0.356, -1.877, -1.657, -0.621, 1.675, 2.393, 1.166, -1.876, 0.484, -1.464, -2.419, 0.601, 0.578, 2.015, 1.748, -1.764, 1.496, -2.068, -0.468, 2.427, -0.999, -0.65, 0.338, 0.749, 0.117, 2.379, -0.189, -0.259, -1.391, 0.642, -1.822, -0.317, -2.015, 2.342, -0.68, -2.462, -1.045, -2.318, 2.396, -2.203, 1.366, 2.132, -1.082, -1.474, -1.85, 1.475, 0.156, -0.695, 0.674, 2.184]
valeurs2 = [-1.309, -0.609, 1.165, 1.05, 2.421, -0.497, 0.278, 0.463, 0.565, 0.43, -0.189, 0.638, -1.986, 1.836, -0.123, 0.954, 1.554, -1.436, -0.245, -0.234, -0.104, -1.6, -0.481, 0.789, -0.565, -1.259, 0.428, -0.11, 0.357, 0.192, 0.566, 0.821, -1.336, -0.246, -0.635, -0.021, 0.175, 0.817, 0.627, -0.034, 1.681, 1.665, -1.149, 0.62, -1.308, -2.435, 0.739, 0.523, -0.849, 1.467, 1.848, -0.397, -1.225, -0.246, -1.066, 1.498, 0.753, 0.205, -0.358, -1.422, 0.83, -1.073, 0.431, 0.151, 1.486, 1.466, 0.016, 0.978, -0.225, 1.529, -0.359, -0.675, 0.998, 0.178, -1.749, -1.87, -0.389, -1.524, -0.556, -1.293, 1.539, -1.483, -0.222, -0.038, 0.933, -0.917, -2.551, 0.16, -2.057, 0.182, -0.551, -0.133, -0.165, -0.104, -1.698, -0.59, -1.882, 0.856, -0.076, -0.409]
valeurs3 = [8.649, 1.9, 3.254, 2.45, -0.902, 4.961, 0.09, 0.63, 11.236, 1.2, -1.551, 6.139, -0.938, -0.574, 1.1, 6.955, 0.664, 0.934, 0.393, 0.37, -1.102, 3.656, 2.378, -0.261, -0.856, 6.877, 1.13, 6.428, 0.067, 9.157, 7.213, -0.384, 4.301, 3.32, 3.697, 0.682, 11.909, 0.453, 0.335, -0.29, 0.108, 0.785, 0.939, -1.085, 3.586, 5.27, 3.11, 1.697, 5.068, 2.778, 1.019, 8.008, 5.3, 1.464, -0.106, 0.45, 0.144, 5.703, 1.164, 4.026, 11.161, 0.161, -0.424, -1.167, -0.877, 6.885, 0.629, 8.758, 1.247, -0.105, 3.362, 2.172, 1.52, -0.378, 1.161, 1.292, 0.461, 0.865, 2.912, 0.197, 4.871, 1.368, 7.249, 0.938, 1.719, 10.49, 2.725, 9.139, 0.493, 9.582, 1.266, -0.592, 2.265, 4.385, 6.742, 0.224, -0.609, 1.049, -0.656, 0.243]
valeurs4 = [-2.091, -3.598, 1.839, 1.923, 4.103, -2.163, -2.969, 0.751, -0.173, -1.366, -0.216, 2.128, -4.707, 3.807, 0.347, 0.02, 0.983, -4.6, -0.393, 1.586, -1.37, -2.15, 0.415, 3.594, -4.012, -1.775, -0.488, -3.718, -3.237, -0.319, -1.158, -0.058, -2.688, -1.413, -1.149, -0.073, -2.179, -0.006, 0.155, -1.212, 4.678, 1.947, -2.904, 0.957, -3.819, -5.262, -0.044, -1.209, -2.178, 2.664, 0.12, -2.351, -3.666, 0.03, 0.176, 2.17, 2.399, -2.035, -3.294, -5.111, -1.144, -2.946, 14.862, -2.058, 1.097, 0.1, -3.236, 1.412, -2.475, 1.326, -1.782, -0.439, 0.658, -1.01, -6.347, -4.809, -1.678, -3.468, -3.242, -3.91, 0.348, -0.495, -0.741, -0.115, -0.959, -0.657, -6.829, 0.651, -2.859, -0.119, -0.603, -2.656, -1.824, -0.427, 25.604, -0.439, -3.409, -0.729, 43.848, -3.462]


# Histogrammes
inter1 = [-3, -2.75, -2.5, -2.25, -2, -1.75, -1.5, -1.25, -1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]

plt.hist(valeurs1, bins=inter1, rwidth=0.8)  # Création de l'histogramme 1
plt.xlabel('Valeurs ')
plt.xticks(np.arange(-3, 4))
plt.ylabel('Nombres')
plt.title("VAL 1 : " + "Moy : " + str(moyenne(valeurs1)) + " σ : " + str(ecartType(valeurs1)))
plt.show()


inter2 = [-3, -2.75, -2.5, -2.25, -2, -1.75, -1.5, -1.25, -1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5]

plt.hist(valeurs2, bins=inter2, rwidth=0.8)  # Création de l'histogramme 2
plt.xlabel('Valeurs ')
plt.xticks(np.arange(-3, 4))
plt.ylabel('Nombres')
plt.title("VAL 2 : " + "Moy = " + str(moyenne(valeurs2)) + " σ = " + str(ecartType(valeurs2)))
plt.show()


inter3 = [-2.,   -1.75, -1.5,  -1.25, -1.,   -0.75, -0.5,  -0.25,  0.,    0.25,  0.5,   0.75,  1.,    1.25,  1.5,   1.75,  2.,    2.25,  2.5,   2.75,  3.,    3.25,  3.5,   3.75,  4.,    4.25,  4.5,   4.75,  5.,    5.25,  5.5,   5.75,  6.,    6.25,  6.5,   6.75,  7.,    7.25,  7.5,   7.75,  8.,    8.25,  8.5,   8.75,  9.,    9.25,  9.5,   9.75, 10.,   10.25, 10.5,  10.75, 11.,   11.25, 11.5,  11.75, 12.]

plt.hist(valeurs3, bins=inter3, rwidth=0.8)  # Création de l'histogramme 3
plt.xlabel('Valeurs ')
plt.xticks(np.arange(-2, 13))
plt.ylabel('Nombres')
plt.title("VAL 3 : " + "Moy = " + str(moyenne(valeurs3)) + " σ = " + str(ecartType(valeurs3)))
plt.show()


inter4 = [-3, -2.75, -2.5, -2.25, -2, -1.75, -1.5, -1.25, -1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]

plt.hist(valeurs4, bins=inter4, rwidth=0.8)  # Création de l'histogramme 4
plt.xlabel('Valeurs ')
plt.xticks(np.arange(-3, 4))
plt.ylabel('Nombres')
plt.title("VAL 4 : " + "Moy = " + str(moyenne(valeurs4)) + " σ = " + str(ecartType(valeurs4)))
plt.show()

# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------


# Affichage des observations

print("Info pour Valeurs 1")
print(" ")
print(" ")
print("La moyenne est égale à " + str(moyenne(valeurs1)))
print(" ")
print("La variance est égale à " + str(variance(valeurs1)))
print(" ")
print("L'écart-type est égal à " + str(ecartType(valeurs1)))
print(" ")
print(" ")


print("Info pour Valeurs 2")
print(" ")
print(" ")
print("La moyenne est égale à " + str(moyenne(valeurs2)))
print(" ")
print("La variance est égale à " + str(variance(valeurs2)))
print(" ")
print("L'écart-type est égal à " + str(ecartType(valeurs2)))
print(" ")
print(" ")


print("Info pour Valeurs 3")
print(" ")
print(" ")
print("La moyenne est égale à " + str(moyenne(valeurs3)))
print(" ")
print("La variance est égale à " + str(variance(valeurs3)))
print(" ")
print("L'écart-type est égal à " + str(ecartType(valeurs3)))
print(" ")
print(" ")


print("Info pour Valeurs 4")
print(" ")
print(" ")
print("La moyenne est égale à " + str(moyenne(valeurs4)))
print(" ")
print("La variance est égale à " + str(variance(valeurs4)))
print(" ")
print("L'écart-type est égal à " + str(ecartType(valeurs4)))
print(" ")
print(" ")


# Nuages de points :

""" Nuage avec VALEUR 1 & VALEUR 2 """
plt.scatter(valeurs1, valeurs2)
plt.title("Nuage de points comparant valeurs1 & valeurs2")
plt.xlabel("Valeurs 1")
plt.ylabel("Valeurs 2")
plt.savefig("NuageDePoints-1.png")
plt.show()


""" Nuage avec VALEUR 1 & VALEUR 3 """
plt.scatter(valeurs1, valeurs3)
plt.title("Nuage de points comparant valeurs1 & valeurs2")
plt.xlabel("Valeurs 1")
plt.ylabel("Valeurs 3")
plt.savefig("NuageDePoints-2.png")
plt.show()


""" Nuage avec VALEUR 2 & VALEUR 3 """
plt.scatter(valeurs2, valeurs3)
plt.title("Nuage de points comparant valeurs1 & valeurs2")
plt.xlabel("Valeurs 2")
plt.ylabel("Valeurs 3")
plt.savefig("NuageDePoints-3.png")
plt.show()


""" Nuage avec VALEUR 2 & VALEUR 4 """
plt.scatter(valeurs2, valeurs4)
plt.title("Nuage de points comparant valeurs1 & valeurs2")
plt.xlabel("Valeurs 2")
plt.ylabel("Valeurs 4")
plt.savefig("NuageDePoints-4.png")
plt.show()
