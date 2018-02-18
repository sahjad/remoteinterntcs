import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Question 1
df1= pd.read_csv('ign.csv')
df2= pd.read_csv('ign_score.csv')
df_merged= pd.merge(df1,df2,on='id')
print(df_merged)

#Question 2
df3=df_merged[['title','score']]
sorted_df = df3.sort_values(by='score',ascending=False)
name_sorted_df = sorted_df[['title']]
print(name_sorted_df[0:10])

#Question 3
df4= df_merged
df4['Rank'] = df4['score'].rank(ascending=False,method='min')
print(df4[['title','score','Rank']])


#Question 4
gen= df_merged[['genre']]
sco= df_merged[['score']]
plt.xlabel('genre')
plt.ylabel('score')
plt.scatter(gen,sco)
plt.show()

#Question 5
grouped = df_merged.groupby('genre')
g_a_s= grouped['score'].agg(np.mean)
ff=g_a_s.sort_values(ascending=False)
print(ff[[0]])

#Question 6
print(pd.pivot_table(df_merged,index=["genre","title"],values=["score"]))