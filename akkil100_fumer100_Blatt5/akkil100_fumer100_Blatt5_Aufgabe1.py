from matplotlib import pyplot as plt
import numpy as np

url="https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
data=np.genfromtxt(url, delimiter=",")
klasse=data[:,0].astype("i8")
unique, counts=np.unique(klasse, return_counts=True)
alcohol=data[:,1]

alcohol_by_class=[alcohol[data[:,0]==c] for c in(1,2,3)]



for alcohol_class in alcohol_by_class:
    plt.boxplot(alcohol_class,vert=True,patch_artist=True);   
    plt.show()
    
    
print("Boxplots eignen sich zum Vergleich von Bereich und Verteilung von Gruppen mit Zahlendaten. Vorteile: Boxplots strukturieren große Datenmengen und machen Ausreißerwerte sichtbar. Man kann anhand eines Boxplots wichtige Lageparameter erkennen. Zur ersten Sichtung der Daten ist dies hilfreich, daher sollte dieser ins Skript")
