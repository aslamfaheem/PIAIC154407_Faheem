#!/usr/bin/env python
# coding: utf-8

# # NumPy Exercise - 1

# In[5]:


import numpy as np

a = np.arange(15).reshape(3,5)

a


# Attribute# 1: The dimensions of the array

# In[6]:


a.shape


# Attribute# 2: The number of axes (dimensions) of the array

# In[7]:


a.ndim


# Attribute# 3: An object describing the type of the elements in the array

# In[9]:


a.dtype.name


# Attribute# 4: The size in bytes of each element of the array

# In[11]:


a.itemsize


# Attribute# 5: The total number of elements of the array

# In[12]:


a.size


# Attribute# 6

# In[13]:


a.dtype


# Attribute# 7

# In[16]:


b = np.array([1.2, 3.5, 5.1])
b.dtype


# Attribute#8: The function zeros creates an array full of zeros

# In[18]:


np.zeros((3,4))


# Attribute#9: the function ones creates an array full of ones

# In[25]:


np.ones((3,4), dtype = np.int16)


# Attribute#10: the function empty creates an array whose initial content is random and depends on the state of the memory

# In[29]:


np.empty((3,3))


# Attribute#11: To create sequences of numbers, NumPy provides the arange function

# In[30]:


np.arange(10, 30, 5)


# Attribute#12: Linspapce

# In[32]:


from numpy import pi
np.linspace(0,2,9)


# Attribute#13: Print 1d array

# In[33]:


a = np.arange(6)
print(a)


# Attribute#14: Printing 2d array

# In[34]:


b = np.arange(12).reshape(4,3)
print(b)


# Attribute#15: Printing 3d array

# In[35]:


c = np.arange(24).reshape(2,3,4)
print(c)


# Attribute#16: Arithmetic Operations

# In[39]:


a = np.array([20,30,40,50])
b = np.arange(4)
c = a - b
print(c)


# Attribute17: Arithmetic Operation 2

# In[40]:


d = a * b
print(d)


# Attribute18: Arithmetic Operations 3

# In[41]:


e = b**2
print(e)


# Attribute19: Arithmetic Operations 4

# In[43]:


a = np.array([[2, 3],[4, 2]])
b = np.array([[2, 0],[3, 4]])
a @ b


# Attribute20: Arithmetic Operation 5

# In[45]:


a.dot(b)


# Attribute21: Aritmetic Operations 6

# In[69]:


a = np.ones((2, 3), dtype= np.int)
a


# In[70]:


a *= 3
a


# Attribute22: Arithmetic Operations 7

# In[71]:


a += 2
a


# Attribute#23: Unray Operations 1

# In[78]:


a = np.arange(12).reshape(3, 4)
a


# In[79]:


a.sum()


# Attribute#24: Unray Operations 2

# In[80]:


a.min()


# Attribute#25: Unray Operations 3

# In[81]:


a.max()


# Attribute#26: Unray Operations 4

# In[82]:


a.sum(axis=0)


# Attribute#27: Unray Operations 5

# In[83]:


a.max(axis=0)


# Attribute#28: Unray Operations 5

# In[84]:


a.min(axis=1)


# Attribute#29: Unray Operations 6

# In[85]:


a.cumsum(axis=0)


# Attribute#30: Universal Function

# In[86]:


a = np.arange(3)
a
np.exp(a)


# Attribute#31: Universal Function 2

# In[87]:


np.sqrt(a)


# Attribute#32: Universal Function 3

# In[88]:


np.min(a)


# Attribute#33: Universal Function 4

# In[89]:


b = np.array([1, -1, 2])
np.add(a,b)


# Attribute#34: Universal Function 5

# In[90]:


np.nonzero(a)


# Attribute#35: Universal Function 6

# In[91]:


np.average(a)


# Attribute#36: Universal Function 7

# In[94]:


np.sum(a)


# Attribute#37: Indexing, Slicing, Iterating 1

# In[98]:


a = np.arange(10)**3
a


# In[99]:


a[2]


# Attribute#38: Indexing, Slicing, Iterating 2

# In[100]:


a[2:5]


# Attribute#39: Indexing, Slicing, Iterating 3

# In[105]:


a[:8:2] = 1000
a


# Attribute#40: Indexing, Slicing, Iterating 4

# In[107]:


a[::-1]


# Attribute#41: Indexing, Slicing, Iterating 5

# In[108]:


for i in a:
    print(i**(1/3))


# Attribute#42: Indexing, Slicing, Iterating 6

# In[110]:


def f(x, y):
    return 10 * x + y

b = np.fromfunction(f, (5, 4), dtype=int)
b


# In[111]:


b[2, 3]


# Attribute#43: Indexing, Slicing, Iterating 7

# In[116]:


b[0:5, 2]


# Attribute#44: Indexing, Slicing, Iterating 8

# In[119]:


b[1: 4, :]


# Attribute#45: Shape 1

# In[123]:


a = np.floor(10 * rg.random((3, 4)))
a


# In[124]:


a.ravel()


# Attribute#46: Shape 2

# In[125]:


a.reshape(6,2)


# Attribute#47: Shape 3

# In[126]:


a.T


# Attribute#48: Shape 4

# In[127]:


a.T.shape


# Attribute#49: Shape 5

# In[128]:


a.shape


# Attribute#50: Shape 6

# In[132]:


a


# In[134]:


a.resize((3,4))
a


# In[ ]:




