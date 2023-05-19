from scipy.stats import nbinom
prob = 1 - nbinom.cdf(3,2,0.5) #3 Misserfolge, 2 Erfolge und 1/2 als p für ein Bernouli-Versuch
print(prob)
