#!/usr/bin/env python
# coding: utf-8

# In[4]:


# 1. Shift Left K Cells:

def shiftLeft(source, k):
    length = len(source)
    for i in range(length):
        if i + k < length:
            source[i] = source[i + k]
        else:
            source[i] = 0
    print(source)

source = [10, 20, 30, 40, 50, 60]
shiftLeft(source, 3)


# In[12]:


# 2. Rotate Left K Cells:

def rotateLeft(source, k):

    if not source or k <= 0:
        return
    
    k = k % len(source)
    
    rotated_array = source[k:] + source[:k]
    
    source[:] = rotated_array

source = [10, 20, 30, 40, 50, 60]
rotateLeft(source, 3)
print(source)


# In[14]:


# 3. Remove an element from an array:

def remove(source, size, idx):
    
    if idx < 0 or idx >= size:
        return
    
    for i in range(idx, size - 1):
        source[i] = source[i + 1]
    
    source[size - 1] = 0

source = [10, 20, 30, 40, 50, 0, 0]
remove(source, 5, 2)
print(source)


# In[17]:


# 4. Remove all occurrences of a particular element from an array:

def removeAll(source, size, element):
    
    i = 0
    while i < size:
        if source[i] == element:

            for j in range(i, size - 1):
                source[j] = source[j + 1]
            size -= 1 
        else:
            i += 1
    
    for i in range(size, len(source)):
        source[i] = 0

source = [10, 2, 30, 2, 50, 2, 2, 0, 0]
removeAll(source, 7, 2)
print(source)


# In[ ]:




