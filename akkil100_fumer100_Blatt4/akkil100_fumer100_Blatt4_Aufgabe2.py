import numpy as np

a = np.genfromtxt('iris_toy.csv', delimiter=',',skip_header = 1,usecols=(0,1,2,3),dtype=np.float)
b = np.recfromcsv('iris_toy.csv',encoding = 'utf8')

#Aufgabe1
print("Aufgabe1:")
print("Zeilen:"  ,len(a))
print("Spalten:", len(a[0]))
print("\n")

#Aufgabe2
b.dtype
print("Aufgabe2:")
print('<f8 bedeutet soviel wie float64, das heißt man kann Dezimalwerte lagern und verwendet 32 bit für jede Nummer')
print('<U12 bedeutet soviel wie Unicode, 12 steht für die Anzahl an Characters')
print("\n")

#Aufgabe3
print("Aufgabe3:")
print(type(a))
print(type(b))
print("a ist ein ndarray, das heißt in diesem Array liegen ausschlieslich elemente eines einzigen Types und in dem Falle wäre dies der float Datenyp.")
print("b ist ein Array, welches Felder enthält,analog zu Spalten in einem Arbeitsblatt. Jede Eintrag kann sowohl integer als auch floats oder strings beinhalten. Das bedeutet die Spalten haben des Arrays haben demnach unterschiedliche Typen. Man kann auf die Werte mit arr.y zugreifen anstelle von arr['x'].")
print("\n")



#4
print("Aufgabe4:")
print("möchte man Aggregieren über mathematische Operationen und sollte man eventuell ndarray verwenden. Es gibt aber kein wirkliches schwarz weiß -verfahren. Es hängt speziell von den Daten ab")
print("\n")


#Aufgabe5
print("Aufgabe5:")
print(a.max(axis=0))
print("bei a wird für jede Spalte ein Maximum bestimmt, dh. man geht komplett die eine Spalte von oben nach unten durch und bestimmt für Spalte 1 den Max. Analog macht man dies für alle weiteren Spalten. Man erhält letzendlich einen Vektor mit allen Maxima spaltenweise")
print("\n")



#Aufgabe6
print("Aufgabe6:")
#print(b.max(axis=0))
print("Vermutlich liegt es daran weil max eine mathematische Operation ist aber die letzte Spalte von b ist eine Spalte mit String Elementen, wie soll man dafür den max bestimmen? Die vorherigen Spalten sind nicht kompaitbel mit der letzten Spalte")
print("\n")


#Aufgabe7
print("Aufgabe7:")
print(np.argmax(a, axis=0))









