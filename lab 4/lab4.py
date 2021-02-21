#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# numpy library for equations deal with numbers and arrays and it can use for 
#algebra and liner 


# In[ ]:


#if u dont have it type pip install numpy


# In[ ]:


#to open all library we use import ### from ###


# In[ ]:


#down here we import numpy as np to shortcut the name (numpy)
#and arange is mean 


# In[53]:


help(np.ndarray) #help(function) to know functions help


# In[5]:


# reshape do re oreder array 
import numpy as np
a = np.arange(15)
a


# In[1]:


import numpy as np
a = np.arange(15).reshape(3, 5)
a


# ## 1.1 arrays

# In[2]:


import numpy as np 

print(np.array([8, 4, 6, 0, 2]))


# In[6]:


print('create a 2-d array by passing a list of lists into array().')
A = np.array( [ [1, 2, 3],[4, 5,6], [7, 8, 9] ] )
print(A)

# here to access 2d first bracket for the arrays and second 
#array for the element iside the array 
#so here a[0.1] mean array 0 and 1
#and a(1.2)mean array 0 elemnt 1 and elemnt2 in array 1
print('Access elemnts of the array with brackets.')
print(A[0, 1], A[1, 2])

print('the elemnts of a 2-d array are 1d arrays')
print(A[0])


# ## exercise 1.1

# In[75]:


import numpy as np


a = np.array([[3, 1 , 4],[1 , 5 , 9]])
b = np.array([[2,4,5,6],[1,7,9,3],[3,2,7,2]])
x=np.dot(a, b)
x


# ## exrcise 1.2

# In[ ]:


#np.ndarray -> go to help(ndarray) and give example 


# In[80]:


import numpy as np
a = np.array([1, 2, 3,4,5], ndmin = 2) 
a


# ## 1.2 basic array operations

# In[8]:


# here the operations on arrays 
#operations on arrays are differnt that usual operations
print('Addition concatenates lists together')
print([1, 2, 3]+[4, 5, 6])

print('mutliplication concatenates a list with itself a given number of times')
print([1, 2, 3] * 4)


# ## exercise 1.3

# In[10]:


x=np.array([3, -4, 1])
y=np.array([5, 2, 3])
z = x + 10


print(z)


# ##  1.4 array attributes

# In[39]:



# from 0 to 50 add 10
x = np.arange(0, 50, 10)
index = np.array([3, 1, 4])
print(x)
print(x[index])

mask = np.array([True, False, False, True, False])
print(x[mask])


# ## ex 1.4

# In[83]:


A = np.array([[1, 2, 3],[4, 5, 6]])
A.ndim


# In[84]:


A = np.array([[1, 2, 3],[4, 5, 6]])
A.shape


# In[85]:


A = np.array([[1, 2, 3],[4, 5, 6]])
A.size


# ## ex1.5

# In[88]:


A = np.array([[1, 2, 3],[4, 5, 6]])
print(A.dtype)


# In[90]:


A = np.array([[1, 2, 3],[4, 5, 6]])
A = A = A.astype('float64')
print(A.dtype)


# ## 1.5 data access ex1.6

# In[92]:


x = np.arange(10)
print(x)


# In[98]:


x = np.arange(10)
x[3]


# In[96]:


x = np.arange(10)
x[4:]


# In[97]:


x = np.arange(10)
x[4:8]


# ## ex 1.7

# In[102]:


x= np.array([[0,1,2,3,4],[5,6,7,8,9]])

x[ : , 2 : ]


# In[101]:


x= np.array([[0,1,2,3,4],[5,6,7,8,9]])
x[1, 2]


# ##  1.5.2 fancy indexing

# In[11]:


y= np.arange(10, 20, 2)
print(y)
mask = y > 15
print(mask)
print(y[mask])

y[mask] = 100
print(y)


# In[ ]:


#sklearn library 


# In[11]:


from sklearn import datasets

iris = datasets.load_iris()
print(iris.filename)


# In[ ]:


#this library give data set default


# In[21]:


import numpy as np 
iris_data = np.genfromtxt('C:\\Users\\2\\anaconda3\\lib\\site-packages\\sklearn\\datasets\\data\\iris.csv', delimiter=",", skip_header=1)
print(iris_data)


# In[19]:


#column names
iris.feature_names


# In[113]:


import numpy as np 
iris_data = np.genfromtxt('C:\\Users\\2\\anaconda3\\lib\\site-packages\\sklearn\\datasets\\data\\iris.csv', delimiter=",", skip_header=1)

print("mean of {} is {}".format(iris.feature_names[0], iris_data[:,0].mean()))


# ## 2.working on iris.csv file ex 2

# In[118]:


print(iris_data[3, : ].mean())


# In[117]:


print(iris_data[3, : ].std())


# In[116]:



print(iris_data[3, : ].var())


# In[115]:


print(iris_data[3, : ].max())


# In[114]:


print(iris_data[3, : ].min())


# In[ ]:




