#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[10]:


dataset=datasets.load_iris()

data=pd.DataFrame(dataset['data'],columns=['Petal length','Petal Width','Sepal Length','Sepal Width'])
data['Species']=dataset['target']
data['Species']=data['Species'].apply(lambda x: dataset['target_names'][x])


# In[11]:


data.head(10)


# In[12]:


data.describe()


# In[13]:


data.isnull().sum()


# In[14]:


#to add new value dictonary {} and array []
#nan means its a null value
modData = data.append({'Petal length' : np.nan , 'Petal Width' : 3.6, 'Sepal Length': 0,

            'Sepal Width': 0.2, 'Species': 'setosa' } , ignore_index=True)


# In[15]:


modData.isnull().sum()


# In[16]:


print('columns w missing value')
print(modData.isnull().sum())
print('\n column with zero values')
print((modData[['Petal length','Petal Width','Sepal Length','Sepal Width']]==0).sum())


# In[17]:


#replace all zeros with null value
modData[['Petal length',

     'Petal Width',

     'Sepal Length',

     'Sepal Width','Species']] = modData[['Petal length',

                       'Petal Width',

                       'Sepal Length',

                       'Sepal Width',

                       'Species']].replace(0, np.NaN)


print('Columns with missing values')

print(modData.isnull().sum())


# In[18]:


modData.fillna(modData.mean(), inplace=True)
print(modData.isnull().sum())


# In[25]:


modData.fillna(modData.median(), inplace=True)
print(modData.isnull().sum())


# In[20]:


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# load dataset into Pandas DataFrame


# In[21]:


PCA_df = pd.read_csv(url, names=['sepal length',
                        'sepal width',
                        'petal length',
                        'petal width',
                        'target'])


# In[22]:


PCA_df.head()


# In[23]:


#using normlization as we explained in the slides
from sklearn.preprocessing import StandardScaler, MinMaxScaler


# In[24]:



features = ['sepal length', 'sepal width', 'petal length', 'petal width']

# Separating out the features
# :, gives u from the start to all colmns
x = PCA_df.loc[:, features].values

# Separating out the target

y = PCA_df.loc[:,['target']].values

# Standardizing the features

#x = StandardScaler().fit_transform(x)

#mini max feature
#x =  MinMaxScaler().fit_transform(x)

print (x)


# In[67]:


from sklearn.decomposition import PCA


# In[68]:


pca = PCA(n_components=2)


# In[69]:


principalComponents = pca.fit_transform(x)


# In[73]:


principalDf = pd.DataFrame(data = principalComponents

       , columns = ['principal component 1', 'principal component 2'])


# In[76]:


print(principalDf)


# In[80]:


finalDf = pd.concat([principalDf, PCA_df[['target']]], axis = 1)
print(finalDf)


# In[83]:


finalDf = pd.concat([principalDf, PCA_df[['target']]], axis = 1)


# In[87]:


import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

#sns.set(color_codes=True)



fig = plt.figure(figsize = (8,8))

ax = fig.add_subplot(1,1,1) 

ax.set_xlabel('principal Component 1', fontsize = 15)

ax.set_ylabel('principal Component 2', fontsize = 15)

ax.set_title('2 component PCA', fontsize = 20)

targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

colors = ['r', 'g', 'b']

for target, color in zip(targets,colors):

    indicesToKeep = finalDf['target'] == target

    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']

        , finalDf.loc[indicesToKeep, 'principal component 2']

        , c = color

        , s = 50)

ax.legend(targets)

ax.grid()




# In[ ]:




