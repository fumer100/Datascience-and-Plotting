import numpy as np
import random

n = 10
xs = np.random.rand(n)
type(xs)

def transform_nobranch(xs):
    return (xs < 0.5).astype(int)*(2*xs-1) + (xs >= 0.5).astype(int)*np.round((3*xs+0.5))

ys = transform_nobranch(xs)
ys

print(ys)
print(type(ys))
print("Argument1: Zeitintensiv, man sollte nicht versuchen jetzt jede Methode zu vektorieseren, da dies Zeit in anspruch nimmt und das Projek wichtiger ist. -> Es ist ein Trade-Off")
print("Argument2:Da man mehrere Prozessoren verwendet, steigen die Kosten und der Verbrauch der CPU, nicht jeder Comeputer kann sich das leisten")

