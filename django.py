import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('campasX.xlsx')
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Embarked'].fillna("S",inplace=True)
print(df.head(10))

# classx = (df['Pclass'].unique())
# classy = (df['Pclass'].value_counts())

# plt.bar(classx,classy,color='pink')
# plt.xlabel('Class Name')
# plt.ylabel('Count of Person')
# plt.title('Class Data')
# plt.grid(color='black')
# plt.show()

# # PLOTING

fig, ax = plt.subplots(2,2,figsize=(15,10))


x = (df['Sex'].unique())
y = (df['Sex'].value_counts())

ax[0,0].bar(x,y,color='green',label='Male,Female')
ax[0,0].set_title('Analysis Male Female data')
ax[0,0].set_xlabel('Gender')
ax[0,0].set_ylabel('Total')
ax[0,0].legend()
ax[0,0].grid(color='black')


columss = (df['Embarked'].unique())
columssum = (df['Embarked'].value_counts())

ax[0,1].pie(columssum,labels=columss,colors=['red','green','blue'],autopct='%1.1f%%')
ax[0,1].set_title('Analysis Embarked Data')



agex = (df['Age'].unique())

ax[1,0].hist(agex,bins=10,edgecolor='black',color='purple',label='Age analysis')
ax[1,0].legend()
ax[1,0].set_xlabel('Person Age')
ax[1,0].set_ylabel('Total Person')
ax[1,0].set_title('Age Aaalysis')
ax[1,0].grid(color='red')



surX = (df['Survived'].unique())
surY = (df['Survived'].value_counts())

ax[1,1].pie(surY,labels=['Not Survived','Survived'],autopct='%1.1f%%')
ax[1,1].set_title('Survived Data')



fig.suptitle("Data Analysis with Python")

plt.tight_layout()
plt.savefig('Titanci_Data.png',dpi=300,bbox_inches='tight')
plt.show()



