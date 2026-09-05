import pandas as pd
import matplotlib.pyplot as plt

"""
data = pd.DataFrame({
    "Students":["Max","Nathan","Arnold","Tom","Paul"],
    "Marks":["86","97","73","56","48"]
})

plt.bar(data["Students"],data["Marks"])
plt.show()
#X axis represents the independent variable:position,time,etc...
#Y axis represents the dependent variable:quantity,etc...

plt.plot(x,y,"ro") #ro means red circles
plt.show()

plt.plot(x,y,"g^") #g^ means green triangles
plt.show()

plt.plot(x,y,"r--") #r-- means red dashed lines
plt.show()

plt.plot(x,y,"b--") #b-- means blue dashed lines
plt.show()

plt.plot(x,y,"b-") #b- means blue line
plt.show()
"""
x = [1,2,3,4,5]
y = [1,2,3,4,5]

#Controlling the axis
plt.plot(x,y)
plt.axis([0,10,0,200]) #[xMin,xMax,yMin,yMax]
plt.show()

#Adding labels,titles,legends
plt.plot(x,y,"b-",label="Y=X") #lineWidth to decide the width of the line
plt.axis([0,6,0,6])
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Sample Graph")
plt.legend()
plt.show()

#Plot multiple graphs in a single plot
plt.plot([1,2,3,4,5],[2,4,6,8,10],"r--",label="Y=X**2")
plt.plot([1,2,3,4,5],[3,6,9,12,15],"b-",label="Y=X**3")
plt.axis([0,6,0,20])
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Sample Graph 2")
plt.legend()
plt.show()

df = pd.read_csv("titanic.csv")
survival = df["Survived"].value_counts()
plt.bar(["Didn't Survive","Survived"],survival)
plt.xlabel("Passenger Statues")
plt.ylabel("Number of Passengers")
plt.title("Titanic Passengers Survival")
plt.show()