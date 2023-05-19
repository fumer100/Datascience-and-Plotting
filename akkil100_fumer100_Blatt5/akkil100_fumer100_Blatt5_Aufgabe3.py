import numpy as np
from matplotlib import pyplot as plt
from scipy import stats as st


print("1: weight-height.csv")
print("\n")
url = "https://www.kaggle.com/datasets/mustafaali96/weight-height"
print("2:", url)
print("\n")


data = np.genfromtxt("weight-height.csv",delimiter=",")
data

print("3:",np.shape(data))
print("\n")
print("4: Sind Männer größer als Frauen?, Sind Männer schwerer als Frauen?, Gibt es einen linearen Zusammenhang zwischen Größe und Gewicht?, Größe und Gewicht sind normalverteilt ?" )




height = data[:,1]
weight = data[:,2]

def isNan(num):
    return num != num


height[isNan(height)] = 0
height[height == 0] = np.mean(height) 
weight[isNan(weight)] = 0
weight[weight == 0] = np.mean(weight) 
print("\n")
print("5:")
print("minHeight:",np.min(height),
      "maxHeight:",np.max(height),
      "meanHeight:",np.mean(height)
     )
print("\n")
print("minWeight:",np.min(weight),
      "maxWeight:",np.max(weight),
      "meanWeight:",np.mean(weight)
     )


mu,sigma = st.norm.fit(height)
x=np.linspace(np.min(height)-0.5, np.max(height)+0.5,50)
plt.plot(x,st.norm(mu,sigma).pdf(x))
plt.hist(height,density = True,bins=15)
plt.title("height")
plt.show()


mu,sigma = st.norm.fit(weight)
x=np.linspace(np.min(weight)-0.5, np.max(weight)+0.5,50)
plt.plot(x,st.norm(mu,sigma).pdf(x))
plt.hist(weight,density = True,bins=15)
plt.title("weight")
plt.show()
plt.title("Height vs Weight")
plt.scatter(weight,height,alpha = 0.5)
plt.show()




print("\n")
print("6:Meine Erwartung zu der Größe wurde erfüllt, mein Bauchgefühl sagte, die Größe ist eindeutig normalverteilt und in der Tat, ist sie es")
print("Am Scatter plot erkenne ich dass eine positive Korrealation zwischen der Größe und Gewicht gibt, meine Vermutung stimmte ebeno ")
print("Was mich überascht hat ist dass das Gewicht nicht eindeutig normalverteilt ist sondern bimodal bzw. eine andere Form der Normalverteilung.")


print("\n")
print("7: Mich hätte es interesiert ob diese Korrelation auch wirklich kausal ist oder nur wegen der Stichprobe dieser Zusammenhang exisitert!"
)
print(" Ich hätte gerne das Verhältnis von Männern und Frauen näher betrachtet aber leider sind die Variabelnspalte alle auf NaN gesetzt. Dies wird mir dadurch erschwert. Mithilfe Pandas müsste aber dies möglich sein")
