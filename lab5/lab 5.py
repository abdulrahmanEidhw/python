#!/usr/bin/env python
# coding: utf-8

# In[4]:


# importing required libraies
import pandas as pd
import numpy as np
import seaborn as sns #visualisation
import matplotlib.pyplot as plt #drawing library
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[5]:


x = np.linspace(0, 10, 100)

fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--')


# In[9]:


from sklearn import datasets
iris = datasets.load_iris()
df= pd.read_csv(iris.filename)
#df.describe()
df.head(5)


# In[87]:


df_with_columns=pd.read_csv(r'C:\Users\2\anaconda3\lib\site-packages\sklearn\datasets\data\iris.csv',
                        delimiter=',',
                        header=0,
                        names=['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)','Variety'])
df_with_columns.head()


# ## high level static

# In[48]:


print(df_with_columns["Variety"].value_counts())


# In[44]:


print(df_with_columns.shape)


# In[49]:


print(df_with_columns.describe())


# ## data visualaisation

# In[50]:


for ojha, feature in enumerate(list(df_with_columns.columns)[:-1]):
    fg = sns.FacetGrid(df_with_columns, hue='Variety', height=5)
    fg.map(sns.distplot, feature).add_legend()
    plt.show()


# In[54]:


sns.boxplot(x='Variety', y='petal length (cm)', data=df_with_columns)
plt.show()


# In[58]:


sns.violinplot(x='Variety',y='petal length (cm)',data=df_with_columns)
plt.show()


# In[83]:


data=df_with_columns.plot(kind='scatter',x='sepal length (cm)',y='sepal width (cm)',c= 'g')
plt.show


# In[84]:


sns.set_style("whitegrid")
sns.FacetGrid(df_with_columns, hue="Variety",height=10)     .map(plt.scatter, "sepal length (cm)","sepal width (cm)")     .add_legend();
plt.show();


# In[89]:


sns.set_style("whitegrid");
sns.pairplot(df_with_columns,vars = iris.feature_names, hue = 'Variety', diag_kind = 'kde',
              plot_kws = {'alpha': 0.6, 's': 80, 'edgecolor': 'k'}, size =2)
plt.show()


# In[ ]:




