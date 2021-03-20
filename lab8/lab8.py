#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install mlxtend


# In[3]:


from mlxtend.frequent_patterns import apriori


# In[4]:


dataset = [['Drink', 'Nuts', 'Diaper'],

      ['Drink', 'Coffee', 'Diaper'],

      ['Drink', 'Diaper', 'Eggs'],

      ['Nuts', 'Eggs', 'Milk'],

      ['Nuts', 'Coffee', 'Diaper', 'Eggs', 'Milk']
         
          ]


# In[5]:


dataset


# In[6]:


import pandas as pd

from mlxtend.preprocessing import TransactionEncoder



TranEncod = TransactionEncoder()

te_ary = TranEncod.fit(dataset).transform(dataset)

df = pd.DataFrame(te_ary, columns=TranEncod.columns_)


# In[7]:


df


# In[8]:


apriori(df, min_support=0.6)


# In[9]:


apriori(df , min_support=0.6, use_colnames=True)


# In[29]:


apriori(df , min_support=0.5, use_colnames=True)


# ## 1.3

# In[46]:


frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)

frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))

frequent_itemsets


# In[47]:




frequent_itemsets[ (frequent_itemsets['length'] == 2) &

          (frequent_itemsets['support'] >= 0.5) ]


# In[57]:


frequent_itemsets[ frequent_itemsets['itemsets'] == {'Diaper', 'Drink'} ]


# In[59]:




