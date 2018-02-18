import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics

#Question 1
iris = pd.read_csv('Iris.csv')
print(iris)

#Question 2
headers=list(iris)
print(headers)

#Question 3
features=headers[1:5]
print(features)

#Question 4
print(iris[1:6])

#Question 5
label = iris[['Id']] 
df1 = iris[['SepalLengthCm']]
df2 = iris[['SepalWidthCm']]
df3 = iris[['PetalLengthCm']]
df4 = iris[['PetalWidthCm']]
plt.scatter(label,df1)
plt.xlabel('label')
plt.ylabel('SepalLengthCm')
plt.show()
plt.scatter(label,df2)
plt.xlabel('label')
plt.ylabel('SepalWidthCm')
plt.show()
plt.scatter(label,df3)
plt.xlabel('label')
plt.ylabel('PetalLengthCm')
plt.show()
plt.scatter(label,df4)
plt.xlabel('label')
plt.ylabel('PetalWidthCm')
plt.show()

#Question 6
print("Range: ",min(iris['SepalLengthCm']),"-",max(iris['SepalLengthCm']))
s1=sorted(iris['SepalLengthCm'],reverse=True)
print("Second Largest Element: ", s1[1])

#Question 7
print("Mean Width: ",np.mean(np.array(iris['SepalWidthCm'])))

#Question 8
iris['Length'] = np.where(iris['SepalLengthCm']<5, 'Small', 'Large')
print(iris)

#Question 9
df = pd.DataFrame(iris)
grouped = df.groupby('Species')
print(grouped.get_group('Iris-setosa'))
print(grouped.get_group('Iris-virginica'))
print(grouped.get_group('Iris-versicolor'))
df5 = iris[['Species']]
plt.hist(df5,bins=3)
plt.show()

#Question 10
print("Deviation: ", statistics.stdev(iris['SepalLengthCm']))

#Question 11
corr1=iris['SepalLengthCm'].corr(iris['PetalLengthCm'])
corr2=iris['SepalLengthCm'].corr(iris['PetalWidthCm'])
corr3=iris['SepalLengthCm'].corr(iris['SepalWidthCm'])
corr4=iris['SepalWidthCm'].corr(iris['PetalLengthCm'])
corr5=iris['SepalWidthCm'].corr(iris['PetalWidthCm'])
corr6=iris['PetalLengthCm'].corr(iris['PetalWidthCm'])
print(corr1,corr2,corr3,corr4,corr5,corr6)
print("Columns with more than 70% percent correlation are: ")
if abs(iris['SepalLengthCm'].corr(iris['PetalLengthCm']))>.7:
	print("SepalLengthCm and PetalLengthCm ",corr1)
if abs(iris['SepalLengthCm'].corr(iris['PetalWidthCm']))>.7:
	print("SepalLengthCm and PetalWidthCm ",corr2)
if abs(iris['SepalLengthCm'].corr(iris['SepalWidthCm']))>.7:
	print("SepalLengthCm and SepalWidthCm ",corr3)
if abs(iris['SepalWidthCm'].corr(iris['PetalLengthCm']))>.7:
	print("SepalWidthCm and PetalLengthCm ",corr4)
if abs(iris['SepalWidthCm'].corr(iris['PetalWidthCm']))>.7:
	print("SepalWidthCm and PetalWidthCm ",corr5)
if abs(iris['PetalLengthCm'].corr(iris['PetalWidthCm']))>.7:
	print("PetalLengthCm and PetalWidthCm ",corr6)

#12
df=df.fillna(df.mean())

#13
df.to_csv('newiris', sep='\t')